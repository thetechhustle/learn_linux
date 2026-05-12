## Chapter 21: Network File System

Network storage is where local Linux administration starts to become shared
infrastructure. A directory that looks ordinary on one machine might actually
live on another server, depend on a network path, enforce remote permissions,
and affect dozens of clients when it slows down or disappears.

This chapter uses NFS as the main model for understanding shared filesystems on
Linux. The goal is not merely to mount a directory. The goal is to know what is
being shared, who can access it, how identity is mapped, what failure looks
like, and how to operate the service without surprising the people and systems
that depend on it.

### What NFS Solves

NFS lets Linux and Unix-like systems present remote files as part of the local
filesystem tree. That makes it useful for shared home directories, build
artifacts, application data, backup staging areas, media libraries, and lab
environments where several machines need the same files.

That convenience comes with real operational tradeoffs. NFS depends on network
reachability, server availability, correct exports, compatible mount options,
stable identity mapping, and careful client behavior. A bad export can expose
too much data. A bad mount option can hang boot. A slow server can look like a
slow application. A UID mismatch can turn a clean design into a permissions
mess.

### The Operator's Mental Model

Treat every NFS setup as four connected decisions:

- **Data boundary**: what directory is being shared, which data belongs there,
  and what should stay local.
- **Trust boundary**: which clients are allowed to mount it, what permissions
  they receive, and whether root on a client should be trusted.
- **Identity boundary**: how users, groups, UIDs, GIDs, and NFSv4 names map
  across machines.
- **Failure boundary**: what happens when the server, network, DNS, or identity
  service is unavailable.

When those boundaries are explicit, NFS becomes manageable. When they are
implicit, small configuration choices can turn into outages or security issues.

### What You Will Learn

The chapter starts by placing NFS among other network file services, then
narrows into the NFS design itself. From there, it separates the server and
client sides so you can reason about exports, mounts, permissions, and
troubleshooting one layer at a time.

You will also learn why NFSv4 identity mapping matters, how `nfsstat` helps
separate client, server, and network symptoms, where dedicated file servers fit,
and how automatic mounting can make shared filesystems easier to consume
without making every boot depend on every remote share.

### Skills to Build

By the end of this chapter, you should be able to:

- Explain when NFS is a good fit and when another storage pattern is safer.
- Read an export and identify the clients, permissions, and trust assumptions.
- Mount an NFS share deliberately instead of copying an option string blindly.
- Diagnose common failures such as permission denied, stale handles, hangs, and
  slow reads or writes.
- Distinguish file permissions from export policy, firewall policy, DNS issues,
  and identity-mapping issues.
- Use automounting to reduce startup fragility and idle mount overhead.
- Describe the operational responsibilities of a dedicated NFS server.

### Lessons in This Chapter

- [21.1 Meet Network File Services](21.1_meet_network_file_services.md)
- [21.2 The NFS Approach: Creating Seamless Networks](21.2_the_nfs_approach.md)
- [21.3 Server-Side NFS](21.3_server-side_nfs.md)
- [21.4 Client-Side NFS](21.4_client-side_nfs.md)
- [21.5 Identity Mapping for NFS Version 4](21.5_identity_mapping_for_nfs_version_4.md)
- [21.6 NFSstat: Dump NFS Statistics](21.6_nfsstat-_dump_nfs_statistics.md)
- [21.7 Dedicated NFS File Servers](21.7_dedicated_nfs_file_servers.md)
- [21.8 Automatic Mounting](21.8_automatic_mounting.md)
- [21.9 Recommended Reading](21.9_recommended_reading.md)

### How to Practice Safely

Use two disposable Linux systems or virtual machines if possible: one server and
one client. Keep the first export small, read-only, and filled with test data.
Confirm basic connectivity and name resolution before changing NFS settings.
Then change one variable at a time: export options, mount options, identity
mapping, firewall rules, and automount configuration.

Avoid practicing on important home directories or production application data
until you can explain the export policy, rollback path, and expected client
behavior during a server restart. Network filesystems are powerful because they
make remote data feel local; they are risky for the same reason.
