# Learn Linux

<div class="course-hero" markdown>

<div markdown>
<span class="course-badge">Practical Linux course</span>

# Learn Linux by operating real systems

Build the habits behind modern Linux work: inspect first, change carefully, verify with evidence, document what happened, and automate the repeatable parts.

[Start the course](course/overview.md){ .md-button .md-button--primary }
[Set up the lab](course/lab-setup.md){ .md-button }

</div>

![The Linux operator learning loop](assets/images/operator-loop.svg)

</div>

## What this course is

This is a hands-on Linux operations course for future system administrators, cloud engineers, DevOps engineers, SREs, support engineers, and builders who want practical command-line confidence.

<div class="course-grid" markdown>

<div class="course-card" markdown>
### Learn by doing
Every lesson includes a field story, operator principle, hands-on practice, and review questions.
</div>

<div class="course-card" markdown>
### Modern tooling
The course favors current Linux commands such as `ip`, `ss`, `systemctl`, `journalctl`, `dnf`, `apt`, and modern firewall guidance.
</div>

<div class="course-card" markdown>
### Real-world path
The syllabus moves from fundamentals to networking, storage, identity, automation, security, monitoring, and operations practice.
</div>

</div>

## Course outcomes

By the end, you should be able to:

- Navigate a Linux system and explain what you are seeing.
- Manage packages, users, permissions, processes, services, logs, storage, and networking.
- Debug common operational failures with a repeatable evidence trail.
- Build safe labs with VMs or containers before touching production systems.
- Document findings clearly enough for a teammate to continue the work.

## Where to begin

Not sure where to jump in? Pick the description that fits you best.

<div class="course-grid" markdown>

<div class="course-card" markdown>
### Absolute beginner
No Linux experience yet. Start at Chapter 1 and work forward. Every concept is introduced before it is used.

[Start at Chapter 1](lessons/01_where_to_start/README.md){ .md-button }
</div>

<div class="course-card" markdown>
### Help desk / support tech
You know the basics. Jump to Chapter 4 (processes), Chapter 8 (users), or Chapter 10 (logging) for day-to-day operational skills.

[Jump to Chapter 4](lessons/04_process_control/README.md){ .md-button }
</div>

<div class="course-card" markdown>
### Software engineer
You write code but want production confidence. Focus on Chapters 9–13 (cloud, kernel, networking) then Chapters 23–26 (config management, containers, CI/CD).

[Jump to Chapter 9](lessons/09_cloud_computing/README.md){ .md-button }
</div>

<div class="course-card" markdown>
### Cloud / DevOps / SRE learner
You already use Linux but want depth. Head straight to the Operations track: Chapters 20–29 cover storage, security, monitoring, and performance.

[Jump to Chapter 20](lessons/20_storage/README.md){ .md-button }
</div>

</div>

## Learning rhythm

1. Read the concept.
2. Run the guided practice in a disposable lab.
3. Capture command output and explain it in your own words.
4. Complete the checkpoint questions.
5. Revisit the field story and decide what you would do first during a real incident.

!!! tip "New to Linux?"
    Start with the [Glossary](course/glossary.md) to get familiar with common terms, then read [Lab Setup](course/lab-setup.md) before running any commands.

!!! warning "Use a lab"
    Many Linux commands can change system state. Run exercises in a VM, container, cloud sandbox, or spare machine unless you are certain the command is read-only.
