## Chapter 11: Drivers and the Kernel

The kernel is the part of Linux that talks directly to hardware, schedules processes, manages memory, exposes devices, loads drivers, and decides what happens during boot. Most administrators do not rebuild kernels every day, but they do depend on kernel behavior every day.

This chapter is about operating the kernel safely. You will learn how to inspect the running kernel, connect hardware symptoms to drivers and modules, make low-risk boot choices, and know when a kernel change needs a rollback plan instead of optimism.

!!! abstract "What you will learn"
    - Identify the running kernel version and understand why it matters.
    - Connect devices, drivers, modules, and boot choices during troubleshooting.
    - Recognize when a kernel update, module change, or configuration change can affect uptime.
    - Build an evidence trail for kernel-related incidents without making the system worse.

!!! example "Operator scenario"
    A server reboots after updates and loses network connectivity. The application did not change, but the kernel did. A useful investigation checks the booted kernel, previous kernel, network driver, loaded modules, kernel logs, and bootloader fallback options before making another change.

!!! success "Chapter principle"
    Treat the kernel as a shared operating contract between hardware, drivers, services, and boot configuration. Inspect first, change carefully, and keep a rollback path.

## What the kernel does for operators

The kernel is not just theory. It is visible in common operations work:

- A storage device appears as `/dev/nvme0n1` or disappears after a driver issue.
- A network card needs the right kernel module to come online.
- A container runtime depends on kernel namespaces, cgroups, and filesystems.
- A cloud VM may need a different kernel for a provider-specific device or performance feature.
- A security update may install a new kernel and require a reboot.
- A boot problem may require selecting an older kernel from the bootloader.

When kernel work goes wrong, the symptom often appears somewhere else: networking, storage, boot, performance, or service stability.

## Evidence before action

Kernel troubleshooting should start with read-only facts:

```bash
uname -a
uname -r
cat /etc/os-release
journalctl -k -b --no-pager | tail -80
lsmod | head
lspci -nn
lsblk
```

Those commands answer basic questions:

- Which kernel is currently running?
- Which distribution and release is this host using?
- What did the kernel report during this boot?
- Which modules are loaded?
- What hardware and block devices does the system see?

On systems that use `systemd`, previous-boot kernel logs are often essential:

```bash
journalctl -k -b -1 --no-pager
```

That command is especially useful after a reboot, failed upgrade, driver issue, or unexpected kernel panic.

## Common administrator responsibilities

Kernel-related chores include:

- Tracking the running kernel version.
- Applying distribution-supported kernel updates.
- Rebooting into new kernels during maintenance windows.
- Keeping at least one known-good older kernel available.
- Checking whether a hardware issue maps to a driver or module.
- Loading, unloading, or blacklisting modules only when the risk is understood.
- Confirming bootloader entries and fallback options.
- Capturing kernel logs before evidence rotates away.

Most production systems should use vendor or distribution kernels unless there is a strong reason not to. Custom kernels can be appropriate, but they increase support and rollback responsibility.

## Risk boundaries

Some kernel actions are low-risk inspection:

```bash
uname -r
journalctl -k -b --no-pager
lsmod
modinfo e1000e
```

Some actions can interrupt service and need more care:

```bash
sudo modprobe -r driver_name
sudo modprobe driver_name
sudo grubby --set-default /boot/vmlinuz-example
sudo reboot
```

Before a risky kernel action, know:

1. What problem are you trying to solve?
2. What evidence points to the kernel, driver, module, or boot path?
3. What is the rollback path?
4. Is there console or out-of-band access if networking fails?
5. Is this a maintenance window or an emergency?

## How to use this chapter

Read Chapter 11 as an operator map:

- **11.1 Kernel chores** covers the everyday administrator tasks around versions, updates, modules, and cleanup.
- **11.2 Kernel version numbering** explains how to read version strings and distribution kernel naming.
- **11.3 Devices and drivers** connects hardware detection to driver behavior.
- **11.4 and 11.5 Kernel configuration** explain Linux and FreeBSD configuration concepts.
- **11.6 Loadable kernel modules** covers module inspection and careful module changes.
- **11.7 Booting** shows how the system reaches the running kernel.
- **11.8 Alternate kernels in the cloud** covers cloud-specific boot and kernel choices.
- **11.9 Kernel errors** focuses on panic, oops, hardware, and driver failure evidence.
- **11.10 Recommended reading** points to deeper kernel and driver references.

## Hands-on practice

Use a lab VM when practicing anything that could affect boot, modules, storage, or networking.

1. Record the running kernel with `uname -r`.
2. Capture the last 80 kernel log lines from the current boot.
3. List loaded modules and pick one harmless module to inspect with `modinfo`.
4. Identify one storage device and one network device.
5. Find whether your system has more than one installed kernel package.
6. Write a rollback note for a hypothetical kernel update.

Example rollback note:

```text
Host: lab-vm-01
Current kernel: 6.x.y
New kernel to test: 6.x.z
Rollback path:
  - use bootloader previous-kernel entry from console
  - confirm network after boot with ip addr and ping gateway
  - preserve journalctl -k -b and -b -1 output
Risk:
  - network driver regression would require console access
```

## Check your understanding

- Why is `uname -r` not enough by itself during a kernel incident?
- What evidence would connect a network outage to a driver or module?
- Why should a production kernel update have a rollback path?
- What is the difference between inspecting a module and unloading one?
- Why is console access important before changing boot or network-driver behavior?

<!-- lesson-index:start -->

## Lessons in this chapter

- [11.1 Kernel Chores for System Administrators](11.1_kernel_chores_for_system_administrators.md)
- [11.2 Kernel Version Numbering](11.2_kernel_version_numbering.md)
- [11.3 Devices and Their Drivers](11.3_devices_and_their_drivers.md)
- [11.4 Linux Kernel Configuration](11.4_linux_kernel_configuration.md)
- [11.5 FreeBSD Kernel Configuration](11.5_freebsd_kernel_configuration.md)
- [11.6 Loadable Kernel Modules](11.6_loadable_kernel_modules.md)
- [11.7 Booting: From Ignition 🚀 to Liftoff 🏁](11.7_booting.md)
- [11.8 Booting Alternate Kernels in the Cloud](11.8_booting_alternate_kernels_in_the_cloud.md)
- [Coping with the Unexpected: Kernel Errors](11.9_kernel_errors.md)
- [11.10 Recommended Reading](11.10_recommended_reading.md)

<!-- lesson-index:end -->
