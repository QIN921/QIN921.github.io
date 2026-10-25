import hashlib
import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlparse
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
MANIFEST = json.loads((ROOT / 'tests/legacy_manifest.json').read_text())

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href') and value:
                self.urls.append(value)

class MigrationTests(unittest.TestCase):
    def test_identity_and_personal_content(self):
        home = (SITE / 'index.html').read_text()
        for text in ('Chuqin Zhou', 'Shanghai Jiao Tong', 'Huazhong', 'Research Interest', 'zhouchuqin@sjtu.edu.cn'):
            self.assertIn(text, home)
        self.assertNotRegex(home, r'Xiangxiang Dai|Zeyu Zhang|Your Name|profile.png|clustrmaps')
        self.assertNotIn('<img src="/images/"', home)
        papers = (SITE / 'publications/index.html').read_text()
        for text in ('Differentiable VMAF', 'Controllable Distortion-Perception', 'Large language model for lossless', 'Bandwidth-efficient'):
            self.assertIn(text, papers)

    def test_scholar_publications_and_github_avatar(self):
        page = (SITE / 'publications/index.html').read_text()
        expected = json.loads((ROOT / '_data/publications.json').read_text())
        self.assertEqual(len(expected), 15)
        for paper in expected:
            self.assertIn(paper['title'], page)
            self.assertIn(paper['url'].replace('&', '&amp;'), page)
        self.assertIn('Year not specified', page)
        self.assertIn('Chuqin Zhou*', page)
        home = (SITE / 'index.html').read_text()
        self.assertIn('/images/github-avatar.jpg', home)
        self.assertIn('eA17fngAAAAJ', home)
        self.assertGreater((SITE / 'images/github-avatar.jpg').stat().st_size, 1000)

    def test_preview_assets_and_navigation_use_current_origin(self):
        home = (SITE / 'index.html').read_text()
        self.assertRegex(home, r'href="/assets/css/main\.css\?v=\d+"')
        self.assertIn('href="/publications/"', home)
        self.assertIn('src="/assets/js/main.min.js"', home)

    def test_all_legacy_urls_and_assets_survive(self):
        for name, digest in MANIFEST.items():
            source = ROOT / 'docs' / name
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), digest, name)
            if name.endswith('.md'):
                dest = SITE / (name[:-3] + '.html')
                self.assertTrue(dest.is_file(), str(dest))
            elif name.startswith(('deep_learning/', 'video_compression/')):
                self.assertEqual(hashlib.sha256((SITE / name).read_bytes()).hexdigest(), digest, name)
        self.assertEqual((SITE / 'CNAME').read_text().strip(), 'qin921.github.io')

    def test_wiki_renders_notes_instead_of_a_redirect(self):
        wiki = (SITE / 'wiki/index.html').read_text()
        self.assertIn('Deep Learning', wiki)
        self.assertIn('Video Compression', wiki)
        self.assertNotIn('http-equiv="refresh"', wiki)
        expected = [name[:-3]+'.html' for name in MANIFEST if name.endswith('.md') and name.startswith(('deep_learning/', 'video_compression/'))]
        for path in expected:
            self.assertIn('/'+path, wiki)

    def test_internal_links_have_targets(self):
        broken = []
        for page in SITE.rglob('*.html'):
            parser = Links()
            parser.feed(page.read_text())
            for url in parser.urls:
                parts = urlparse(url)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                path = unquote(parts.path)
                target = SITE / path.lstrip('/') if path.startswith('/') else page.parent / path
                if target.is_dir():
                    target = target / 'index.html'
                if not target.is_file():
                    broken.append(f'{page.relative_to(SITE)}: {url}')
        self.assertTrue(any(SITE.rglob('*.html')), 'Build output missing')
        self.assertEqual(broken, [])

if __name__ == '__main__':
    unittest.main()
