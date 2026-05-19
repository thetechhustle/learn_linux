# Glossary

Use this glossary as a quick lookup while working through the lessons and labs. The definitions favor practical Linux operations over academic precision. When a term appears in a lesson and the meaning is not clear from context, look it up here.

---

**ACL**: Access control list. An extension to traditional Unix permissions that can grant or deny access for specific users or groups beyond owner/group/other.

**Apt**: Debian and Ubuntu package-management tooling used to install, update, remove, and inspect software packages. Core commands: `apt install`, `apt update`, `apt upgrade`.

**Bash**: The Bourne Again Shell; the default command interpreter on most Linux systems. Scripts ending in `.sh` typically run in Bash.

**BIND**: A common DNS server implementation used to host authoritative zones and recursive resolvers.

**Bootloader**: The program that starts an operating system kernel. GRUB is the most common Linux bootloader.

**CIDR**: Classless inter-domain routing notation such as `192.0.2.0/24`, used to describe IP networks and address ranges.

**CI/CD**: Continuous integration and continuous delivery or deployment. The practice of building, testing, and shipping changes through repeatable automated pipelines.

**Container**: A lightweight, isolated process environment that shares the host kernel. Docker and Podman are common container runtimes.

**Cron**: A time-based job scheduler. Cron jobs run commands on a schedule defined in a `crontab` file.

**Daemon**: A background process that provides a service. Examples: `sshd` (SSH), `nginx` (web), `systemd` (init).

**Default gateway**: The router a host uses when traffic is destined for a network that is not directly connected.

**DHCP**: Dynamic Host Configuration Protocol. Automatically assigns IP addresses, gateway, and DNS server information to network clients.

**Dnf**: Modern Fedora, Rocky Linux, AlmaLinux, and RHEL-family package-management tooling used to install, update, remove, and inspect software packages.

**DNS**: Domain Name System. The distributed naming system that maps names such as `example.com` to records such as IP addresses, mail exchangers, and service metadata.

**Environment variable**: A named value available to processes in a shell session. Set with `export VAR=value`; read with `echo $VAR`.

**Filesystem**: The structure an operating system uses to organize, store, and retrieve files on a storage device. Common Linux filesystems: ext4, XFS, Btrfs, ZFS.

**Firewall**: Software or hardware that filters network traffic according to rules. Linux labs commonly use `nftables`, `firewalld`, or `ufw`.

**FQDN**: Fully qualified domain name, such as `www.example.com`, that identifies a host or service within the DNS hierarchy.

**GRUB**: Grand Unified Bootloader. Loads the Linux kernel at startup; its configuration lives in `/boot/grub/`.

**Hostname**: The human-readable name assigned to a machine on a network. Set with `hostnamectl set-hostname`.

**IaC**: Infrastructure as Code. Managing servers and configuration through version-controlled files rather than manual steps. Tools include Ansible, Terraform, and Salt.

**Idempotent**: Safe to apply repeatedly with the same intended result. Configuration-management tools aim for idempotent changes.

**Init system**: The first user-space process and service manager (PID 1). On most current Linux distributions, this is `systemd`.

**Inode**: Filesystem metadata that tracks a file's ownership, permissions, timestamps, size, and data-block locations.

**IP address**: A numeric network address assigned to an interface. IPv4 examples look like `192.0.2.10`; IPv6 examples look like `2001:db8::10`.

**Journal**: The systemd logging system queried with `journalctl`. Stores structured log entries from services and the kernel.

**Kernel**: The core of the operating system. Manages hardware, memory, processes, and system calls. The Linux kernel is the `vmlinuz` file in `/boot/`.

**Least privilege**: The practice of granting only the permissions needed to do a specific task, nothing more.

**LDAP**: Lightweight Directory Access Protocol. A standard for directory services used for centralized authentication (user accounts, group membership).

**Load average**: A summary of runnable and waiting work on a system over 1, 5, and 15 minutes. Interpret it with CPU count and workload context.

**LVM**: Logical Volume Manager. A Linux storage layer that can group disks, create flexible logical volumes, and resize storage more easily than raw partitions.

**MFA**: Multi-Factor Authentication. Requiring two or more verification methods (password + one-time code) to authenticate a user.

**Mount point**: The directory where a filesystem is attached to the running file tree. `/` is always mounted; `/home`, `/var`, and `/boot` are common separate mount points.

**NAT**: Network Address Translation. Rewrites packet source or destination addresses; commonly used for private networks that share public connectivity.

**NFS**: Network File System. A Unix-oriented protocol for sharing filesystems over a network.

**Package**: A compressed archive containing software binaries, libraries, and metadata managed by a package manager.

**Package manager**: A tool that installs, updates, and removes software packages and resolves their dependencies automatically (apt, dnf, pacman).

**Package repository**: A trusted source of installable software packages and metadata for tools such as `apt` and `dnf`.

**PATH**: The shell variable that lists directories searched when you run a command without typing its full path.

**PID**: Process identifier. A unique integer the kernel assigns to every running process. View with `ps aux` or `top`.

**Pipeline**: A shell pattern that connects one command's output to another command's input with `|`, or a CI/CD workflow that moves changes through build, test, and deploy stages.

**Port**: A numeric endpoint (0–65535) used by TCP or UDP services. Well-known ports: 22 (SSH), 80 (HTTP), 443 (HTTPS).

**Process**: A running instance of a program. Each process has its own PID, memory space, and set of open files.

**Protocol**: A defined set of rules for communication between networked systems. Examples: TCP, UDP, HTTP, SSH, SMTP.

**RAID**: Redundant Array of Independent Disks. A storage technique that combines disks for redundancy, performance, or both. Levels 0, 1, 5, and 6 are most common.

**Resolver**: The client-side or server-side DNS component that looks up DNS records on behalf of applications or users.

**Rollback**: A planned way to return a system to a known-good state after a change fails or produces unexpected behavior.

**Root**: The superuser account with unrestricted access to the system. Also the top of the filesystem hierarchy (`/`). Avoid running as root unless necessary.

**Runbook**: A written operational procedure for performing or recovering a task. Runbooks are the written evidence of operational knowledge.

**Service unit**: A systemd configuration file (ending in `.service`) that defines how a daemon starts, stops, and restarts.

**Shell**: A command interpreter such as Bash or Zsh that reads user commands and passes them to the kernel.

**Signal**: A process-control notification such as `SIGTERM` or `SIGKILL`. Signals are used to request process shutdown, reload, stop, or other behavior.

**SLA**: Service-level agreement. A formal commitment on availability, response time, or performance of a service.

**SMB**: Server Message Block. A file-sharing protocol commonly used by Windows systems and implemented on Unix-like systems with Samba.

**Snapshot**: A saved point-in-time state of a VM or storage volume. Restore it to undo changes after a mistake.

**SSH**: Secure Shell. The standard encrypted remote-login and remote-command protocol for Linux administration. The `ssh` client connects to `sshd` on port 22.

**Sudo**: A tool that lets authorized users run specific commands with elevated privileges while preserving accountability. Configured in `/etc/sudoers`.

**Swap**: Disk-backed space the kernel can use when memory pressure is high. Swap is slower than RAM and should be interpreted as a symptom source during performance analysis.

**Systemd**: A Linux init system and service manager that also provides logging, timers, sockets, and unit dependency management.

**Tarball**: An archive file, often ending in `.tar`, `.tar.gz`, or `.tgz`, used to bundle files for transfer or backup.

**Terminal**: A text interface for interacting with a shell. Can be a physical TTY, a virtual console (`Ctrl+Alt+F2`), or a terminal emulator application.

**TTL**: Time to live. In DNS, how long a resolver may cache a record before re-querying the authoritative server.

**Unit file**: A systemd configuration file that describes a service, timer, socket, mount, or other managed object.

**Uptime**: How long a system has been running without a reboot. Check with `uptime` or `systemctl show --property=ActiveEnterTimestamp`.

**Virtual machine (VM)**: A complete guest operating system running on virtualized hardware provided by a hypervisor. Provides strong isolation; the recommended lab environment for this course.

**Volume**: A storage object presented to a system or application. Depending on context, it may refer to a disk, partition, logical volume, filesystem, container volume, or cloud block device.

**VPN**: Virtual Private Network. Creates an encrypted tunnel between a client and a server, extending a private network over the internet.

**Zone file**: A DNS data file that defines records for a domain or reverse-lookup zone.
