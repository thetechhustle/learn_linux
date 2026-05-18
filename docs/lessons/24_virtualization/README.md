## Chapter 24: Virtualization

Virtualization lets one physical system run multiple isolated operating systems,
test environments, or repeatable lab machines. For administrators, it is less
about novelty and more about controlled risk: you can snapshot before a change,
practice a migration, reproduce a bug, and separate workloads without buying a
new server for every experiment.

This chapter focuses on the operational side of virtualization. You will learn
the language used by hypervisors, how Linux and FreeBSD host virtual machines,
where desktop tools such as VirtualBox fit, and how image-building tools such as
Packer and Vagrant support repeatable environments.

!!! abstract "Learning outcomes"
    By the end of this chapter, you should be able to:

    - Explain the difference between hosts, guests, hypervisors, images, disks,
      snapshots, templates, and virtual networks.
    - Choose a virtualization tool that fits a lab, workstation, or server use
      case.
    - Inspect VM CPU, memory, disk, and network settings before making changes.
    - Use snapshots and disposable guests to reduce the risk of risky commands.
    - Describe how image and environment automation improves repeatability.

!!! warning "Production caution"
    Virtual machines still consume real CPU, memory, storage, and network
    capacity. Avoid treating a VM as "just a file." Oversubscribed hosts, thin
    disks, missing backups, and unclear network placement can turn a small lab
    habit into a production incident.

## How to approach this chapter

Start with vocabulary, then build a small lab habit: inspect the host, inspect
the guest, make one reversible change, and record the evidence. That pattern is
useful whether you are using KVM on Linux, bhyve on FreeBSD, VMware in an
enterprise, or VirtualBox on a laptop.

A useful virtualization lab should answer these questions:

- What resources does the guest need, and what does the host actually have?
- Where does the guest disk live, and is it backed up or disposable?
- Which network can the guest reach, and which systems can reach it?
- Is there a snapshot or rebuild path before risky testing begins?
- What command proves the guest is healthy after a change?

## Common failure patterns

- **Resource oversubscription:** too many vCPUs, too much committed memory, or
  thin disks that quietly fill the host.
- **Snapshot misuse:** keeping long snapshot chains as a substitute for backup,
  or forgetting that snapshots can grow quickly.
- **Network confusion:** guests attached to the wrong bridge, NAT network, VLAN,
  or host-only segment.
- **Image drift:** hand-built guests that cannot be recreated because setup
  steps were never written down.
- **Host dependency:** several important guests relying on one unmonitored host
  with no maintenance or recovery plan.

## Suggested lab path

1. Create or choose a disposable Linux guest.
2. Record its CPU, memory, disk, and network settings.
3. Take a snapshot before changing the guest.
4. Run a small administrative task inside the guest, such as adding a test user
   or installing a package.
5. Verify the task, revert the snapshot, and confirm the guest returned to the
   earlier state.
6. Write down which parts were reproducible and which depended on manual steps.

## Lessons in this chapter

- [24.1 Virtual Vernacular](24.1_virtual_vernacular.md)
- [24.2 Virtualization with Linux](24.2_virtualization_with_linux.md)
- [24.3 FreeBSD bhyve](24.3_freebsd_bhyve.md)
- [24.4 VMware](24.4_vmware.md)
- [24.5 VirtualBox](24.5_virtualbox.md)
- [24.6 Packer](24.6_packer.md)
- [24.7 Vagrant](24.7_vagrant.md)
- [24.8 Recommended Reading](24.8_recommended_reading.md)
