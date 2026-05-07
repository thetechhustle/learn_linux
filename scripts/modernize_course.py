#!/usr/bin/env python3
"""Normalize and enrich the Learn Linux Markdown course.

The original repository is a Markdown draft. This script keeps the useful base
content, removes empty duplicate files, modernizes common Linux command examples,
and adds a consistent course scaffold to each lesson.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "docs" / "lessons"

CHAPTER_CONTEXT = {
    "01_where_to_start": ("a first-week junior admin onboarding into a small cloud team", "Identify the OS, distribution, support window, and package source before changing anything."),
    "02_booting_and_system_management_daemons": ("a production VM that fails to boot after a kernel update", "Trace the boot chain from firmware to systemd before changing bootloader settings."),
    "03_access_control_and_rootly_powers": ("a shared server where a contractor needs temporary access", "Grant the smallest useful permission, then verify it from the user's point of view."),
    "04_process_control": ("an API server where latency spikes because one process is consuming CPU", "Collect process evidence before killing or renicing anything."),
    "05_the_filesystem": ("a web application running out of disk space during a deployment", "Separate path, mount, inode, permission, and capacity problems."),
    "06_software_installation_and_management": ("a fleet that must install security updates without breaking a release", "Know where software came from and how to roll it back."),
    "07_scripting_and_the_shell": ("a repetitive operations checklist that needs to become a safe script", "Prefer small, observable scripts with clear inputs, outputs, and failure behavior."),
    "08_user_management": ("a departing teammate whose access must be removed without losing evidence", "Treat accounts as lifecycle objects: create, audit, disable, archive, and remove deliberately."),
    "09_cloud_computing": ("a startup moving one Linux workload from a laptop to a cloud VM", "Match the hosting model to operational responsibility and cost exposure."),
    "10_logging": ("an outage where logs are the only reliable timeline", "Use logs to answer who, what, when, where, and how often."),
    "11_drivers_and_the_kernel": ("a server that loses network connectivity after a kernel change", "Connect hardware symptoms to drivers, modules, kernel versions, and boot choices."),
    "12_printing": ("an office printer that fails only for Linux users", "Debug printing as a queue, driver, permission, and network problem."),
    "13_tcp_ip_networking": ("a container host that can reach the internet but not an internal service", "Diagnose from interface to route to DNS to firewall before guessing."),
    "14_physical_networking": ("a new office rack where cabling mistakes look like software failures", "Respect the physical layer: labels, ports, power, cabling, and test evidence matter."),
    "15_ip_routing": ("two subnets that need reliable traffic flow across a router", "Read routing tables as policy, not mystery."),
    "16_dns_the_domain_name_system": ("a domain migration where email and web traffic must keep working", "Plan DNS changes around TTLs, authoritative servers, and rollback."),
    "17_single_sign-on": ("a company replacing local Linux passwords with centralized identity", "Authentication, authorization, and account data are related but different systems."),
    "18_electronic_mail": ("a self-hosted app that must send reliable transactional email", "Email reliability depends on DNS, reputation, transport, filtering, and monitoring."),
    "19_web_hosting": ("a website launch that needs TLS, reverse proxying, and clear rollback", "Separate the web server, application runtime, proxy, certificate, and deployment concerns."),
    "20_storage": ("a database server that needs more capacity without losing data", "Backups, partitioning, filesystems, volume management, and monitoring are one system."),
    "21_the_network_file_system": ("a team sharing build artifacts between Linux machines", "Network filesystems fail across identity, permissions, mount options, and latency boundaries."),
    "22_smb": ("a mixed Windows, macOS, and Linux office sharing project files", "Make protocol, identity, permissions, and security expectations explicit."),
    "23_configuration_management": ("a growing fleet where manual server setup is no longer reliable", "Configuration management is about repeatability, drift control, and reviewable change."),
    "24_virtualization": ("a lab where learners need disposable Linux systems", "Use virtualization to create safe failure, repeatable labs, and clean snapshots."),
    "25_containers": ("a service moving from a snowflake server into a repeatable runtime", "Containers package processes; they do not remove the need to understand Linux."),
    "26_continuous_integration_and_delivery": ("a team that wants every Linux change tested before it reaches production", "CI/CD is a feedback system: build, test, package, deploy, observe, and recover."),
    "27_security": ("a Linux host exposed to the internet for the first time", "Security starts with inventory, updates, identity, least privilege, logging, and backups."),
    "28_monitoring": ("an on-call rotation that needs fewer surprises and faster diagnosis", "Monitor symptoms users feel and signals operators can act on."),
    "29_performance_analysis": ("a server that became slow after traffic doubled", "Performance work starts with measurement and ends with a verified change."),
    "30_data_center_basics": ("a small office server closet growing into real infrastructure", "Power, cooling, physical security, and labeling are reliability features."),
    "31_methodology_policy_and_politics": ("an operations team trying to become predictable without becoming bureaucratic", "Policies are useful when they make good work easier and risky work harder."),
}

COMMAND_UPDATES = [
    (r"\bifconfig\b", "ip address"),
    (r"\bnetstat -rn\b", "ip route"),
    (r"\bnetstat -tuln\b", "ss -tuln"),
    (r"\bnetstat -a\b", "ss -a"),
    (r"\bnetstat\b", "ss"),
    (r"\bsudo service ([a-zA-Z0-9_.-]+) restart\b", r"sudo systemctl restart \1"),
    (r"\bsudo service ([a-zA-Z0-9_.-]+) start\b", r"sudo systemctl start \1"),
    (r"\bservice ([a-zA-Z0-9_.-]+) restart\b", r"sudo systemctl restart \1"),
    (r"\bsudo apt-get update && sudo apt-get upgrade\b", "sudo apt update && sudo apt upgrade"),
    (r"\bsudo apt-get install\b", "sudo apt install"),
    (r"\bsudo apt-get update\b", "sudo apt update"),
    (r"\bsudo apt-get upgrade\b", "sudo apt upgrade"),
    (r"\bsudo apt-get remove\b", "sudo apt remove"),
    (r"\bsudo apt-get purge\b", "sudo apt purge"),
    (r"\bapt-get install\b", "apt install"),
    (r"\bCentOS 7\b", "Rocky Linux 9 or AlmaLinux 9"),
    (r"\bsudo yum update -y\b", "sudo dnf update -y"),
    (r"\bsudo yum install\b", "sudo dnf install"),
    (r"\bQuagga\b", "FRRouting"),
    (r"\bquagga\b", "frr"),
]

NOISE = [r"^Sure, let's dive straight into the content!\n\n"]


def title_from_file(path: Path, text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip().strip("`")
        if stripped.startswith("**") and stripped.endswith("**"):
            return stripped.strip("*").strip()
    return path.stem.replace("_", " ").replace("-", ": ").title()


def section_number(path: Path) -> str:
    match = re.match(r"(\d+)\.(\d+)", path.stem)
    if match:
        return f"{int(match.group(1))}.{int(match.group(2))}"
    match = re.match(r"(\d+)", path.parent.name)
    return str(int(match.group(1))) if match else ""


def normalize_heading(text: str, title: str) -> str:
    stripped = text.lstrip()
    if stripped.startswith("#"):
        return text
    return f"# {title}\n\n{text}"


def modernize_commands(text: str) -> str:
    for pattern, replacement in COMMAND_UPDATES:
        text = re.sub(pattern, replacement, text)
    if "iptables" in text and "nftables" not in text:
        text += (
            "\n\n!!! note \"Modern firewall note\"\n"
            "    Many existing Linux estates still use `iptables`, but new designs should also evaluate `nftables` "
            "or a distribution front end such as `firewalld`/`ufw`. Treat older commands as legacy literacy, not the only modern path.\n"
        )
    if "ip address" in text and "Older tutorials often use `ifconfig`" not in text:
        text += (
            "\n\n!!! tip \"Modern networking command\"\n"
            "    Older tutorials often use `ifconfig`. This course favors `ip address`, `ip link`, `ip route`, and `ss` because they are available by default on modern Linux distributions.\n"
        )
    return text


def strip_noise(text: str) -> str:
    for pattern in NOISE:
        text = re.sub(pattern, "", text)
    text = text.replace("Linux warrior", "Linux operator")
    text = text.replace("paladin", "operator")
    return text


def enrichment_block(path: Path, title: str) -> str:
    context, principle = CHAPTER_CONTEXT.get(path.parent.name, ("a real production Linux system", "Make the smallest observable change and verify the result."))
    sec = section_number(path)
    return f"""

!!! abstract "What you will learn"
    - Explain where **{title}** fits in day-to-day Linux operations.
    - Use current Linux tooling to inspect, change, and verify the relevant system behavior.
    - Connect the concept to a real operational scenario: {context}.

!!! example "Field story"
    Imagine {context}. Your job is not to memorize a command; it is to build a short evidence trail, choose a low-risk change, and prove whether the system improved.

!!! success "Operator principle"
    {principle}

## Hands-on practice

Run these on a disposable VM, container, or lab machine unless the lesson explicitly says otherwise.

1. Inspect the current state with a read-only command related to this topic.
2. Save the command and output in a short lab note.
3. Make one reversible change or simulate the change in a sandbox.
4. Re-run the inspection and explain what changed.

## Check your understanding

- What evidence would tell you that this system is healthy?
- What is the riskiest command in this lesson, and how would you make it safer?
- How would you explain section {sec} to a teammate during an incident handoff?
""".rstrip() + "\n"


def has_enrichment(text: str) -> bool:
    return "What you will learn" in text and "Hands-on practice" in text


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return False
    original = text
    text = strip_noise(text)
    title = title_from_file(path, text)
    text = normalize_heading(text, title)
    text = modernize_commands(text)
    if path.name != "README.md" and not has_enrichment(text):
        lines = text.splitlines()
        insert_at = 1
        while insert_at < len(lines) and not lines[insert_at].strip():
            insert_at += 1
        lines.insert(insert_at, enrichment_block(path, title))
        text = "\n".join(lines).rstrip() + "\n"
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def remove_empty_duplicates() -> list[Path]:
    removed = []
    for path in LESSONS.rglob("*.md"):
        if path.stat().st_size == 0:
            path.unlink()
            removed.append(path)
    return removed


def write_lesson_index() -> None:
    rows = []
    for chapter in sorted(p for p in LESSONS.iterdir() if p.is_dir()):
        readme = chapter / "README.md"
        if not readme.exists():
            continue
        title = title_from_file(readme, readme.read_text(encoding="utf-8"))
        rel = "../" + readme.relative_to(ROOT / "docs").as_posix()
        count = len([p for p in chapter.glob("*.md") if p.name != "README.md"])
        rows.append(f"| [{title}]({rel}) | {count} lessons |")

    index = """# Course Syllabus

This course is organized as a practical Linux operator path. Start with the foundations, then move into services, networking, automation, security, monitoring, and operations leadership.

| Chapter | Lessons |
| --- | ---: |
""" + "\n".join(rows) + "\n"
    (ROOT / "docs" / "course" / "syllabus.md").write_text(index, encoding="utf-8")


def main() -> None:
    removed = remove_empty_duplicates()
    changed = []
    for path in sorted(LESSONS.rglob("*.md")):
        if process_file(path):
            changed.append(path)
    write_lesson_index()
    print(f"Removed empty duplicate files: {len(removed)}")
    print(f"Modernized Markdown files: {len(changed)}")


if __name__ == "__main__":
    main()
