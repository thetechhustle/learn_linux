# Chapter 08: User Management

User management is the operational discipline of deciding who can use a system, what identity they use, what groups and privileges they receive, and what happens when their access changes.

This chapter treats accounts as lifecycle objects:

- create the right identity
- assign the least useful set of privileges
- verify login and group behavior
- lock access quickly when risk appears
- remove or archive access without losing evidence
- centralize identity when local files no longer scale

The core Linux files and tools are simple, but mistakes can be expensive. A wrong UID can break file ownership. A stale group can preserve access after a teammate leaves. A rushed account removal can destroy evidence or service data. Good operators inspect first, change narrowly, and leave a clear handoff trail.

## What You Should Be Able To Do

By the end of this chapter, you should be able to:

- explain the relationship between usernames, UIDs, primary groups, supplementary groups, home directories, and login shells
- read account state from `/etc/passwd`, `/etc/shadow`, and `/etc/group`
- describe the FreeBSD account files that differ from Linux
- add users with a documented process instead of a guess
- choose between manual account creation and scripted account tools
- lock, disable, or remove accounts safely
- explain where PAM fits in login and authentication policy
- recognize when centralized account management is safer than local-only accounts

## Operational Model

Most user-management work follows the same pattern.

1. **Identify the account.** Confirm the username, UID, groups, home directory, login shell, and active sessions.
2. **Identify the reason.** New teammate, role change, incident response, departure, service account, lab account, or audit cleanup.
3. **Choose the safest action.** Create, modify, lock, expire, archive, remove, or escalate to centralized identity.
4. **Verify behavior.** Check files, groups, login state, and access outcomes.
5. **Record the evidence.** Keep the command, timestamp, reason, and verification result in the ticket or handoff.

This workflow matters more than memorizing one command. User-management commands can behave differently across distributions and organizations.

## Safety Rules

Before changing accounts on a real system:

- confirm whether the host uses local accounts, LDAP, Active Directory, SSO, or another identity provider
- avoid deleting home directories until retention and evidence requirements are clear
- avoid reusing UIDs unless the organization has an explicit UID policy
- treat service accounts differently from human accounts
- check active sessions before disabling a user during business hours
- prefer account lockout or expiration when immediate removal is too risky

Read-only inspection is usually safe:

```sh
id username
getent passwd username
getent group groupname
who
w
last -n 10 username
```

Changing account state usually needs elevated privileges and a clear reason.

## What To Read First

- Start with [08.1 Account Mechanics](08.1_account_mechanics.md) for usernames, UIDs, GIDs, home directories, and shells.
- Read [08.2 The `/etc/passwd` File](08.2_the_-etc-passwd_file.md) to understand the local account database.
- Read [08.3 The Linux `/etc/shadow` File](08.3_the_linux_-etc-shadow_file.md) for password hashes, aging, and lockout clues.
- Read [08.5 The `/etc/group` File](08.5_the_-etc-group_file.md) before changing permissions or supplementary groups.
- Use [08.6 Manual Steps for Adding Users](08.6_manual_steps_for_adding_users.md) to understand what account tools automate.
- Use [08.7 Scripts for Adding Users](08.7_scripts_for_adding_users-_useradd,_adduser,_and_newusers.md) for repeatable account creation.
- Use [08.8 Safe Removal of a User's Account and Files](08.8_safe_removal_of_a_user’s_account_and_files.md) before disabling or deleting access.
- Use [08.9 User Login Lockout](08.9_user_login_lockout.md) when the immediate need is to stop access.
- Use [8.10 Risk Reduction with PAM](8.10_risk_reduction_with_pam.md) when login policy, authentication modules, or access controls are involved.
- Use [8.11 Centralized Account Management](8.11_centralized_account_management.md) when one-host local account management is no longer enough.

## Chapter Map

| Lesson | Focus |
| --- | --- |
| [08.1 Account Mechanics](08.1_account_mechanics.md) | Usernames, UIDs, GIDs, homes, shells, and account lifecycle basics |
| [08.2 The `/etc/passwd` File](08.2_the_-etc-passwd_file.md) | Local account records and safe inspection |
| [08.3 The Linux `/etc/shadow` File](08.3_the_linux_-etc-shadow_file.md) | Password hashes, aging, and lock indicators |
| [08.4 FreeBSD Account Files](08.4_freebsd's_-etc-master.0passwd_and_-etc-login.conf_files.md) | FreeBSD `master.passwd` and `login.conf` differences |
| [08.5 The `/etc/group` File](08.5_the_-etc-group_file.md) | Primary and supplementary group membership |
| [08.6 Manual Steps for Adding Users](08.6_manual_steps_for_adding_users.md) | What account-creation tools do under the hood |
| [08.7 Account Creation Tools](08.7_scripts_for_adding_users-_useradd,_adduser,_and_newusers.md) | `useradd`, `adduser`, `newusers`, and repeatable onboarding |
| [08.8 Safe User Removal](08.8_safe_removal_of_a_user’s_account_and_files.md) | Locking, archiving, file ownership, and removal |
| [08.9 User Login Lockout](08.9_user_login_lockout.md) | Stopping access while preserving evidence |
| [8.10 Risk Reduction with PAM](8.10_risk_reduction_with_pam.md) | PAM policy and authentication risk controls |
| [8.11 Centralized Account Management](8.11_centralized_account_management.md) | LDAP, Active Directory, SSO, and fleet-scale identity |

## Practice Mindset

Use disposable lab systems for account changes. A container, VM, or throwaway cloud instance is enough to practice:

- reading account files
- creating users
- changing groups
- locking and unlocking accounts
- testing login shells
- preserving or archiving home directories

On real systems, start with read-only commands and write down the expected result before making a change.

<!-- lesson-index:start -->

## Lessons in this chapter

- [08.1 Account Mechanics](08.1_account_mechanics.md)
- [Getting to Know etc-passwd 📚](08.2_the_-etc-passwd_file.md)
- [An Exploration into the -etc-shadow File 🕵️‍♀️](08.3_the_linux_-etc-shadow_file.md)
- [08.4 FreeBSD’s -etc-master.passwd & -etc-login.conf Files 🗂️](08.4_freebsd's_-etc-master.0passwd_and_-etc-login.conf_files.md)
- [08.5 The -etc-group File: Group Dynamics 101](08.5_the_-etc-group_file.md)
- [08.6 Manual Steps for Adding Users](08.6_manual_steps_for_adding_users.md)
- [08.7 Scripts for Adding Users: useradd, adduser, and newusers](08.7_scripts_for_adding_users-_useradd,_adduser,_and_newusers.md)
- [Introduction to Safe User Removal 🧹👤](08.8_safe_removal_of_a_user’s_account_and_files.md)
- [User Login Lockout 🔒](08.9_user_login_lockout.md)
- [8.10 Risk Reduction with PAM](8.10_risk_reduction_with_pam.md)
- [8.11 Centralized Account Management 🗂️](8.11_centralized_account_management.md)

<!-- lesson-index:end -->
