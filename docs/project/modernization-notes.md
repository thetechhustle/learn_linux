# Modernization Notes

This branch converts Learn Linux from a raw Markdown draft into a structured, buildable course site.

## Concerns documented and addressed

| Concern | Resolution |
| --- | --- |
| Markdown-only repo with no web layer | Added MkDocs Material, `mkdocs.yml`, theme assets, CSS, JavaScript, and build commands. |
| Broken root README link to missing `02_linux_basics` | Replaced the old README and moved canonical course pages under `docs/`. |
| Empty duplicate files with colon names | Removed 27 zero-byte duplicate Markdown files with the modernization script. |
| No course landing page | Added `docs/index.md` and a modern GitHub `README.md`. |
| No learner setup path | Added `docs/course/lab-setup.md`. |
| No full-course structure | Added overview, syllabus, glossary, capstone, and explicit MkDocs navigation. |
| Outdated command examples | Modernization script updates common examples from `ifconfig` to `ip address`, `netstat` to `ss`, `service` to `systemctl`, `yum` to `dnf`, `apt-get` to `apt`, and Quagga references toward FRRouting. |
| Weak learning experience | Added lesson scaffolding: learning objectives, field story, operator principle, hands-on practice, and review questions. |
| No license | Added MIT license. |
| No repeatable QA/build path | Added `requirements.txt`, `Makefile`, GitHub Actions workflow, and QA checklist. |

## Framework decision

MkDocs Material was chosen because this repo is already plain Markdown and needs a polished open-source course site without forcing a React/MDX migration.

Alternatives considered:

- Docusaurus: strong for React-heavy MDX and interactive components, but higher migration cost.
- VitePress: clean and fast, but less course/docs functionality out of the box.
- Docsify: very fast prototype, but weaker static build, SEO, and validation story.

## Remaining editorial work

The content is now structured and safer, but it still deserves a deeper human editorial pass before public launch:

- Verify every command against current Ubuntu LTS and Rocky Linux/AlmaLinux.
- Replace generic explanations with more precise examples where needed.
- Add screenshots or terminal recordings for high-value labs.
- Expand chapter-level exercises into downloadable lab sheets.
- Decide whether MIT is the final intended license for all course content.
