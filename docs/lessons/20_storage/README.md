# Chapter 20: Storage

Storage work is where Linux administration becomes physically real. A
service can be restarted, a package can be reinstalled, and a bad
configuration can often be reverted. Lost data is different. Before you
resize a filesystem, replace a failed disk, create a RAID set, or test a
backup, you need a clear picture of the devices, layers, owners, and
failure modes involved.

This chapter builds that picture from the bottom up. You will learn how
Linux sees disks, partitions, logical volumes, RAID arrays, filesystems,
mount points, and backups. The goal is not to memorize every storage
feature. The goal is to make storage changes deliberately, verify them
with evidence, and know when to stop before a command becomes
destructive.

## What You Should Be Able To Do

By the end of this chapter, you should be able to:

- Identify storage devices and explain what each layer is doing.
- Add a new disk without confusing the device, partition, filesystem, and
  mount-point steps.
- Read the current storage state with tools such as `lsblk`, `blkid`,
  `findmnt`, `df`, `du`, `mount`, `mdadm`, `lvs`, and `zpool`.
- Understand when LVM, RAID, ZFS, Btrfs, or a traditional filesystem is
  the right tool for the job.
- Explain the difference between redundancy, snapshots, replication, and
  backups.
- Plan storage maintenance with rollback, monitoring, and recovery in
  mind.

## The Storage Stack

A useful way to reason about storage is to separate the stack into
layers:

1. Hardware: disks, SSDs, NVMe drives, controllers, cables, enclosures,
   and cloud block devices.
2. Device discovery: kernel device names, persistent identifiers, udev,
   and multipath where needed.
3. Partitioning: GPT or legacy partition tables that divide a disk into
   usable regions.
4. Aggregation: LVM, software RAID, hardware RAID, ZFS pools, Btrfs
   multi-device layouts, or cloud volume managers.
5. Filesystems: ext4, XFS, UFS, ZFS, Btrfs, and the metadata structures
   that turn blocks into files.
6. Mounting and policy: `/etc/fstab`, mount options, quotas, permissions,
   SELinux labels, and service expectations.
7. Protection: snapshots, backups, restores, monitoring, and replacement
   plans.

When something breaks, naming the failed layer is half the repair. "The
disk is full" might mean the filesystem is full, the inode table is full,
the thin pool is exhausted, the snapshot reserve is gone, the wrong mount
point is being used, or the application is writing somewhere unexpected.

## Start With Evidence

Before making a storage change, collect the current state:

```bash
lsblk -f
findmnt
df -hT
sudo blkid
sudo journalctl -k --since "1 hour ago"
```

For a production host, also check the application owner, backup status,
monitoring alerts, and whether anything is actively writing to the target
path. A safe storage operator can explain both the command they are about
to run and the evidence that makes that command appropriate.

## Common Storage Jobs

This chapter prepares you for practical work such as:

- Adding a new disk to a server.
- Growing a filesystem after a cloud volume resize.
- Moving an application directory to a larger mount point.
- Creating or repairing an LVM volume.
- Understanding a degraded RAID array.
- Choosing between ext4 and XFS for ordinary Linux workloads.
- Knowing when ZFS or Btrfs features are worth the operational cost.
- Designing a backup plan that has actually been restored in a test.

Each job should be treated as a small procedure: inspect, plan, back up,
change, verify, and document. The dangerous commands are rarely long.
They are dangerous because they act on the wrong device, the wrong layer,
or the wrong assumption.

## Redundancy Is Not Backup

RAID, mirrored disks, cloud replication, ZFS copies, and Btrfs profiles can
keep a system online through certain hardware failures. They do not
protect you from every ordinary disaster. A bad deletion, ransomware, a
corrupt application migration, a mistaken `mkfs`, or a buggy script can be
replicated perfectly across redundant storage.

Backups need a separate recovery story:

- What is backed up?
- How often is it backed up?
- Where is it stored?
- Who can restore it?
- How long does restore take?
- When was the last test restore?

If you cannot answer those questions, you do not yet have a reliable
backup strategy.

## Safety Habits

Use these habits throughout the storage lessons:

- Prefer persistent identifiers in `/etc/fstab`, such as UUIDs, over
  unstable device names like `/dev/sdb`.
- Read command output twice before running destructive commands such as
  `mkfs`, `wipefs`, `dd`, `parted`, `pvcreate`, or `zpool destroy`.
- Keep a terminal log or change note for storage work.
- Confirm backups before resizing, reformatting, replacing, or
  repartitioning.
- Verify the result from the kernel's point of view and the application's
  point of view.
- Practice on disposable disks or loop devices before touching important
  systems.

Storage rewards patience. Most serious incidents happen when someone
skips inventory, assumes a device name, or treats redundancy as recovery.

## How To Use This Chapter

Read the early lessons in order if storage is new to you. They establish
the device and layering vocabulary needed for the rest of the chapter.
After that, you can return to individual topics when a job demands them:
LVM for flexible volume management, RAID for redundancy, filesystems for
layout and behavior, ZFS or Btrfs for integrated storage features, and
backup strategy for recovery planning.

The hands-on mindset matters more than the specific platform. Whether the
disk is a physical SATA drive, an NVMe device, a virtual disk, or a cloud
block volume, the operational questions stay the same: what is it, who
depends on it, what protects it, how will we change it, and how will we
prove the change worked?

<!-- lesson-index:start -->

## Lessons in this chapter

- [20.1 I Just Want to Add a Disk!](20.1_i_just_want_to_add_a_disk!.md)
- [20.2 Storage Hardware: The Physical Layer of Storage](20.2_storage_hardware.md)
- [Understanding Storage Hardware Interfaces](20.3_storage_hardware_interfaces.md)
- [20.4 Attachment and Low-Level Management of Drives](20.4_attachment_and_low-level_management_of_drives.md)
- [20.5 The Software Side of Storage: Peeling the Onion](20.5_the_software_side_of_storage-_peeling_the_onion.md)
- [20.6 Disk Partitioning: Organizing Your Linux Space](20.6_disk_partitioning.md)
- [20.7 Logical Volume Management (LVM)](20.7_logical_volume_management.md)
- [20.8 RAID: Redundant Arrays of Inexpensive Disks](20.8_raid-_redundant_arrays_of_inexpensive_disks.md)
- [20.9 Filesystems: The Librarian of Your Linux System](20.9_filesystems.md)
- [20.10 Traditional Filesystems: UFS, EXT4, and XFS](20.10_traditional_filesystems-_ufs,_ext4,_and_xfs.md)
- [20.11 Next-Generation Filesystems: ZFS and Btrfs](20.11_next-generation_filesystems-_zfs_and_btrfs.md)
- [Understanding ZFS: All Your Storage Problems Solved](20.12_zfs-_all_your_storage_problems_solved.md)
- [20.13_Btrfs: 'ZFS Lite' for Linux](20.13_btrfs-_“zfs_lite”_for_linux.md)
- [20.14 Data Backup Strategy](20.14_data_backup_strategy.md)
- [20.15 Recommended Reading](20.15_recommended_reading.md)

<!-- lesson-index:end -->
