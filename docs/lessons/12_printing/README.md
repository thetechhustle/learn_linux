## Chapter 12: Printing

Printing looks old-fashioned until payroll checks, shipping labels, medical forms,
badges, classroom packets, or executive reports stop coming out of the printer.
Linux administrators do not need to love printers, but they do need to understand
the path from an application to a queue, from a queue to a print service, and from
that service to a networked device that may be out of paper, offline, filtered by
policy, or speaking a protocol the workstation cannot use.

This chapter focuses on CUPS, the Common UNIX Printing System, because it is the
standard printing layer on most Linux systems. CUPS receives jobs, tracks queues,
applies printer options, talks IPP and related protocols, and exposes both web and
command-line administration interfaces. When printing breaks, CUPS gives you the
evidence trail: queue state, job state, printer URIs, driverless IPP discovery,
logs, and error messages.

!!! abstract "What you will learn"
    - Explain how Linux print jobs move from applications to CUPS queues and printers.
    - Use CUPS commands and the web interface to inspect printers, jobs, and defaults.
    - Separate workstation, queue, driver, permission, and network causes during troubleshooting.
    - Make small, reversible changes when adding or repairing a printer.
    - Capture enough evidence to hand off a printing incident clearly.

!!! example "Field story"
    A finance team says the office printer works from macOS but not from Linux.
    The printer is online, Windows users can print, and the Linux users see jobs
    disappear without output. A useful administrator does not reinstall random
    packages first. They check the CUPS service, list queues, inspect job history,
    confirm the printer URI, test IPP reachability, review CUPS logs, and then
    change one thing at a time.

!!! success "Operator principle"
    Treat printing as a pipeline: application, queue, policy, filter, protocol,
    network path, and physical device. Find the failed stage before changing it.

## Why Printing Still Matters

Printing problems are usually cross-boundary problems. The symptoms may show up in
a desktop app, but the cause may be a stopped CUPS service, an old queue pointing
at the wrong IP address, a printer that moved VLANs, a missing color option, a
held job, a policy restriction, or a device that only accepts secure IPP.

That makes printing a good administration skill. It forces you to practice:

- reading service status before restarting things
- using both GUI and CLI evidence
- checking network reachability without assuming the network is healthy
- understanding defaults, permissions, and queue state
- documenting the exact printer, job, and error message

## The CUPS Mental Model

CUPS sits between user applications and printers.

1. An application submits a job.
2. CUPS places the job in a queue.
3. The queue applies defaults and policy.
4. CUPS filters or prepares the job as needed.
5. CUPS sends the job to the printer using a backend such as IPP, socket, LPD, or
   a local device backend.
6. The printer accepts, rejects, prints, holds, or errors the job.

For modern printers, driverless IPP is often the cleanest path. Older devices may
still require vendor drivers, PPD files, or legacy protocols. The operational
habit is the same either way: discover the queue, inspect its configuration, send
a small test job, and observe where the job changes state.

## Evidence You Should Collect

When someone reports a printing issue, collect facts before changing the setup.

Useful first questions:

- Which host or user is affected?
- Which printer or queue name is affected?
- Does the job appear in the queue?
- Does the job fail, hold, complete without output, or never submit?
- Does printing work from another OS, user, network, or application?
- Did the printer IP, hostname, access policy, driver, or CUPS package change?

Useful first commands:

```bash
systemctl status cups
lpstat -t
lpstat -p
lpstat -o
lpoptions -p PRINTER_NAME -l
journalctl -u cups --since "30 minutes ago"
```

For networked printers, also check reachability:

```bash
ping PRINTER_HOSTNAME_OR_IP
ippfind
ip route get PRINTER_IP
```

## What This Chapter Covers

- **12.1 CUPS Printing** introduces CUPS from the workstation side: installing or
  verifying the service, adding a printer, listing queues, setting defaults, and
  sending test jobs.
- **12.2 CUPS Server Administration** moves into shared service administration:
  configuration files, remote access, browsing, policy, logs, and safe service
  changes.
- **12.3 Troubleshooting Tips** gives you an incident workflow for stuck jobs,
  held queues, driver or filter failures, unreachable printers, and confusing
  completed-without-output cases.
- **12.4 Recommended Reading** points you toward CUPS, IPP, OpenPrinting, and
  distribution documentation that are worth keeping close.

## Safe Practice Environment

You can practice most of this chapter without touching a real office printer.

Good lab options:

- use a disposable VM
- install CUPS locally
- add a PDF or file-backed test printer if available
- inspect queues and service state
- submit harmless text jobs
- test commands without changing production queues

Avoid experimenting on a shared print server during business hours. Restarting
CUPS, deleting queues, changing defaults, or replacing drivers can disrupt other
people's work.

## Chapter Outcome

By the end of this chapter, you should be able to look at a Linux printing problem
and describe the next safe diagnostic step. You will know where CUPS keeps the
queue state, how to inspect jobs, how to send a small test page, and how to decide
whether the issue is local configuration, server policy, network reachability, or
the printer itself.

<!-- lesson-index:start -->

## Lessons in this chapter

- [12.1 CUPS Printing](12.1_cups_printing.md)
- [12.2 CUPS Server Administration](12.2_cups_server_administration.md)
- [12.3 Troubleshooting Tips](12.3_troubleshooting_tips.md)
- [12.4 Recommended Reading](12.4_recommended_reading.md)

<!-- lesson-index:end -->
