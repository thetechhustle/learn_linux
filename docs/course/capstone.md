# Capstone: Operate a Small Linux Service

The capstone turns the lessons into one realistic workflow.

## Scenario

You joined a small team that needs a Linux VM to host an internal status page. Your job is to build it, secure it, monitor it, document it, and prove it can recover from common failures.

## Requirements

- Provision a disposable Linux VM.
- Create a non-root admin user with SSH access.
- Install and run a web server.
- Serve a static status page.
- Configure a firewall so only SSH and HTTP/HTTPS are reachable.
- Capture logs for the web service and SSH.
- Add a basic monitoring check.
- Simulate one failure and recover from it.
- Write an operator handoff.

## Evidence to submit

- System inventory: OS, kernel, IP address, package sources.
- Commands used and their important outputs.
- Service status before and after failure.
- Firewall rules.
- Log excerpts that prove the service worked.
- Handoff note with rollback and next maintenance step.

## Review rubric

| Area | Good evidence |
| --- | --- |
| Safety | Used a lab, snapshots, and reversible changes |
| Operations | Inspected before changing and verified after changing |
| Security | Used least privilege, firewalling, updates, and logs |
| Reliability | Demonstrated failure and recovery |
| Communication | Handoff is clear enough for another operator |
