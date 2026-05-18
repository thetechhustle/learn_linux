# Chapter 27: Security

## Why security belongs in daily operations

Security is not a separate job that happens after Linux systems are built. It is part of how accounts are created, software is installed, services are exposed, logs are reviewed, backups are tested, and incidents are handled.

This chapter introduces the operating habits that make Linux systems harder to abuse and easier to recover. The goal is not to memorize every security tool. The goal is to understand the layers of control around a system and to know which evidence proves those controls are working.

## The operating model

A practical security program starts with a few questions:

- Who can log in?
- What can they do after logging in?
- Which services are listening on the network?
- Which data needs protection?
- Which software is installed and patched?
- Which secrets exist, and where are they stored?
- Which logs would show misuse or failure?
- What is the recovery path if the host is compromised?

Linux gives you many controls for these questions: file permissions, accounts, groups, `sudo`, PAM, SSH, firewalls, cryptography, package updates, logs, backups, and network segmentation. Each control matters more when it is tied to a clear threat and a verification step.

## Defense in layers

Do not depend on one perfect control. Real systems need layers:

- **Identity:** accounts, groups, passwords, keys, MFA, and directory services.
- **Authorization:** file permissions, `sudo`, service privileges, and application roles.
- **Network exposure:** listening ports, firewalls, VPNs, and service binding choices.
- **Data protection:** encryption, backups, retention, and access logs.
- **System integrity:** package sources, patching, configuration management, and baseline checks.
- **Detection:** logs, alerts, audit events, and anomaly investigation.
- **Response:** isolation, credential rotation, restoration, forensics, and communication.

The strongest security work is usually boring and repeatable: remove unused access, patch known flaws, avoid unnecessary public services, protect credentials, monitor logs, and test recovery.

## Risk before tools

Security tools are useful only when they answer a real operational question.

For example:

- `ss -ltnp` answers what is listening.
- `sudo -l` answers what a user can run with elevated privileges.
- `last` and `journalctl` help inspect login and service activity.
- `find` can locate dangerous permissions such as unexpected setuid files.
- `nmap` can compare expected exposure with actual network exposure.
- `fail2ban`, firewalls, and rate limits can reduce common brute-force pressure.

Before reaching for a tool, name the risk. After using a tool, keep the evidence.

## What this chapter covers

The lessons move from security concepts into practical Linux controls:

- elements of security and common compromise paths
- basic hardening habits
- password and account management
- security investigation tools
- cryptography fundamentals
- SSH operations
- firewalls
- VPNs
- standards and certification context
- sources of security information
- incident response after a site is attacked
- recommended reading for continued practice

The through-line is operational judgment. A secure Linux operator does not just turn on a firewall or copy an SSH hardening snippet. They understand what changed, what broke, what evidence proves the intended state, and how to recover.

## Hands-on mindset

Use disposable VMs or lab hosts for practice. Security commands can lock you out, interrupt services, or hide important evidence if used carelessly.

For each lesson, build a small note with:

1. the risk being studied
2. the command or configuration inspected
3. the before state
4. the intended change
5. the after state
6. the rollback or recovery step

Security confidence comes from practiced verification, not from optimistic configuration.

## Check your understanding

- Which accounts can become root on your Linux host?
- Which services are reachable from the network?
- Which secrets would need rotation after a compromise?
- Which logs would show a failed login, a successful privileged command, or a crashed service?
- What is your first isolation step if a host is suspected to be compromised?

<!-- lesson-index:start -->

## Lessons in this chapter

- [27.1 Elements of Security 🛡️](27.1_elements_of_security.md)
- [Understanding the Breach: How Security is Compromised 👾](27.2_how_security_is_compromised.md)
- [27.3 Basic Security Measures 🛡️](27.3_basic_security_measures.md)
- [Understanding Passwords and User Accounts 💡](27.4_passwords_and_user_accounts.md)
- [27.5: Security Power Tools 💥](27.5_security_power_tools.md)
- [A mystical primer on Cryptography ⚗️](27.6_cryptography_primer.md)
- [An Overview to SSH: The Humble Gatekeeper 🗝️](27.7_ssh,_the_secure_shell.md)
- [27.8_Firewalls: The Ramparts of Digital Defense 🛡️](27.8_firewalls.md)
- [27.9 Virtual Private Networks (VPNs) 🚀](27.9_virtual_private_networks_vpns.md)
- [27.10 Certifications and Standards: Setting The Bar of Excellence 📊](27.10_certifications_and_standards.md)
- [Gaining Knowledge to Fortify Your Fortress: Sources of Security Information](27.11_sources_of_security_information.md)
- [27.12 When Your Site Has Been Attacked: A Guide to Recovery and Resilience](27.12_when_your_site_has_been_attacked.md)
- [Recommended Reading 📚](27.13_recommended_reading.md)

<!-- lesson-index:end -->
