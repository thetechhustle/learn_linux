## Chapter 22: SMB and Samba

SMB is the file-sharing protocol most Linux administrators meet when Linux
systems need to share files with Windows, macOS, or mixed desktop fleets.
Samba is the usual Linux implementation. It can publish shares, join Active
Directory environments, authenticate users, and provide enough visibility for
operators to debug access failures without guessing.

This chapter treats SMB as an operational service, not just a checkbox in a
file manager. You will learn how to tell the difference between protocol
reachability, name discovery, authentication, authorization, filesystem
permissions, and client-side mount behavior.

!!! abstract "What you will learn"
    - Explain when SMB is a better fit than NFS, rsync, object storage, or a
      collaboration platform.
    - Identify the Samba services and configuration files that control SMB file
      sharing on Linux.
    - Mount and browse SMB shares from Linux clients with repeatable commands.
    - Separate authentication, share permissions, and local filesystem
      permissions during troubleshooting.
    - Apply baseline security expectations before exposing a share to real
      users.

!!! warning "Production caution"
    SMB shares often sit near sensitive business data and directory identities.
    Test changes on a lab share first, keep a rollback copy of `smb.conf`, and
    avoid broad guest access unless the data owner has explicitly approved it.

## Operator mental model

SMB failures usually come from one of five layers:

1. The client cannot reach TCP port 445 on the server.
2. The client can reach the server but cannot discover or list the share.
3. The user cannot authenticate.
4. The user authenticates but is denied by Samba share rules.
5. Samba allows the request but the underlying Linux filesystem denies it.

Good troubleshooting records which layer failed. For example, `smbclient -L`
tests discovery and authentication, `testparm` validates Samba configuration,
`journalctl` or Samba logs show server-side denials, and `ls -ld` or
`getfacl` confirms local filesystem permissions.

## Skills to build

By the end of this chapter, you should be able to:

- Describe the roles of `smbd`, `nmbd`, and `winbindd`.
- Install Samba packages and validate a minimal share configuration.
- Use `smbclient` to list and inspect shares before mounting them.
- Mount a share manually and understand what belongs in `/etc/fstab`.
- Recognize risky SMB defaults, including guest write access, old protocol
  versions, and shares that expose more of the filesystem than intended.
- Build a short incident note that includes client command output, server log
  evidence, and the exact user or service account being tested.

## Suggested lab path

Use two disposable systems if possible: one Samba server and one Linux client.
If you only have one VM, you can still practice configuration validation and
client commands against `localhost`.

1. Create a lab directory that contains non-sensitive test files.
2. Configure a read-only share first, then validate it with `testparm`.
3. Connect with `smbclient` and record what the client can list.
4. Add one authenticated write path and verify both Samba and filesystem
   permissions.
5. Mount the share from a Linux client, then unmount and clean up the lab.
6. Break one thing at a time, such as the password, share name, or directory
   mode, and identify which evidence changes.

## Common failure patterns

- The firewall allows SSH but not SMB on TCP port 445.
- The share name is correct, but the path in `smb.conf` does not exist.
- The user has a Linux account but no Samba password or directory identity
  mapping.
- Samba permits the share, but Linux mode bits or ACLs deny the file operation.
- A client saved stale credentials and keeps retrying the wrong account.
- Security hardening disabled old SMB dialects that an unsupported client still
  needs.

<!-- lesson-index:start -->

## Lessons in this chapter

- [22.1 Samba: SMB Server for Unix](22.1_samba-_smb_server_for_unix.md)
- [22.2 Installing and Configuring Samba](22.2_installing_and_configuring_samba.md)
- [22.3 Mounting SMB File Shares](22.3_mounting_smb_file_shares.md)
- [22.4 Browsing SMB File Shares](22.4_browsing_smb_file_shares.md)
- [22.5 Ensuring Samba Security](22.5_ensuring_samba_security.md)
- [22.6 Debugging Samba](22.6_debugging_samba.md)
- [22.7 Recommended Reading](22.7_recommended_reading.md)

<!-- lesson-index:end -->
