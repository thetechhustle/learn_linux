# Chapter 05: The Filesystem

Filesystems are where Linux turns hardware, processes, users, and
applications into something you can inspect and manage. When a service cannot
write a file, a disk fills during a release, a mount disappears after reboot,
or a backup misses critical data, the first useful step is usually filesystem
evidence.

This chapter teaches the filesystem as an operator surface, not just a place
to store files. You will learn how to move through pathnames, recognize mount
boundaries, read the standard file tree, identify file types, inspect file
metadata, and use access control lists when basic permission bits are not
enough.

## What You Should Be Able to Do

By the end of this chapter, you should be able to:

- Explain the difference between a pathname problem, a mount problem, a
  permission problem, and a capacity problem.
- Use `pwd`, `ls`, `stat`, `find`, `df`, `du`, `mount`, and related tools to
  collect read-only evidence before changing a system.
- Identify important top-level directories such as `/etc`, `/var`, `/home`,
  `/usr`, `/opt`, `/tmp`, `/proc`, and `/dev`.
- Recognize regular files, directories, symbolic links, device files, sockets,
  and pipes.
- Interpret file ownership, modes, timestamps, inode data, and extended
  attributes as operational signals.
- Decide when standard Unix permissions are enough and when ACLs are the right
  tool.

## Operator Scenario

Imagine a deployment fails because the application says it cannot write its
cache file. A weak response is to change permissions until the error goes away.
A stronger response is to prove what is happening:

```bash
pwd
ls -ld /var /var/cache /var/cache/example
stat /var/cache/example
df -h /var/cache/example
mount | grep ' /var '
getfacl /var/cache/example 2>/dev/null || true
```

Those commands separate several different failure modes:

- The path might be wrong.
- The directory might live on a read-only or full filesystem.
- Ownership or mode bits might block the application user.
- An ACL might override what the basic mode bits suggest.
- A symbolic link might point somewhere unexpected.

This is the habit the chapter builds: collect enough evidence to make the next
change small, reversible, and explainable.

## Study Path

Start with pathnames, because every filesystem investigation depends on naming
the target precisely. Then study mounting so you understand where one
filesystem ends and another begins. After that, learn the file tree, file
types, attributes, and ACLs as layers of evidence you can combine during real
troubleshooting.

For each lesson, keep a short lab note with three parts:

1. The read-only command you ran.
2. The important line of output.
3. The operational conclusion you can safely draw from it.

## Safety Notes

Filesystem commands can be deceptively risky. Prefer read-only inspection while
learning. Be careful with `rm`, recursive ownership changes, recursive
permission changes, and commands that write to block devices or mounted
filesystems. In production, capture the current state before changing it and
make sure you know how to undo the change.

<!-- lesson-index:start -->

## Lessons in this chapter

- [05.1 Pathnames](05.1_pathnames.md)
- [05.2 Filesystem Mounting and Unmounting](05.2_filesystem_mounting_and_unmounting.md)
- [05.3 Organization of the File Tree](05.3_organization_of_the_file_tree.md)
- [05.4 File Types](05.4_file_types.md)
- [05.5 File Attributes](05.5_file_attributes.md)
- [05.6 Access Control Lists](05.6_access_control_lists.md)

<!-- lesson-index:end -->
