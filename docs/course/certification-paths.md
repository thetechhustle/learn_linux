# Certification Paths

This course teaches Linux operations in a distro-agnostic way: the goal is a
durable operator model that works on Red Hat, Debian, Ubuntu, SUSE, and their
derivatives. That approach maps well onto the major Linux certifications, which
test the same underlying skills — user and permission management, storage,
networking, services, logging, security, and automation — even when they use one
distribution's exact tooling on the exam.

The tables below map this course's chapters to the objective areas of common
certifications. They are a study aid, not a replacement for each vendor's
official objective list. Certification objectives and exam versions change over
time, so always confirm the current objectives on the vendor's site before you
schedule an exam.

!!! note "How to read these maps"
    A chapter reference means the course covers the topic area an objective
    lives in, not that the chapter reproduces the exam word for word. Where an
    exam is tied to one distribution (RHCSA and RHCE are RHEL-specific), practice
    the RHEL tooling — `dnf`, `nmcli`, `firewalld`, `systemd`, `podman`,
    `stratis`, `chrony`, `tuned` — on a RHEL 9 or compatible system such as
    AlmaLinux 9 or Rocky Linux 9.

## Red Hat Certified System Administrator (RHCSA, EX200, RHEL 9)

RHCSA is a hands-on, task-based exam performed on live RHEL 9 systems. You are
graded on the state of the system after your work, so practice until the tasks
are muscle memory. The following chapters cover the RHCSA objective areas.

| RHCSA objective area | Course chapters |
| --- | --- |
| Manage users and groups, set password aging | Ch08 (User Management) |
| Manage file permissions, ACLs, and SELinux contexts and modes | Ch03 (Access Control and Rootly Powers), Ch05 (The Filesystem), Ch27 (Security) |
| Configure local storage: partitions, LVM, and Stratis | Ch20 (Storage) |
| Manage systemd services, boot targets, rescue mode, and reset the root password | Ch02 (Booting and System Management Daemons) |
| Schedule tasks with `cron`, `at`, and systemd timers | Ch04 (Process Control) |
| Install and manage software with `dnf`, modules, and repositories | Ch06 (Software Installation and Management) |
| Configure networking with `nmcli` and host firewall with `firewalld` | Ch13 (TCP/IP Networking), Ch14 (Physical Networking), Ch27 (Security) |
| Find, run, and manage containers with `podman`, including as systemd services | Ch25 (Containers) |
| Review system journals and logs with `journalctl`, configure time with `chrony` | Ch10 (Logging) |
| Tune system performance profiles with `tuned` | Ch29 (Performance Analysis) |

!!! tip "RHCSA practice discipline"
    Two skills decide RHCSA outcomes more than any single command: recovering a
    system you cannot log in to (boot to `rescue`/`emergency`, break into the
    root shell, reset the root password, and — on RHEL — relabel SELinux) and
    making changes persist across reboot. Reboot your practice VM after every
    task and confirm the change survived.

## Red Hat Certified Engineer (RHCE, EX294, RHEL 9)

On RHEL 9 the RHCE exam (EX294) is entirely about automation with Ansible. You
write and run playbooks that configure managed RHEL hosts: managing inventories,
variables, facts, templates, roles, handlers, and using Ansible modules to
perform the same administration tasks RHCSA tests by hand.

| RHCE (EX294) objective area | Course chapters |
| --- | --- |
| Install and configure an Ansible control node, inventories, and configuration | Ch23 (Configuration Management) |
| Write playbooks, use variables, facts, loops, conditionals, and handlers | Ch23 (Configuration Management), Ch07 (Scripting and the Shell) |
| Use templates (Jinja2), roles, and Ansible Galaxy content | Ch23 (Configuration Management) |
| Automate RHCSA-level tasks (users, storage, services, software) with modules | Ch23 (Configuration Management) plus the RHCSA chapters above |

!!! note "Honest scope for RHCE"
    This course introduces Ansible and configuration management in Chapter 23,
    and Chapter 07 builds the shell and scripting fundamentals that automation
    rests on. That is enough to understand the model and start writing
    playbooks, but it is an introduction rather than full EX294 exam depth. To
    prepare for RHCE, work through Chapter 23, then study the official Red Hat
    course material (RH294) and the upstream Ansible documentation, and practice
    writing idempotent playbooks and roles against RHEL 9 managed nodes until the
    workflow is automatic.

## CompTIA Linux+ and LPIC-1 (high level)

CompTIA Linux+ (XK0-005) and LPIC-1 are distribution-neutral, which lines up
well with how this course teaches. They cover a broad base of everyday Linux
administration rather than one vendor's tooling, so most of the early and middle
chapters apply.

!!! note "Linux+ (XK0-005) at a glance"
    Linux+ spans system management, shells and scripting, security, and
    troubleshooting. Chapters 02-08 cover boot and services, access control, the
    filesystem, software management, scripting, and users. Chapters 13-15 cover
    networking and routing. Chapters 20-22 cover storage and shared filesystems.
    Chapters 23-27 add automation, virtualization, containers, and security, and
    Chapters 28-31 cover monitoring, performance, and operations practice.

!!! note "LPIC-1 at a glance"
    LPIC-1 (exams 101 and 102) covers system architecture and boot, package
    management, the GNU and Unix commands, filesystems and the FHS, shells and
    scripting, networking fundamentals, and basic security. Chapters 01-08 build
    the command-line, filesystem, software, and user foundations; Chapters 10-13
    add logging, the kernel, and networking basics; Chapter 27 covers the
    security fundamentals LPIC-1 expects.

## How to use this course for exam prep

!!! tip "Turn the operator loop into exam habits"
    Every lesson reinforces the same five-step loop:
    **Inspect → Change → Verify → Document → Automate.** Hands-on exams reward
    exactly this discipline. Inspect the current state before you touch anything,
    make the smallest change that satisfies the task, verify it with real command
    output, and — for hands-on exams — reboot and confirm the change persisted.
    On RHCE, the final step of the loop becomes the whole exam: encode the change
    as an idempotent Ansible playbook.

Work certification prep like this:

1. Pick a target exam and read its current official objectives.
2. For each objective area, do the mapped chapter's labs in a disposable VM or
   container until the task is quick and reliable.
3. Practice on the exam's distribution when the exam is vendor-specific (RHEL 9
   or a compatible rebuild for RHCSA and RHCE).
4. Use the [Capstone](capstone.md) as a full-scope rehearsal: it exercises the
   operator loop end to end across many chapters, which is close to how a
   hands-on exam feels — a sequence of realistic tasks under time pressure with
   evidence that your changes actually worked.

!!! note "The certification is a checkpoint, not the goal"
    The lasting outcome of this course is the operator's judgment: knowing what
    to inspect, changing one thing at a time, proving the result, and handing off
    clean notes. A certification confirms that skill on a given day. Keep
    practicing the loop after the exam and the credential stays true.
