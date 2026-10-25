# Chuqin Zhou’s homepage

A Jekyll / AcademicPages academic homepage, styled after the supplied reference websites.

## Local preview

Install Ruby 3.3 and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Open http://127.0.0.1:4000. To verify the migration:

```sh
bundle exec jekyll build --strict_front_matter
python3 -m unittest discover -s tests
```

## Edit content

- `_config.yml`: name, bio, contact links; add `author.avatar` only after placing your own image in `images/`.
- `_pages/about.md`: biography, research interests, education and experience.
- `_pages/publications.md` and `_pages/awards.md`: publications and awards.
- `_data/navigation.yml`: top navigation.
- `_pages/wiki.md`, `deep_learning/`, `video_compression/`: study notes.

## Deployment

The workflow builds Jekyll and publishes `_site` to `gh-pages` on pushes to `master` or a manual run on `master`. Keep GitHub Pages set to **Deploy from a branch → gh-pages → / (root)**, matching the old deployment model. The workflow requires repository Actions write permission. This change has not been pushed or published automatically.

`CNAME` preserves the existing `qin921.github.io` value. Original MkDocs files remain in `docs/`, `overrides/`, `mkdocs.yml` and `requirements.txt` for reference, excluded from the generated site. Notes retain their former `.html` URLs and adjacent images. `/self.html` redirects to the homepage.

## Attribution

Theme source: https://github.com/xiangxdai/xiangxdai.github.io at `59e14e72b4f3925c6145e2f6465631bef9f213fb` (AcademicPages / Minimal Mistakes). Only reusable theme files were imported; the reference owner’s biography, publications, portrait and tracking settings were not copied. Theme copyright and MIT license are retained in `licenses/academicpages-MIT.txt`. Original repository license remains in `LICENSE`.
