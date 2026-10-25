# Migration notes

- Source baseline: QIN921/QIN921.github.io at 1be79d30f8f8d2d3b50833183b9159ce4809550c.
- Theme source: xiangxdai/xiangxdai.github.io (see README and licenses).
- No portrait was available in the original repository, so the optional avatar is hidden.
- Research interests and the short research paragraph were summarized from existing papers and should be reviewed by the owner.
- Education, papers and award reproduce the old homepage; no new achievements, years, paper links or Scholar account were invented.
- The old source files are preserved, with their SHA-256 hashes recorded in tests/legacy_manifest.json.
- No visitor map or third-party analytics account is enabled.

- Wiki uses `/wiki/` only: a case-only `/Wiki/` redirect collides on case-insensitive macOS filesystems and is intentionally omitted.

## Validation

A clean export of tracked source passed `bundle exec jekyll build --strict_front_matter` and all 5 migration checks (identity, old URLs/assets, local preview navigation/assets, Wiki content, internal links). Browser checks covered desktop layout, 390-pixel iframe layout, mobile navigation/profile dropdowns, publications, Wiki and a math-rendered note. Local build used Ruby 2.6.10 and Jekyll 3.10.0; GitHub Actions with Ruby 3.3 has been configured but has not run remotely.

Independent review identified a `vendor/` ignore rule dropping Sass dependencies; the rule was scoped to `/vendor/`, and clean-source rebuild verified the fix.

The preview is local only; no branch was pushed and no online deployment was triggered.

## Scholar and avatar update — 2026-10-25

- Avatar downloaded from https://github.com/QIN921.png, stored locally in images/github-avatar.jpg.
- 15 publications read from https://scholar.google.com/citations?user=eA17fngAAAAJ&hl=zh-CN and their article detail pages. Titles, full author lists, venues, article/PDF links are stored in _data/publications.json.
- Formal venue years are used for AAAI 2025 and TCSVT 2026, although Scholar lists their first-posted years as 2024 and 2025 respectively. Original Scholar year is retained in the data.
- The Perceptual Neural Video Compression entry has no date or venue in Scholar; retained under Year not specified, with its OpenReview link.
- Long challenge-paper author lists are collapsed; all authors remain available. Author asterisks are retained as shown in Scholar; no contribution interpretation is added.
- No live citation counts are displayed to avoid presenting stale metrics.
