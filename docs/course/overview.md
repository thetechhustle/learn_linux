# Course Overview

Learn Linux is structured as a full operator path, not a command glossary. The goal is to help you build judgment around real systems — not just memorize commands, but understand *why* those commands matter and *what to check next* when something goes wrong.

Use the course to practice the same loop you will use on production work:

1. Inspect the current state before changing anything.
2. Make the smallest safe change in a lab.
3. Verify the result with command output, logs, or service behavior.
4. Write down what changed and what evidence supports it.
5. Repeat the work until the process is boring and reversible.

## Audience

This course is for:

- New Linux learners who want a practical, structured path from zero.
- Help desk and support technicians moving toward infrastructure work.
- Software engineers who need stronger production literacy.
- Cloud, DevOps, SRE, and cybersecurity learners who need solid Linux foundations.

If you can open a terminal and type, you have enough background to start.

## Prerequisites

You should be comfortable using a keyboard, browser, and terminal window. No prior Linux administration experience is assumed. If you encounter an unfamiliar term, check the [Glossary](glossary.md) first.

## Time expectations

| Goal | Estimated pace |
| --- | --- |
| One lesson | 20–40 minutes |
| One chapter | 2–5 hours |
| Full course (all 31 chapters) | 80–120 hours |
| Capstone project | 4–8 hours additional |

These are loose estimates. Move faster through topics you already know; slow down and repeat labs for topics that feel unfamiliar.

You will get more from the lessons if you keep a disposable lab nearby. See [Lab Setup](lab-setup.md) before running commands that install packages, edit service files, change accounts, touch storage, or alter networking.

## Course tracks

| Track | Chapters | Focus |
| --- | --- | --- |
| Foundations | 1-8 | Distributions, shell, filesystems, processes, packages, users, permissions |
| Services and infrastructure | 9-19 | Cloud, logs, kernel, printing, networking, routing, DNS, identity, mail, web |
| Operations depth | 20-29 | Storage, shared filesystems, configuration management, virtualization, containers, CI/CD, security, monitoring, performance |
| Professional practice | 30-31 | Data center basics, policy, methodology, documentation, service management |

For the complete chapter sequence, use the [Syllabus](syllabus.md). For repeated terms, use the [Glossary](glossary.md) as a quick reference while you work through lessons.

## Lesson pattern

Each lesson should answer five questions:

1. What is this concept?
2. Why does it matter in real operations?
3. What commands or files help you inspect it?
4. What safe practice can you run in a lab?
5. How would you explain the result to a teammate?

When a lesson includes commands, prefer read-only inspection first. Commands such as `ip addr`, `ss -tulpen`, `systemctl status`, `journalctl -u`, `df -h`, `lsblk`, and `findmnt` are usually safer starting points than commands that restart services, rewrite files, or delete data.

## The operator loop

Every lesson reinforces a five-step habit that professional Linux operators use on real systems:

```
Inspect → Change → Verify → Document → Automate
```

1. **Inspect** — Read the current state before touching anything. What does the system say right now?
2. **Change** — Make one targeted change. Prefer the smallest possible intervention.
3. **Verify** — Confirm the change had the intended effect with evidence (command output, logs, metrics).
4. **Document** — Write down what you did, what you saw, and what it means — clearly enough for a teammate.
5. **Automate** — Once a procedure is reliable and documented, encode it so it never needs to be done manually again.

This loop appears in every chapter. By the end of the course it should be instinct.

## How to Work Through a Chapter

For each chapter:

1. Read the chapter overview and list the operational risks it introduces.
2. Run one lesson's lab in a VM, container, cloud sandbox, or spare machine.
3. Save the commands you ran and the evidence they produced.
4. Answer the review questions without looking back at the lesson.
5. Write a short handoff note with the symptom, commands, result, and next step.

That handoff habit matters. Linux work is rarely finished when a command succeeds; it is finished when another operator can understand what happened and safely continue.

## Safety Boundaries

Treat the following topics as lab-only until you understand the rollback path:

- Disk partitioning, filesystems, RAID, LVM, ZFS, and Btrfs.
- Firewall, routing, DNS, DHCP, and identity configuration.
- User removal, password policy, sudo, PAM, and SSH hardening.
- Package upgrades, kernel changes, boot loaders, and service restarts.
- Backup, restore, incident response, and compliance evidence handling.

If you are connected to a machine you care about, pause before running commands copied from a lesson or search result. Confirm the host, user, working directory, target file, and rollback plan first.

## Assessment model

This course does not require accounts, grading, or certificates. Use the capstone to validate readiness: build a small Linux service, secure it, monitor it, break it safely, recover it, and document the evidence.

The [Capstone](capstone.md) is the final readiness check. A strong capstone submission includes:

- A short design note explaining the service and risk model.
- Baseline evidence from the host before changes.
- Build, security, monitoring, failure, recovery, and cleanup notes.
- Commands and outputs that prove the final state.
- A handoff document that another operator could follow.
