## Chapter 28: Monitoring

Monitoring is how operators know whether a system is healthy, degraded, or
failing. It turns Linux hosts, networks, applications, and security signals
into evidence that can be used before, during, and after an incident.

Good monitoring is not just a dashboard. It is a loop:

1. decide what matters
2. collect the right signals
3. store and query them reliably
4. alert on symptoms that require action
5. investigate with enough context to make a safe decision
6. improve the system after each failure

This chapter introduces that loop from a Linux administrator's point of view.

!!! abstract "What you will learn"
    - Explain the difference between metrics, logs, traces, events, and alerts.
    - Choose useful signals for hosts, networks, applications, and security.
    - Build monitoring habits that support incident response instead of creating noise.
    - Connect monitoring output to dashboards, runbooks, capacity planning, and post-incident review.

!!! success "Operator principle"
    Monitor symptoms users feel, causes operators can fix, and saturation points that predict the next failure.

## Why Monitoring Matters

Without monitoring, administrators work from guesses:

- users say "the site is slow"
- a cron job fails silently
- a disk fills overnight
- a certificate expires
- a database starts rejecting connections
- a compromised host sends traffic no one notices

Monitoring gives those stories timestamps, measurements, and context. It
helps answer:

- Is the service down or just slow?
- Is the problem local to one host or wider?
- Did this begin after a deployment, package update, traffic spike, or
  dependency failure?
- Are we running out of CPU, memory, disk, file descriptors, network, or
  database capacity?
- Did the fix actually improve the system?

The goal is not to collect every possible datapoint. The goal is to collect
enough useful evidence to detect trouble, diagnose it, and prevent repeat
failures.

## Core Signal Types

Monitoring systems usually work with several kinds of data.

**Metrics** are numeric measurements over time, such as CPU usage, memory
pressure, request rate, latency, error count, disk utilization, and queue
depth.

**Logs** are timestamped text or structured records that explain what
happened. System logs, web server logs, application logs, database logs, and
authentication logs all matter.

**Events** are notable changes, such as deployments, service restarts, backup
failures, security-group changes, node joins, and certificate renewals.

**Traces** show how one request moved through multiple services. They are
especially useful in distributed applications.

**Alerts** are notifications that require human or automated action. Alerts
should be rare enough to trust.

Each signal type answers a different question. Metrics show shape. Logs show
details. Events explain timing. Traces show path. Alerts decide when someone
must act.

## What Linux Operators Watch

At the host level, common monitoring areas include:

- CPU load, run queue, and steal time
- memory usage, swap, and out-of-memory events
- disk capacity, inode usage, I/O latency, and filesystem errors
- network throughput, errors, dropped packets, and listening ports
- service state, restarts, timers, and failed units
- package update status and reboot requirements
- authentication failures and privilege changes
- backup success, restore freshness, and replication lag

Useful local starting commands include:

```bash
uptime
free -h
df -h
df -ih
ss -tulpn
systemctl --failed
journalctl -p warning --since "1 hour ago"
```

These commands are not a replacement for a monitoring platform, but they
teach the same habit: look for saturation, errors, changes, and user-visible
impact.

## Alerts Need Judgment

An alert is a promise that someone should stop what they are doing and
respond. If alerts fire for normal behavior, people learn to ignore them.

Strong alerts usually have these traits:

- they describe a user-facing symptom or a clear operational risk
- they include the affected service, host, region, or customer path
- they point to a dashboard or runbook
- they include enough context to start triage
- they avoid waking people for conditions that self-resolve safely

Weak alerts usually say only "CPU high" or "disk warning" without explaining
whether anything is broken or what action is expected.

## Dashboards and Runbooks

Dashboards should answer questions quickly:

- Is the service available?
- Are users experiencing high latency or errors?
- Which dependency is unhealthy?
- Which host, region, deployment, or version changed?
- Are we approaching capacity limits?

Runbooks should turn those answers into action:

- what to check first
- where logs live
- which commands are safe and read-only
- which mitigations are reversible
- when to escalate
- how to record the incident handoff

Dashboards without runbooks can become wall art. Runbooks without current
signals become guesswork.

## Monitoring Culture

Monitoring is partly technical and partly cultural. Teams need habits that
make monitoring trustworthy:

- add or update monitoring when shipping a service
- review alerts that fired and alerts that should have fired
- delete noisy alerts instead of tolerating them forever
- keep incident notes linked to dashboards and logs
- measure recovery, not just failure
- test backups and restores, not just backup jobs
- treat monitoring gaps as real operational work

The best monitoring systems get better after every incident because the team
uses real failures to improve signals, thresholds, dashboards, and runbooks.

## Chapter Map

This chapter builds from concepts to practice:

- **28.1 An Overview of Monitoring** introduces monitoring vocabulary and
  operator goals.
- **28.2 The Monitoring Culture** explains habits that keep monitoring useful.
- **28.3 The Monitoring Platforms** compares common monitoring platform
  patterns.
- **28.4 Data Collection** covers how Linux monitoring data is collected and
  transported.
- **28.5 Network Monitoring** focuses on network reachability, throughput,
  errors, and path visibility.
- **28.6 Systems Monitoring** covers host health, capacity, and service state.
- **28.7 Application Monitoring** connects application behavior to Linux and
  platform signals.
- **28.8 Security Monitoring** covers authentication, integrity, suspicious
  activity, and audit evidence.
- **28.9 SNMP** explains where the Simple Network Management Protocol still
  fits.
- **28.10 Tips and Tricks for Monitoring** collects practical operator habits.
- **28.11 Recommended Reading** points to sources for deeper study.

## Hands-on Practice

Use a lab VM or non-production host.

1. Run the local commands listed above and record one observation from each.
2. Identify one signal that predicts a future problem, such as disk capacity
   growth or repeated service restarts.
3. Identify one signal that represents user impact, such as request errors or
   failed logins.
4. Draft one alert that would be worth waking an operator for.
5. Draft one dashboard question that the alert should link to.

## Check Your Understanding

- Why is "CPU is high" usually weaker than "checkout requests are failing"?
- What is the difference between a metric and a log?
- Why should deployments and service restarts be visible on dashboards?
- What makes an alert actionable?
- How can incident reviews improve monitoring over time?

<!-- lesson-index:start -->

## Lessons in this chapter

- [28.1 An Overview of Monitoring](28.1_an_overview_of_monitoring.md)
- [28.2 The Monitoring Culture](28.2_the_monitoring_culture.md)
- [28.3 The Monitoring Platforms](28.3_the_monitoring_platforms.md)
- [28.4 Data Collection: Interpreting the Language of Your Linux System 🌺📚](28.4_data_collection.md)
- [28.5 Network Monitoring: Spot the Intricacies from Miles Away 🌄🔭](28.5_network_monitoring.md)
- [28.6 Systems Monitoring](28.6_systems_monitoring.md)
- [28.7 Application Monitoring](28.7_application_monitoring.md)
- [28.8 Security Monitoring: Forge Your Shield and Sword](28.8_security_monitoring.md)
- [28.9 SNMP: The Simple Network Management Protocol](28.9_snmp-_the_simple_network_management_protocol.md)
- [🛠️28.10 Tips and Tricks for Monitoring🚀](28.10_tips_and_tricks_for_monitoring.md)
- [28.11 Recommended Reading](28.11_recommended_reading.md)

<!-- lesson-index:end -->
