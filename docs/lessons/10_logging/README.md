## Chapter 10: Logging

Logs are the operating record of a Linux system. They show what started, what failed, who authenticated, which services changed state, and what the kernel reported while hardware, drivers, and filesystems were coming online. When an incident is active, logs often become the shared timeline that lets operators compare symptoms with facts.

This chapter teaches logging as an evidence workflow, not as a pile of files to memorize. You will learn where common logs live, how the systemd journal and syslog fit together, how to inspect boot and kernel messages, and how to keep logs useful without letting them fill disks or expose sensitive data.

!!! abstract "What you will learn"
    - Find the right local log source for service, authentication, kernel, package, and boot events.
    - Use `journalctl`, `/var/log`, syslog files, and rotation state to build a short incident timeline.
    - Distinguish read-only investigation from changes that alter retention, forwarding, or access.
    - Explain when local logs are enough and when centralized logging, retention policy, or compliance rules matter.

!!! success "Operator principle"
    Start with the question you need logs to answer: what changed, when it changed, who or what changed it, and whether the problem is still happening.

## Logging Triage Sequence

Use this order when you do not yet know where the failure is coming from:

1. Write down the symptom, hostname, service name, and approximate time window.
2. Check service state and recent journal entries with read-only commands such as `systemctl status <unit>` and `journalctl -u <unit> --since "30 minutes ago"`.
3. Check distribution log files under `/var/log` when the service or subsystem writes text logs there.
4. Check kernel and boot messages with `journalctl -k`, `dmesg`, and boot-specific journal queries.
5. Correlate timestamps across application, authentication, package, kernel, and scheduler logs before making a change.
6. Preserve the exact command and output that support your conclusion.

## Safety Boundaries

Most log inspection is safe and read-only, but log management can affect incident response and compliance. Be careful with:

- Deleting, truncating, or compressing logs before confirming retention requirements.
- Changing `journald`, `rsyslog`, or `logrotate` configuration on production systems without a rollback plan.
- Forwarding logs that contain secrets, tokens, personal data, or customer content.
- Expanding debug logging without checking disk capacity and rotation behavior.
- Sharing full logs externally when a focused redacted excerpt would answer the question.

## Practice Path

For the hands-on work in this chapter, use a disposable VM or lab host. Create a short lab note with:

- The question you are investigating.
- The time window you searched.
- The commands you ran.
- The log lines or counts that mattered.
- The next action you would recommend and why it is safe.

## Lessons in this Chapter

<!-- lesson-index:start -->

- [10.1 Log Locations](10.1_log_locations.md)
- [10.2 The systemd Journal](10.2_the_systemd_journal.md)
- [10.3 Syslog](10.3_syslog.md)
- [10.4 Kernel and Boot-time Logging](10.4_kernel_and_boot-time_logging.md)
- [10.5 Management and Rotation of Log Files](10.5_management_and_rotation_of_log_files.md)
- [10.6 Management of Logs at Scale](10.6_management_of_logs_at_scale.md)
- [10.7 Logging Policies](10.7_logging_policies.md)

<!-- lesson-index:end -->
