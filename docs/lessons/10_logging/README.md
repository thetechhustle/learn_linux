# Chapter 10: Logging

Logs are operational evidence. They show what the system, kernel, services, applications, and users reported before, during, and after a problem.

A Linux operator does not read logs only after something breaks. Good logging habits help you verify changes, explain incidents, detect suspicious activity, protect audit trails, and hand off work clearly.

!!! abstract "What you will learn"
    - Find the main places Linux systems store logs.
    - Use the systemd journal and traditional syslog with a clear purpose.
    - Inspect kernel, boot, service, and application evidence.
    - Rotate logs without losing needed history.
    - Plan for centralized logging at scale.
    - Write logging policies that balance troubleshooting, security, privacy, and retention.

!!! example "Field story"
    A web service was restarted overnight and now users report intermittent errors. The service is running now, but that does not explain what happened.

    A good operator builds a timeline: deployment notes, `systemctl` state, journal entries, application errors, kernel messages, disk usage, load balancer health, and any upstream provider events. Logs turn "it was broken" into evidence.

!!! success "Operator principle"
    Logs are only useful when you know where they live, how long they are retained, what time zone they use, and which layer produced them.

## What logs can prove

Logs can answer questions like:

- When did a service start, stop, reload, or crash?
- Which config file or command changed behavior?
- Did the kernel report hardware, driver, memory, or filesystem trouble?
- Did authentication succeed or fail?
- Did a scheduled job run?
- Did an application return errors before users noticed?
- Did disk pressure, memory pressure, or dependency failure appear first?
- Did a request reach the host at all?

Logs are not perfect truth. They can be missing, delayed, rotated away, filtered, spoofed, or written in the wrong time zone. Treat them as evidence to compare with other evidence.

## The main logging layers

Linux logging usually spans several layers:

- Kernel logs: boot messages, drivers, hardware events, network events, filesystem warnings, and low-level errors.
- Service manager logs: `systemd` unit starts, stops, failures, restarts, and dependency behavior.
- Syslog-style logs: traditional text logs under `/var/log`.
- Application logs: service-specific files, structured JSON logs, web access logs, error logs, and job output.
- Authentication logs: SSH, sudo, login, and PAM-related events.
- Audit and security logs: explicit policy-driven events when audit tooling is enabled.
- Remote logs: centralized logging systems, SIEM tools, cloud logging, and provider audit logs.

When troubleshooting, avoid reading one log in isolation. Build a timeline across layers.

## First commands to know

Start with read-only inspection:

```bash
systemctl --failed
journalctl -p warning..alert --since "1 hour ago"
journalctl -u <service> --since "1 hour ago"
dmesg --ctime | tail -n 50
ls -lh /var/log
df -h /var/log
```

Common text-log inspection:

```bash
sudo tail -n 100 /var/log/syslog
sudo tail -n 100 /var/log/messages
sudo tail -n 100 /var/log/auth.log
sudo tail -n 100 /var/log/secure
```

Different distributions use different filenames. Debian and Ubuntu commonly use `/var/log/syslog` and `/var/log/auth.log`. RHEL-family systems commonly use `/var/log/messages` and `/var/log/secure`.

## Time matters

Logging work depends on time alignment.

Check the host clock:

```bash
timedatectl
date --iso-8601=seconds
```

When making an incident timeline, record:

- local time zone.
- UTC time, when available.
- service restart times.
- deployment times.
- user report times.
- provider event times.
- log retention window.

If two systems disagree about time, correlation becomes unreliable.

## What this chapter covers

### 10.1 Log locations

You will learn where Linux systems commonly store logs and how to inspect `/var/log` without assuming every distribution is the same.

Key operator questions:

- Which logs are local?
- Which logs are remote?
- Which logs are compressed or rotated?
- Which logs require privilege to read?
- Which logs belong to the service being investigated?

### 10.2 The systemd journal

You will learn how to use `journalctl` to inspect structured service and system events.

Key operator questions:

- Which unit produced the message?
- What happened before and after the failure?
- Is the journal persistent across reboots?
- Are you filtering by unit, priority, boot, or time range?

### 10.3 Syslog

You will learn the traditional syslog model, including facilities, priorities, local files, and forwarding.

Key operator questions:

- Which daemon receives syslog messages?
- Which file receives a facility or priority?
- Are messages forwarded to a central collector?
- Are local and remote logs consistent?

### 10.4 Kernel and boot-time logging

You will learn how to inspect kernel and boot evidence with `dmesg`, the journal, and boot-specific filters.

Key operator questions:

- Did the kernel report device, driver, memory, or filesystem errors?
- Did a problem start at boot or later?
- Are messages from the current boot or an older boot?

### 10.5 Management and rotation of log files

You will learn why logs grow, how rotation protects disk space, and how retention choices affect investigations.

Key operator questions:

- Are logs filling the filesystem?
- Is rotation configured?
- Are compressed logs still searchable?
- Does retention match operational and compliance needs?

### 10.6 Management of logs at scale

You will learn why larger systems centralize logs and how collection changes the troubleshooting workflow.

Key operator questions:

- Are logs collected from every host?
- Are application logs structured?
- Can you search by service, host, request ID, and time range?
- What happens when the collector is unavailable?

### 10.7 Logging policies

You will learn how to decide what to log, how long to keep it, who can read it, and what data should not appear in logs.

Key operator questions:

- Are secrets or personal data being logged?
- Who can read sensitive logs?
- How long are logs retained?
- Which logs are required for audit, security, or incident response?

## Logging during changes

Before changing a service, capture the current evidence:

```bash
systemctl status <service>
journalctl -u <service> --since "30 minutes ago"
df -h
```

After the change, capture new evidence:

```bash
systemctl status <service>
journalctl -u <service> --since "5 minutes ago"
```

For web services, include an application check:

```bash
curl -I http://127.0.0.1:<port>/
```

The handoff should say what changed, when it changed, what logs were checked, and what verification passed.

## Logging safety

Be careful with logs. They often contain sensitive data:

- usernames.
- IP addresses.
- tokens.
- request paths.
- email addresses.
- stack traces.
- database errors.
- customer data.

Do not paste raw sensitive logs into public tickets, chat rooms, or documentation. Redact secrets and personal data. Preserve enough context to troubleshoot without exposing more than necessary.

## Hands-on practice

Use a disposable VM, local lab machine, or container with `systemd` support where possible.

1. Pick one running service.
2. Check its current `systemctl` status.
3. Read the last hour of journal entries for that service.
4. Find the main `/var/log` files on the system.
5. Check whether `/var/log` has enough free space.
6. Write a short timeline from the evidence you found.

Example timeline:

```text
10:02 UTC: service restarted by systemd.
10:03 UTC: app logged database connection timeout.
10:04 UTC: kernel reported no disk or memory errors.
10:05 UTC: health endpoint returned HTTP 200 locally.
Conclusion: service recovered; next check is database connectivity and upstream dependency health.
```

## Check your understanding

- Why should you compare journal logs, application logs, and kernel logs during an incident?
- What is the difference between current boot logs and older boot logs?
- Why can log rotation make troubleshooting harder?
- What sensitive information should not be copied into a public ticket?
- What should a good log-based handoff include?

<!-- lesson-index:start -->

## Lessons in this chapter

- [10.1 Log Locations](10.1_log_locations.md)
- [10.2 The systemd Journal](10.2_the_systemd_journal.md)
- [10.3 Syslog](10.3_syslog.md)
- [10.4 Kernel and Boot-time Logging](10.4_kernel_and_boot-time_logging.md)
- [10.5 Management and Rotation of Log Files](10.5_management_and_rotation_of_log_files.md)
- [10.6 Management of Logs at Scale](10.6_management_of_logs_at_scale.md)
- [10.7 Logging Policies](10.7_logging_policies.md)

<!-- lesson-index:end -->
