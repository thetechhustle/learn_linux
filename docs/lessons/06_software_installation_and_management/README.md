# Chapter 06: Software Installation and Management

Software management is one of the highest-leverage responsibilities on a Linux
system. It determines what code runs, where it came from, how it is updated,
how quickly security fixes land, and how reliably a machine can be rebuilt.

This chapter treats installation and package management as operational work,
not just a sequence of commands. You will learn how to install an operating
system safely, use package managers with evidence, understand package-system
differences, manage higher-level tooling, recognize FreeBSD's software model,
and handle localization and configuration without losing track of what changed.

## What You Should Be Able to Do

By the end of this chapter, you should be able to:

- Plan an operating system installation without wiping the wrong disk or
  leaving the system unreachable.
- Identify which package manager family a system uses and where its package
  metadata lives.
- Inspect installed packages, available updates, repositories, and package
  ownership for files on disk.
- Separate vendor packages, distribution packages, local packages, language
  packages, and manually installed software.
- Apply updates in a way that respects change windows, reboot requirements,
  rollback paths, and service impact.
- Explain the difference between Linux package management and FreeBSD ports
  and packages.
- Record software changes clearly enough that another operator can reproduce
  or reverse them.

## Operator Scenario

Imagine a production host is missing a command needed by a deployment script.
A risky response is to search the web, paste an install command, and hope it
works. A stronger response is to identify the system, inspect trusted package
sources, install the smallest required package, and verify the result.

```bash
cat /etc/os-release
command -v apt dnf yum zypper pacman pkg
apt-cache policy curl 2>/dev/null || true
dnf info curl 2>/dev/null || true
dpkg -S /usr/bin/curl 2>/dev/null || true
rpm -qf /usr/bin/curl 2>/dev/null || true
```

Those commands help answer the important questions:

- What operating system and release am I changing?
- Which package manager owns this system?
- Which repository would provide the software?
- Is the command already installed under a different path?
- If I install or upgrade something, how can I prove what changed?

That is the habit this chapter builds: treat software changes as traceable
system changes.

## Change Discipline

Package operations can restart services, replace libraries, update kernels,
change configuration defaults, and introduce new dependencies. Before making a
non-lab change, capture the current state:

```bash
date -Is
hostnamectl
systemctl --failed 2>/dev/null || true
apt list --upgradable 2>/dev/null || true
dnf check-update 2>/dev/null || true
```

Then make the change through the distribution's supported tools whenever
possible. Prefer a documented repository or package over an unmanaged binary in
`/usr/local/bin`. If you must install software manually, record where it came
from, where it was placed, how it is updated, and how to remove it.

## Study Path

Start with operating system installation because it establishes the base for
every later package decision. Then study package-management concepts before
diving into specific Linux tools. Use the high-level package-tool lesson to
compare day-to-day workflows, then use the FreeBSD lesson to understand a
different but related model. Finish with localization and configuration because
software is not truly installed until it is configured for the system's users,
locale, and service requirements.

For each lesson, keep a short change note:

1. What system did you inspect?
2. What package or configuration did you change?
3. Which command proves the result?
4. What is the rollback or cleanup path?

## Safety Notes

Run practice installs and upgrades on disposable VMs, containers, or lab
machines. Be especially careful with commands that remove packages recursively,
replace repositories, run remote shell installers, or upgrade core system
components during business hours. If a package operation mentions a kernel,
boot loader, libc, OpenSSL, database server, or SSH service, slow down and plan
the rollback path before accepting.

<!-- lesson-index:start -->

## Lessons in this chapter

- [06.1 Operating System Installation](06.1_operating_system_installation.md)
- [06.2 Managing Packages](06.2_managing_packages.md)
- [06.3 Linux Package Management Systems](06.3_linux_package_management_systems.md)
- [06.4 High-level Linux Package Management Systems](06.4_high-level_linux_package_management_systems.md)
- [06.5 FreeBSD Software Management](06.5_freebsd_software_management.md)
- [06.6 Software Localization and Configuration](06.6_software_localization_and_configuration.md)
- [06.7 Recommended Reading](06.7_recommended_reading.md)

<!-- lesson-index:end -->
