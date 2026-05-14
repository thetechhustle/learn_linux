# Capstone: Operate a Small Linux Service

The capstone turns the lessons into one realistic workflow. Treat it like a
small production change: plan first, work in a disposable environment, capture
evidence as you go, and leave a handoff that another operator could use.

## Scenario

You joined a small team that needs a Linux VM to host an internal status page. Your job is to build it, secure it, monitor it, document it, and prove it can recover from common failures.

## Operating constraints

- Use a lab VM, cloud trial instance, or local container that you can delete.
- Do not run the capstone on a workstation, shared server, or irreplaceable VM.
- Take a snapshot before the failure drill if your platform supports snapshots.
- Keep notes in a text file as you work; do not rely on shell history alone.
- Avoid storing real secrets, customer data, or personal credentials in evidence.

## Suggested stack

Pick one path and keep it simple:

- Ubuntu Server or Debian with Nginx or Apache.
- Rocky Linux, AlmaLinux, or Fedora Server with Nginx or Apache.
- A local VM from VirtualBox, VMware, UTM, Multipass, or a short-lived cloud VM.

The exact distribution matters less than the habits: inspect before changing,
make one change at a time, verify it, and record what happened.

## Requirements

- Provision a disposable Linux system and record how it was created.
- Create a non-root admin user with SSH access and sudo rights.
- Update package metadata and install a web server.
- Serve a static status page with a hostname, owner, and last-updated note.
- Configure a firewall so only SSH and HTTP or HTTPS are reachable.
- Capture service logs and SSH authentication logs.
- Add a basic monitoring check for the web service and disk space.
- Simulate one failure, recover from it, and show before/after evidence.
- Write an operator handoff with rollback and next maintenance steps.

## Work phases

### 1. Baseline the host

Capture enough information to prove what system you started with:

```bash
hostnamectl
uname -a
ip address
ip route
df -h
systemctl --failed
```

Also record the package source evidence for your distribution:

```bash
cat /etc/os-release
apt policy 2>/dev/null || dnf repolist 2>/dev/null || yum repolist 2>/dev/null
```

### 2. Build the service

Install the web server, enable it, and verify it locally before opening the
firewall:

```bash
sudo systemctl enable --now nginx 2>/dev/null || sudo systemctl enable --now httpd
systemctl status nginx 2>/dev/null || systemctl status httpd
curl -I http://localhost/
```

Replace the default page with a small status page that includes the service
purpose, operator contact, and update timestamp. Keep the page boring and easy
to inspect.

### 3. Secure the access path

Show that access is intentional:

```bash
id
sudo -l
ss -tulpn
sudo ufw status verbose 2>/dev/null || sudo firewall-cmd --list-all 2>/dev/null
```

Only SSH and the web service should be reachable unless your lab platform
requires another management port. If you use a cloud VM, record both the Linux
firewall state and the cloud security group or firewall rule summary.

### 4. Add lightweight monitoring

Monitoring can be a simple script, cron job, systemd timer, or manual check
documented in the handoff. It should answer two questions:

- Is the web service responding?
- Is the host at risk from obvious resource pressure?

Example checks:

```bash
curl -fsS http://localhost/ >/dev/null
df -h /
systemctl is-active nginx 2>/dev/null || systemctl is-active httpd
```

### 5. Run the failure drill

Choose one reversible failure:

- Stop the web service, detect the outage, and restart it.
- Move the status page aside, detect the bad response, and restore it.
- Fill a temporary test directory enough to trigger your disk-space check, then
  clean it up.

Record the failure time, symptom, detection command, recovery command, and final
proof that the service is healthy again.

## Evidence to submit

- System inventory: OS, kernel, IP address, package sources.
- Commands used and their important outputs.
- Service status before and after failure.
- Firewall rules.
- Log excerpts that prove the service worked.
- Handoff note with rollback and next maintenance step.

## Handoff template

Use this structure for the final operator note:

```text
Service:
Host:
Owner:
Purpose:
Build summary:
Access method:
Firewall policy:
Monitoring check:
Failure tested:
Recovery steps:
Rollback plan:
Known risks:
Next maintenance:
Evidence location:
```

## Completion checks

Before you call the capstone complete, verify these are true:

- A fresh SSH session can log in with the non-root admin account.
- The web page responds locally and from the expected network path.
- The firewall state matches the intended exposure.
- Logs show the service start, access test, failure, and recovery.
- The handoff explains how to operate, recover, and safely retire the lab.

## Review rubric

| Area | Good evidence |
| --- | --- |
| Safety | Used a lab, snapshots, and reversible changes |
| Operations | Inspected before changing and verified after changing |
| Security | Used least privilege, firewalling, updates, and logs |
| Reliability | Demonstrated failure and recovery |
| Communication | Handoff is clear enough for another operator |
