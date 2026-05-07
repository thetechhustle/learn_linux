# QA Checklist

Use this checklist before merging course modernization work.

## Build and navigation

- [ ] `mkdocs build --strict` passes.
- [ ] Root README points learners to the web course path.
- [ ] Main navigation exposes Home, Course, Lessons, and Project notes.
- [ ] Search works in the generated site.
- [ ] Mobile layout keeps the hero, cards, and navigation readable.

## Content quality

- [ ] Lessons include objectives, field story, operator principle, hands-on practice, and review questions.
- [ ] Commands prefer modern Linux tools unless legacy behavior is explicitly being taught.
- [ ] Risky commands include lab/snapshot/safety context.
- [ ] Chapter ordering matches the learner path.
- [ ] Glossary covers repeated core terms.

## Technical hygiene

- [ ] No zero-byte Markdown files remain.
- [ ] No broken relative Markdown links remain.
- [ ] No generated `site/` output is committed.
- [ ] Requirements are pinned enough for repeatable local builds.
- [ ] GitHub Actions builds on pull requests.

## Reviewer notes

Record any unresolved issue with a path, reason, and recommended fix before merge.
