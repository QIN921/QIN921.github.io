# AcademicPages Migration Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Migrate Chuqin Zhou’s existing homepage to the AcademicPages layout used by the supplied reference sites.

**Architecture:** Reuse the MIT-licensed layout, includes, Sass and bundled browser assets from xiangxdai/xiangxdai.github.io. Keep original content under docs for provenance; publish migrated notes at their old .html paths and use Jekyll for the new profile pages. Build to gh-pages to preserve the existing deployment model.

**Tech Stack:** Jekyll 3.10, Liquid, Sass, Markdown, GitHub Actions, Python standard-library verification.

**Spec:** docs/superpowers/specs/2026-10-25-homepage-design.md

## Global Constraints
- Match the reference’s white background, gray sans-serif text, cyan links, masthead and left author sidebar.
- Preserve the existing four papers, education, award, notes, static images and valid CNAME.
- Do not copy reference personal content, portraits, tracking accounts or demo pages.
- Deliver a preview and reviewable source; do not publish automatically during this task.

## Review Focus
- Old note .html URLs and relative images must still resolve.
- No template-owner identity or sample content appears in generated pages.
- No blank avatar generates a broken image.
- Mobile menu and profile links remain accessible without horizontal overflow.
- Workflow deploys generated files to existing gh-pages rather than publishing repository source.

### Task 1: Template and personal pages
- [x] Capture a manifest of the original notes and images; create migration tests before editing.
- [x] Import only theme directories, retaining upstream MIT license separately from the original GPL license.
- [x] Create _config.yml, Gemfile, _data/navigation.yml, _pages/about.md, publications.md, awards.md and wiki.md.
- [x] Remove template tracking, demo assets and identity; guard the optional avatar and add IEEE author link.
- [x] Verify the generated homepage, all four publications and navigation destinations.

### Task 2: Notes and deployment
- [x] Copy existing note directories to root, add front matter and explicit old .html permalinks, preserving relative assets.
- [x] Provide /index.html and /self.html compatibility; use canonical /wiki/ (avoid case-only aliases on macOS) and a sitemap page.
- [x] Preserve CNAME and replace the MkDocs build workflow with Ruby/Jekyll build and gh-pages publication on master only.
- [x] Write local preview and deployment instructions with research-interest text marked for owner review in the handoff.
- [x] Verify note coverage, asset integrity, and internal links in the built site.

### Task 3: Build, preview and handoff
- [x] Resolve dependencies and run bundle exec jekyll build --strict_front_matter.
- [x] Run python3 -m unittest discover -s tests against _site; verify relative links, notes, assets and identities.
- [x] Serve locally; inspect homepage, publications and Wiki; check desktop/mobile rendering and menus.
- [x] Obtain an independent final code review and resolve material findings.
- [x] Commit locally, export source ZIP and screenshots to outputs, and provide preview; no push or online publication.
