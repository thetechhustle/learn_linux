# Chapter 17: Single Sign-On

Single sign-on is the practice of letting users authenticate through a central identity service instead of maintaining separate passwords on every Linux host and application. In a small lab, local `/etc/passwd` accounts might be enough. In a real fleet, they become hard to audit, hard to revoke, and easy to configure inconsistently.

This chapter focuses on the Linux administrator's side of SSO: where identities live, how login requests are checked, what can break, and how to investigate failures without weakening access controls.

## What SSO Solves

A central identity system helps administrators answer operational questions such as:

- Who is allowed to log in?
- Which groups grant elevated access?
- Where is authentication failing: client, directory, network, policy, or credential?
- How quickly can a user's access be removed?
- Which logs prove what happened during a login attempt?

SSO does not remove the need for local security discipline. A Linux host still needs correct PAM rules, NSS configuration, sudo policy, SSH settings, time synchronization, certificates, and emergency access planning.

## Common Building Blocks

Most Linux SSO environments combine several pieces:

- Directory service: stores users, groups, and attributes.
- Authentication protocol: verifies credentials or tickets.
- Authorization policy: decides what authenticated users can do.
- Client integration: connects Linux login tools to the identity source.
- Cache and offline behavior: controls whether logins continue during outages.
- Audit trail: records successful and failed access attempts.

LDAP is a common directory protocol, but LDAP alone is not the entire SSO design. Many environments also use Kerberos, SSSD, FreeIPA, Active Directory, SAML, OAuth 2.0, OpenID Connect, or cloud identity providers depending on the systems being integrated.

## Linux Login Flow

When a user signs in to a Linux host, several subsystems may participate:

1. The entry point accepts the login attempt, such as SSH, console login, or a display manager.
2. PAM applies authentication and account policy.
3. NSS resolves user and group information.
4. SSSD or another client talks to the directory or identity provider.
5. sudo, SSH, or application policy decides what the user may do after login.
6. Logs record the result for troubleshooting and audit.

That separation matters. A user can authenticate successfully but still be denied by account policy, group membership, host access rules, shell settings, home-directory problems, expired credentials, or sudo policy.

## Safe Operating Habits

Treat identity changes like production infrastructure changes:

- Keep at least one tested emergency local admin path.
- Test new policies with a noncritical account before broad rollout.
- Verify time synchronization before debugging Kerberos or certificate-based flows.
- Confirm name resolution and TLS trust before blaming credentials.
- Record the exact host, username, command, timestamp, and log lines for each incident.
- Avoid changing PAM or NSS rules over an SSH session unless you have a fallback console.

## Chapter Path

Start with the core elements, then move into LDAP and host login integration. The later lessons compare alternative identity patterns and point to deeper reading.

<!-- lesson-index:start -->

## Lessons in this chapter

- [17.1 Core SSO Elements](17.1_core_sso_elements.md)
- [17.2 LDAP: “Lightweight” Directory Services 🗂️](17.2_ldap-_“lightweight”_directory_services.md)
- [17.3 Using Directory Services for Login](17.3_using_directory_services_for_login.md)
- [17.4 Alternative Approaches 🚀](17.4_alternative_approaches.md)
- [17.5 Recommended Reading](17.5_recommended_reading.md)

<!-- lesson-index:end -->
