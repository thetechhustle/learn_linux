## Chapter 04: Process Control

Process control is how you prove what is running, decide whether it is healthy, and intervene without making the incident worse. A production host can have hundreds of processes competing for CPU, memory, files, terminals, sockets, and scheduled execution time. Your job is to collect enough evidence to know which process matters and choose the smallest safe action.

This chapter builds the operator habits behind commands such as `ps`, `top`, `nice`, `renice`, `strace`, and `kill`. Treat those tools as an evidence workflow, not a bag of shortcuts: identify the process, understand its parentage and owner, inspect its resource use, confirm whether it is stuck or merely busy, and document any change you make.

## What you will be able to do

By the end of this chapter, you should be able to:

- Explain PID, PPID, UID, process state, priority, open files, and command line in operational terms.
- Use `ps`, `top`, and `/proc` to build a short evidence trail for a suspicious process.
- Distinguish normal CPU or memory use from a process that is stuck, runaway, orphaned, or waiting on I/O.
- Adjust scheduling priority with `nice` or `renice` only when it is safer than restarting or killing the process.
- Use tracing tools such as `strace` to observe system calls before guessing at a failure.
- Stop a process with the least disruptive signal that can solve the problem.
- Explain scheduled jobs well enough to troubleshoot missed or overlapping periodic work.

## A safe process-response pattern

Use this sequence when a process appears to be hurting a system:

1. Record the symptom: slow API, high load average, memory pressure, stuck deployment, missed job, or saturated disk I/O.
2. Identify candidates with read-only tools such as `ps`, `top`, `pgrep`, `systemctl status`, and `/proc/<pid>/status`.
3. Check ownership and blast radius: user, service unit, parent process, open files, network sockets, and whether the process is part of a larger application.
4. Prefer reversible changes: lower priority, pause a batch job, restart a supervised service, or stop only the confirmed process.
5. Verify after the action with the same metrics you used before the action.
6. Leave a handoff note that includes PID, command, owner, evidence, action taken, result, and any follow-up risk.

!!! warning "Avoid blind process killing"
    `kill -9` skips normal cleanup. Use it only after you understand the process, have tried a safer signal where appropriate, and know what data or service impact might follow.

## Chapter path

Start with process anatomy and lifecycle before using the tools that inspect or change live processes:

- **04.1 Components of a Process**: PID, parentage, ownership, files, and runtime context.
- **04.2 The Life Cycle of a Process**: creation, running, waiting, zombie, orphan, and termination states.
- **04.3 `ps`: Monitor Processes**: point-in-time process inspection and useful output fields.
- **04.4 Interactive Monitoring with `top`**: live CPU, memory, state, and priority evidence.
- **04.5 `nice` and `renice`: Influence Scheduling Priority**: safer use of scheduler priority controls.
- **04.6 The `/proc` Filesystem**: process and kernel facts exposed as files.
- **04.7 `strace` and `truss`: Trace Signals and System Calls**: system-call evidence for stuck or confusing programs.
- **04.8 Runaway Processes**: triage and response for resource-hungry processes.
- **04.9 Periodic Processes**: cron, anacron, and recurring job verification.

<!-- lesson-index:start -->

## Lessons in this chapter

- [04.1 Components of a Process](04.1_components_of_a_process.md)
- [04.2 The Life Cycle of a Process](04.2_the_life_cycle_of_a_process.md)
- [04.3 ps: Monitor Processes](04.3_ps-_monitor_processes.md)
- [Interactive Monitoring with top](04.4_interactive_monitoring_with_top.md)
- [04.5 Nice and Renice: Influence Scheduling Priority](04.5_nice_and_renice-_influence_scheduling_priority.md)
- [04.6 The `/proc` Filesystem: A Corridor of Information](04.6_the_-proc_filesystem.md)
- [04.7 strace and truss: Trace Signals and System Calls](04.7_strace_and_truss-_trace_signals_and_system_calls.md)
- [04.8 Runaway Processes](04.8_runaway_processes.md)
- [04.9 Periodic Processes: Master of Routine](04.9_periodic_processes.md)

<!-- lesson-index:end -->
