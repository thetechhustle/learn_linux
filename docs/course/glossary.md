# Glossary

Use this glossary as a quick lookup while working through the lessons and labs. The definitions favor practical Linux operations over academic precision.

**ACL**: Access control list. An extension to traditional Unix permissions that can grant or deny access for specific users or groups.

**Apt**: Debian and Ubuntu package-management tooling used to install, update, remove, and inspect software packages.

**BIND**: A common DNS server implementation used to host authoritative zones and recursive resolvers.

**Bootloader**: The program that starts an operating system kernel. GRUB is the most common Linux bootloader.

**CIDR**: Classless inter-domain routing notation such as `192.0.2.0/24`, used to describe IP networks and address ranges.

**CI/CD**: Continuous integration and continuous delivery or deployment. The practice of building, testing, and shipping changes through repeatable pipelines.

**Daemon**: A background process that provides a service.

**Default gateway**: The router a host uses when traffic is destined for a network that is not directly connected.

**Dnf**: Modern Fedora, Rocky Linux, AlmaLinux, and RHEL-family package-management tooling used to install, update, remove, and inspect software packages.

**DNS**: Domain Name System. The distributed naming system that maps names such as `example.com` to records such as IP addresses, mail exchangers, and service metadata.

**FQDN**: Fully qualified domain name, such as `www.example.com`, that identifies a host or service within the DNS hierarchy.

**Filesystem**: The structure an operating system uses to store and retrieve files.

**Firewall**: Software or hardware that filters network traffic according to rules. Linux labs commonly use tools such as `nftables`, `firewalld`, or `ufw`.

**GRUB**: Grand Unified Bootloader. A bootloader used by many Linux distributions to choose and start kernels.

**Idempotent**: Safe to apply repeatedly with the same intended result. Configuration-management tools aim for idempotent changes.

**Init system**: The first user-space process and service manager. On most current Linux distributions, this is systemd.

**Inode**: Filesystem metadata that tracks a file's ownership, permissions, timestamps, size, and data-block locations.

**IP address**: A numeric network address assigned to an interface. IPv4 examples look like `192.0.2.10`; IPv6 examples look like `2001:db8::10`.

**Journal**: The systemd logging system queried with `journalctl`.

**Kernel**: The core of the operating system that manages hardware, processes, memory, and system calls.

**Least privilege**: The practice of granting only the access needed to do a task.

**Load average**: A summary of runnable and waiting work on a system over 1, 5, and 15 minutes. Interpret it with CPU count and workload context.

**LVM**: Logical Volume Manager. A Linux storage layer that can group disks, create flexible logical volumes, and resize storage more easily than raw partitions.

**Mount point**: The directory where a filesystem is attached to the running file tree.

**NAT**: Network address translation. A technique that rewrites packet addresses, commonly used for private networks that share public connectivity.

**NFS**: Network File System. A Unix-oriented protocol for sharing filesystems over a network.

**Package repository**: A trusted source of installable software packages and metadata for tools such as `apt` and `dnf`.

**PATH**: The shell variable that lists directories searched when you run a command without typing its full path.

**PID**: Process identifier. A numeric ID assigned to a running process.

**Pipeline**: A shell pattern that connects one command's output to another command's input with `|`, or a CI/CD workflow that moves changes through build, test, and deploy stages.

**Port**: A numeric endpoint used by TCP or UDP services. For example, SSH commonly listens on TCP port 22.

**RAID**: Redundant array of independent disks. A storage technique that combines disks for redundancy, performance, or both.

**Resolver**: The client-side or server-side DNS component that looks up DNS records on behalf of applications or users.

**Rollback**: A planned way to return a system to a known-good state after a change fails or produces unexpected behavior.

**Runbook**: A written operational procedure for performing or recovering a task.

**Service unit**: A systemd configuration object that controls a daemon or service.

**Shell**: A command interpreter such as Bash or Zsh.

**Signal**: A process-control notification such as `SIGTERM` or `SIGKILL`. Signals are used to request process shutdown, reload, stop, or other behavior.

**SLA**: Service-level agreement. A formal or informal promise about service behavior such as availability, response time, or support handling.

**SMB**: Server Message Block. A file-sharing protocol commonly used by Windows systems and implemented on Unix-like systems with Samba.

**Snapshot**: A saved VM or storage state that can be restored after a mistake.

**SSH**: Secure Shell. The standard encrypted remote-login and remote-command protocol for Linux administration.

**Sudo**: A tool that lets authorized users run specific commands with elevated privileges while preserving accountability.

**Swap**: Disk-backed space the kernel can use when memory pressure is high. Swap is slower than RAM and should be interpreted as a symptom source during performance analysis.

**systemd**: A Linux init system and service manager that also provides logging, timers, sockets, and unit dependency management.

**Tarball**: An archive file, often ending in `.tar`, `.tar.gz`, or `.tgz`, used to bundle files for transfer or backup.

**TTL**: Time to live; in DNS, the cache duration for a record.

**Unit file**: A systemd configuration file that describes a service, timer, socket, mount, or other managed object.

**Virtual machine**: A complete guest operating system running on virtualized hardware provided by a hypervisor.

**Volume**: A storage object presented to a system or application. Depending on context, it may refer to a disk, partition, logical volume, filesystem, container volume, or cloud block device.

**Zone file**: A DNS data file that defines records for a domain or reverse-lookup zone.
