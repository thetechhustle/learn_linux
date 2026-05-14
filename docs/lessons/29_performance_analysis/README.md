## Chapter 29: Performance Analysis

Performance work is not guessing which knob makes a Linux system faster. It is the practice of proving where time, capacity, or reliability is being lost, then making the smallest change that improves the user-facing result.

A slow system can have many causes:

- CPU saturation or scheduler contention
- memory pressure, swapping, or OOM kills
- disk latency, full filesystems, or exhausted inodes
- network packet loss, retransmits, DNS delay, or connection backlog
- inefficient application code or database queries
- overloaded dependencies
- noisy neighbors in virtualized or cloud environments
- monitoring, backups, antivirus, or batch jobs competing with production work

This chapter teaches you how to move from complaint to evidence without making the system worse.

!!! abstract "What you will learn"
    - Build a disciplined performance investigation workflow.
    - Separate symptoms from bottlenecks.
    - Use Linux evidence to reason about CPU, memory, disk, network, and application behavior.
    - Decide when tuning is safe, when scaling is cleaner, and when the real fix belongs in the application.
    - Communicate performance findings clearly during an incident handoff.

!!! success "Operator principle"
    Measure first, change second, verify third. A performance change without before-and-after evidence is just a hunch.

## Performance analysis starts with the symptom

The first question is not "Which command should I run?" The first question is "Who is experiencing what?"

Useful symptom statements:

- Login takes 20 seconds after 09:00.
- The checkout API p95 latency rose from 300 ms to 2.8 seconds.
- Batch jobs that normally finish in 15 minutes now take 70 minutes.
- SSH is responsive, but the database query queue is growing.
- CPU is idle, but writes to `/var/lib/app` are slow.

Weak symptom statements:

- The server is slow.
- CPU looks weird.
- The app feels bad.
- Something is wrong with Linux.

Clear symptoms help you choose the first evidence path. A login delay, a web latency spike, and a slow disk write are different investigations.

## The performance loop

Use a repeatable loop:

1. Define the symptom and time window.
2. Check whether the problem is still happening.
3. Gather read-only evidence.
4. Identify the most likely bottleneck.
5. Make one low-risk change or mitigation.
6. Re-measure the same symptom.
7. Record the result and any follow-up.

For a first host snapshot:

```bash
date -Is
hostname
uptime
free -h
df -h
df -ih
ss -s
systemctl --failed
journalctl -p warning..alert -n 80 --no-pager
```

If performance tools are installed:

```bash
vmstat 1 5
iostat -xz 1 5
sar -u 1 5
```

These commands do not solve the problem by themselves. They help you decide where to look next.

## Symptoms are not bottlenecks

A symptom is what users or jobs experience. A bottleneck is the constrained resource or failing dependency behind that symptom.

Examples:

- Symptom: web requests are slow.
- Possible bottleneck: database latency, CPU saturation, DNS delay, queue backlog, disk I/O wait, external API timeout.

- Symptom: SSH login is delayed.
- Possible bottleneck: DNS lookup delay, PAM/SSSD dependency, high load, exhausted process table, disk pressure on logging.

- Symptom: batch jobs are late.
- Possible bottleneck: slower input source, CPU throttling, swap activity, serialized locks, storage latency, downstream rate limits.

Do not stop at the first busy graph. Tie resource pressure back to the symptom.

## Know the major resource lanes

Performance investigations usually start in one of these lanes.

### CPU

CPU problems are not only high percentages. Look for sustained load relative to CPU count, runnable queues, steal time, throttling, and whether the work is user CPU, system CPU, interrupts, or waiting on I/O.

First checks:

```bash
nproc
uptime
top
ps -eo pid,ppid,stat,pcpu,pmem,comm --sort=-pcpu | head
```

### Memory

Linux uses memory for cache, so "used memory" by itself is not a problem. Focus on available memory, swap activity, OOM events, and whether the application is growing unexpectedly.

First checks:

```bash
free -h
swapon --show
journalctl -k --grep='Out of memory|oom' --no-pager
ps -eo pid,ppid,stat,pmem,rss,comm --sort=-rss | head
```

### Disk and filesystems

Disk bottlenecks often look like high I/O wait, long request latency, full filesystems, exhausted inodes, or services blocked on reads and writes.

First checks:

```bash
df -h
df -ih
iostat -xz 1 5
dmesg --level=err,warn --ctime | tail -60
```

### Network

Network performance can fail through packet loss, retransmits, DNS delay, overloaded listeners, firewall state, route changes, or remote dependency timeouts.

First checks:

```bash
ip -s link
ss -s
ss -tulpn
resolvectl status
```

### Application and dependencies

Sometimes the Linux host is healthy and the application is slow because a queue is growing, a database plan changed, a cache is cold, or a dependency is failing.

First checks:

```bash
systemctl status app.service --no-pager
journalctl -u app.service -n 120 --no-pager
ss -tanp | head
```

Replace `app.service` with the real unit name. If the service runs in a container, inspect the container logs and health checks too.

## Tuning is not always the fix

There are several ways to improve performance:

- remove unnecessary work
- fix application behavior
- tune Linux or service configuration
- add capacity
- reduce contention
- move work to a better time
- cache carefully
- improve dependency behavior

Kernel and service tuning can help, but it can also hide the real issue. Raising limits may be correct when a limit is too low for expected load. It is not correct when it lets a broken process consume more of the machine.

Before tuning, write down:

```text
symptom:
evidence:
planned change:
expected result:
rollback:
verification command:
owner:
```

## Avoid common performance mistakes

- Changing several things at once.
- Tuning from a blog post without checking kernel, distribution, and workload fit.
- Treating averages as truth while p95 or p99 latency is bad.
- Ignoring time windows around deploys, backups, and traffic changes.
- Calling CPU high when the process is actually waiting on disk or network.
- Ignoring virtualized-host steal time.
- Forgetting to check full disks and inodes.
- Declaring victory without measuring the original symptom again.

## Chapter map

This chapter walks from philosophy to practical incident response:

- `29.1` explains performance tuning philosophy and why evidence comes first.
- `29.2` surveys the major ways to improve performance.
- `29.3` explains the factors that affect performance.
- `29.4` covers stolen CPU cycles and hidden compute contention.
- `29.5` gives a workflow for analyzing performance problems.
- `29.6` shows how to run a regular system performance checkup.
- `29.7` focuses on urgent "the server just got slow" triage.
- `29.8` points to deeper reading and reference material.

## Hands-on practice

Use a disposable VM or lab host.

1. Capture a baseline with `uptime`, `free -h`, `df -h`, `df -ih`, `ss -s`, and `systemctl --failed`.
2. Run `vmstat 1 5` and explain whether the host looks CPU-bound, memory-constrained, I/O-bound, or idle.
3. Find the top CPU and memory consumers with `ps`.
4. Write one symptom statement and one bottleneck hypothesis.
5. Write the rollback and verification plan you would use before changing a tuning value.

## Check your understanding

- Why should a performance investigation begin with a user-facing symptom?
- What is the difference between a symptom and a bottleneck?
- Why can "memory used" be misleading on Linux?
- What evidence would make you suspect disk latency instead of CPU saturation?
- Why is changing several tuning values at once risky?

<!-- lesson-index:start -->

## Lessons in this chapter

- [29.1 Performance Tuning Philosophy](29.1_performance_tuning_philosophy.md)
- [29.2 Ways to Improve Performance](29.2_ways_to_improve_performance.md)
- [29.3 Factors That Affect Performance](29.3_factors_that_affect_performance.md)
- [29.4 Stolen CPU Cycles](29.4_stolen_cpu_cycles.md)
- [29.5 Analysis of Performance Problems](29.5_analysis_of_performance_problems.md)
- [29.6 System Performance Checkup](29.6_system_performance_checkup.md)
- [29.7 Help! My Server Just Got Really Slow!](29.7_help!_my_server_just_got_really_slow!.md)
- [29.8 Recommended Reading](29.8_recommended_reading.md)

<!-- lesson-index:end -->
