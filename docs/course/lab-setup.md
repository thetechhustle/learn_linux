# Lab Setup

Use a disposable environment. The best Linux learning happens when mistakes are safe.

## Recommended lab options

=== "Local VM"

    Use VirtualBox, VMware Fusion, UTM, Hyper-V, or libvirt to run Ubuntu Server LTS plus a second distribution such as Rocky Linux or Debian.

    Good for boot, storage, networking, users, services, and systemd labs.

=== "Cloud VM"

    Use a small cloud instance when you need internet-reachable DNS, TLS, web hosting, SSH, firewall, or monitoring practice.

    Delete unused instances so cost does not drift.

=== "Container"

    Use containers for quick shell, package, scripting, and process labs.

    Containers are not full Linux machines; they share the host kernel and are not a substitute for boot, kernel, or storage labs.

## Baseline tools

On Debian or Ubuntu labs:

```bash
sudo apt update
sudo apt install curl git jq ripgrep shellcheck tmux vim
```

On Rocky Linux or AlmaLinux labs:

```bash
sudo dnf update -y
sudo dnf install curl git jq ripgrep ShellCheck tmux vim-enhanced
```

## Safety checklist

- Know whether you are in a lab, personal machine, or production host.
- Prefer read-only commands first: `pwd`, `ls`, `id`, `uname -a`, `ip address`, `ip route`, `systemctl status`, `journalctl -n 50`.
- Snapshot VMs before storage, bootloader, firewall, identity, and service-management labs.
- Keep a lab notebook with command, output, interpretation, and next action.

## Lab note template

```text
Date:
Host:
Goal:
Command run:
Observed output:
Interpretation:
Change made:
Verification:
Rollback plan:
```
