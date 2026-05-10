## Chapter 02: Booting and System Management Daemons

This chapter teaches the path from power-on to a usable Linux system, then turns that path into an operator workflow. A system that fails during boot is not just "down"; it is failing at a specific boundary. Your job is to identify the boundary, collect evidence without making the outage worse, and choose the smallest reversible fix.

By the end of this chapter, you should be able to:

- Trace the boot chain from firmware to boot loader, kernel, initramfs, `systemd`, and services.
- Distinguish firmware, bootloader, kernel, and service-manager failures from each other.
- Use `systemctl`, `journalctl`, boot logs, and rescue targets to build a useful evidence trail.
- Reboot or shut down a host deliberately, with attention to users, services, and data integrity.
- Explain when a nonbooting system needs rollback, rescue media, filesystem repair, or hardware investigation.

### The Operator Mental Model

Treat boot as a handoff sequence:

```text
firmware -> boot loader -> kernel/initramfs -> PID 1 -> targets/services -> login or workload
```

Each handoff has different evidence and different risk:

- Firmware and hardware problems often show up before the OS logs anything.
- Boot loader problems usually affect menu entries, kernel arguments, or missing boot files.
- Kernel and initramfs problems often involve storage, drivers, root filesystems, or panic output.
- `systemd` and service problems usually leave useful logs in the journal.
- Shutdown and reboot problems often involve stuck units, active users, mounts, or remote access loss.

### Safe Lab Approach

Practice on disposable virtual machines or cloud instances. Avoid changing boot loader files, firmware settings, filesystem repair tools, or shutdown behavior on a host you rely on until you have a rollback plan.

For each lesson, keep a short lab note:

1. What stage of boot or shutdown are you inspecting?
2. What read-only command did you run?
3. What output proves the current state?
4. What change would be reversible, and how would you undo it?
5. What would you hand to the next operator during an incident?

### Suggested Command Set

Start with read-only inspection:

```bash
systemctl list-units --failed
systemctl status
journalctl -b -p warning
journalctl -b -u ssh.service
systemctl get-default
lsblk -f
findmnt /
```

Use changing commands only in a lab or with approval:

```bash
sudo systemctl isolate rescue.target
sudo systemctl set-default multi-user.target
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
sudo reboot
```

### What Good Looks Like

A strong answer in this chapter is not a memorized boot diagram. It is a short operational explanation:

- where the host failed
- what evidence supports that conclusion
- what you tried first
- what you intentionally avoided
- what the next safe step should be

<!-- lesson-index:start -->

## Lessons in this chapter

- [The Symphony of Start-Up: Linux Boot Process](02.1_boot_process_overview.md)
- [02.2 System Firmware - Your System's Master of Ceremonies 🎩](02.2_system_firmware.md)
- [Understanding Boot Loaders 🚀](02.3_boot_loaders.md)
- [02.4 GRUB: The Grand Unified Boot Loader](02.4_grub-_the_grand_unified_boot_loader.md)
- [02.5 The FreeBSD Boot Process](02.5_the_freebsd_boot_process.md)
- [02.6 System Management Daemons 💼](02.6_system_management_daemons.md)
- [Understanding systemd](02.7_systemd_in_detail.md)
- [02.8 FreeBSD Init and Startup Scripts 📜](02.8_freebsd_init_and_startup_scripts.md)
- [Restarting and Shutting Down Systems in Linux](02.9_reboot_and_shutdown_procedures.md)
- [02.10 Stratagems for a Non-Booting System 💡🚀](2.10_stratagems_for_a_nonbooting_system.md)

<!-- lesson-index:end -->
