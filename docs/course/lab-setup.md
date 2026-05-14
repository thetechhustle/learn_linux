# Lab Setup

Use a disposable environment. The best Linux learning happens when mistakes are safe.

## Lab goals

Your lab should let you:

- Break boot, network, storage, user, and service settings without risking real work.
- Compare at least two Linux families when a lesson mentions distribution differences.
- Capture command output, screenshots, or terminal logs as evidence.
- Revert quickly when an experiment goes wrong.
- Tear down cloud resources before they become surprise costs.

## Recommended lab options

=== "Local VM"

    Use VirtualBox, VMware Fusion, UTM, Hyper-V, or libvirt to run Ubuntu Server LTS plus a second distribution such as Rocky Linux or Debian.

    Good for boot, storage, networking, users, services, and systemd labs.

    Recommended baseline:

    - 2 virtual CPUs.
    - 2-4 GiB RAM.
    - 25 GiB disk.
    - NAT networking for ordinary labs.
    - A snapshot named `clean-install` before making risky changes.

=== "Cloud VM"

    Use a small cloud instance when you need internet-reachable DNS, TLS, web hosting, SSH, firewall, or monitoring practice.

    Delete unused instances so cost does not drift.

    Recommended baseline:

    - Smallest practical VM size.
    - SSH key authentication.
    - Security group or firewall that allows only the ports needed for the lab.
    - A project tag such as `learn-linux-lab`.
    - A reminder to stop or delete the VM after the session.

=== "Container"

    Use containers for quick shell, package, scripting, and process labs.

    Containers are not full Linux machines; they share the host kernel and are not a substitute for boot, kernel, or storage labs.

    Recommended baseline:

    - Use disposable containers for command practice.
    - Avoid privileged containers unless a lesson explicitly requires them.
    - Keep host bind mounts read-only unless you need to test writes.
    - Do not treat container results as proof for boot, kernel, filesystem, or systemd behavior.

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

## Preflight checks

Run these commands at the start of a lab and record the output in your notes:

```bash
hostnamectl
uname -a
id
ip address
ip route
df -h
systemctl --failed
```

If you are about to change storage, boot, firewall, identity, or remote access settings, also capture the current configuration:

```bash
sudo lsblk -f
sudo ss -tulpn
sudo systemctl status ssh || sudo systemctl status sshd
sudo journalctl -n 50 --no-pager
```

## Safety checklist

- Know whether you are in a lab, personal machine, or production host.
- Prefer read-only commands first: `pwd`, `ls`, `id`, `uname -a`, `ip address`, `ip route`, `systemctl status`, `journalctl -n 50`.
- Snapshot VMs before storage, bootloader, firewall, identity, and service-management labs.
- Keep a lab notebook with command, output, interpretation, and next action.
- Keep a second login session open before changing SSH, firewall, sudo, or network settings.
- Confirm rollback before changing anything that could disconnect you.

## Snapshot and rollback habit

Use a simple naming pattern so you can tell what each restore point means:

```text
clean-install
before-firewall-lab
before-storage-lab
before-ssh-hardening
after-working-web-service
```

After a risky lab, test one rollback while the stakes are low. A snapshot is only useful if you know how to restore it.

## Cleanup checklist

- Stop or delete cloud VMs, load balancers, volumes, DNS records, and snapshots you no longer need.
- Remove temporary SSH keys from cloud consoles and local agents.
- Destroy throwaway containers and images created only for a lab.
- Keep only the notes and evidence needed to explain what you learned.

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
