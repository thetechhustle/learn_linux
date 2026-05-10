## Chapter 03: Access Control and Rootly Powers

Access control is where Linux administration starts to become operationally
serious. You are no longer just running commands on your own machine. You are
deciding who can read data, who can change systems, who can become root, and how
to prove those decisions later.

This chapter builds the access-control model in layers. Start with ordinary
Unix ownership and mode bits, then add root-account practice, ACLs and special
permission bits, modern mandatory access-control systems, and finally the
references worth keeping close when the stakes are high.

!!! success "Operator principle"
    Access is a change-control problem. Grant the smallest useful permission,
    verify it from the user's point of view, and leave a clear rollback path.

## What you should be able to do

By the end of this chapter, you should be able to:

- Read ownership and permissions with `ls`, `stat`, `id`, and `groups`.
- Explain the difference between file and directory permissions.
- Use `chmod`, `chown`, and `chgrp` safely on a lab system.
- Describe why shared write access, `777`, setuid, setgid, and sticky bits
  need special care.
- Inspect POSIX ACLs and explain when they are more appropriate than broad
  group changes.
- Use `sudo -l`, `visudo -c`, and `sshd -T` as access-control evidence.
- Recognize when SELinux or AppArmor may be enforcing a decision that ordinary
  Unix permissions appear to allow.
- Capture a short incident handoff that separates evidence, change, validation,
  and rollback.

## How to read this chapter

Work through the lessons in order. Each one answers a different operational
question:

1. Who owns this file, and what can each class of user do?
2. Who is allowed to become root, and through which audited path?
3. Where are the exceptions to the basic owner/group/other model?
4. Is a mandatory access-control layer also making a decision?
5. Which references should I trust when I need to change access under pressure?

Run examples on a disposable VM, container, or lab host. Do not practice access
changes against a machine you rely on until you understand both the command and
the rollback.

## Field scenario

A contractor needs temporary access to a shared project directory and limited
restart rights for one service. The wrong answer is to make the contractor root
or recursively open the directory to everyone. A better operator flow is:

1. Identify the user, group, directory, service, and expiration date.
2. Inspect the current state before changing anything.
3. Prefer the narrowest model that fits: group membership, ACL, or a validated
   `sudoers` rule.
4. Test from the contractor's point of view.
5. Record exactly what changed and how to remove it.

That pattern is the backbone of the chapter.

<!-- lesson-index:start -->

## Lessons in this chapter

- [Understanding File Ownership and Permissions](03.1_standard_unix_access_control.md)
- [Management of the Root Account](03.2_management_of_the_root_account.md)
- [Extensions to the Standard Access Control Model](03.3_extensions_to_the_standard_access_control_model.md)
- [Modern Access Control](03.4_modern_access_control.md)
- [Recommended Reading](03.5_recommended_reading.md)

<!-- lesson-index:end -->
