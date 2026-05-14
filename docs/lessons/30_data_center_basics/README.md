## Chapter 30: Data Center Basics

Linux work does not end at the shell prompt. Many Linux systems live in racks, draw power through redundant circuits, depend on cooling, connect through structured cabling, and sit behind physical security controls. A good operator understands enough of that environment to troubleshoot responsibly and ask the right questions during an incident.

This chapter introduces the physical side of infrastructure. You do not need to become a data center facilities engineer, but you should know what a rack unit is, why power paths matter, how heat affects reliability, what availability tiers promise, and which tools help operators find the right machine safely.

!!! abstract "What you will learn"
    - Read basic rack, power, cooling, reliability, and security language used around data centers.
    - Connect Linux operations to the physical environment that keeps servers online.
    - Recognize when a problem is not only a software problem.
    - Collect useful data center facts before escalating to facilities, networking, or hardware teams.

## Why Linux Operators Need Data Center Basics

A slow or unavailable Linux server might be caused by application code, kernel behavior, storage latency, network congestion, or bad configuration. It might also be caused by:

- A server plugged into the wrong power path.
- A failed power supply.
- A hot aisle or blocked airflow path.
- A loose network cable.
- A mislabeled rack position.
- A failed top-of-rack switch.
- A maintenance event in the wrong availability zone or facility zone.

You do not fix all of these from the command line. You do, however, need enough context to describe the symptom clearly, avoid unsafe actions, and coordinate with the people who can touch the hardware.

## The Operator View of a Data Center

Think about a physical host as part of a chain:

```text
Application
  -> operating system
  -> server hardware
  -> rack
  -> power distribution
  -> cooling and airflow
  -> network cabling and switches
  -> facility security and operations
```

If any part of that chain is weak, the Linux system can suffer. A clean `systemctl status` output does not prove the rack has healthy power, and a healthy rack does not prove the application is working. You need both software and physical awareness.

## What to Record About a Server

When you operate physical or colocated Linux systems, keep a short inventory for each important host:

```text
Hostname:
Serial/service tag:
Rack:
Rack unit:
Power feed A:
Power feed B:
Switch/port:
Out-of-band management address:
Hardware owner:
Support contract:
Critical services:
```

This information saves time during outages. It also prevents dangerous mistakes, such as asking remote hands to pull the wrong cable or reboot the wrong server.

!!! warning "Physical actions need precision"
    A vague request like "reboot the Dell in rack 4" is risky. Use exact rack, unit, serial number, port, and maintenance context whenever someone will touch hardware.

## How This Chapter Is Organized

**30.1 Racks** explains how equipment is arranged physically, including rack units, mounting, cable discipline, labeling, and why exact location matters.

**30.2 Power** covers power distribution, redundant feeds, PDUs, power supplies, capacity planning, and the operational risk of plugging redundant devices into the same failure path.

**30.3 Cooling and Environment** introduces airflow, hot and cold aisles, temperature, humidity, blocked vents, and the way environmental problems can become Linux reliability problems.

**30.4 Data Center Reliability Tiers** explains reliability language, redundancy expectations, maintenance impact, and the difference between marketing claims and operational evidence.

**30.5 Data Center Security** covers physical access, visitor control, cages, cameras, asset handling, and why physical security is part of system security.

**30.6 Tools** introduces the tools and systems operators use to identify, access, and manage physical infrastructure: asset databases, labels, console access, out-of-band management, monitoring, and ticketing.

**30.7 Recommended Reading** gives you a practical reading path for continuing beyond this chapter.

## Common Data Center Questions

During real work, you may need to ask:

- Which rack and rack unit contains this server?
- Which switch port is connected to the host?
- Are both power supplies healthy?
- Are the redundant power feeds actually independent?
- Is the out-of-band management interface reachable?
- Is the rack in a hot spot?
- Is there a facility maintenance window in progress?
- Who is allowed to touch the hardware?

These questions are not distractions from Linux administration. They are part of running Linux responsibly when the system depends on physical infrastructure.

## Practical Scenario

Imagine users report that a database server became slow after a maintenance window. Linux metrics show high disk latency and occasional device errors. Before replacing the database or tuning the kernel, an experienced operator asks:

- Was the host moved?
- Were any cables reseated?
- Did a storage shelf, controller, or power path change?
- Are there hardware alerts in out-of-band management?
- Are other hosts in the same rack affected?

The right answer may involve Linux logs, storage tools, remote hands, asset records, and facilities notes. Data center basics help you connect those signals.

## Chapter Practice

As you work through this chapter, build a small inventory template for a lab server, home lab machine, or VM host. If you do not have physical hardware, use a hypothetical server and fill in the fields you would want during an outage.

Suggested fields:

```text
Host:
Purpose:
Location:
Power:
Network:
Remote access:
Owner:
Recovery notes:
```

The habit matters more than the exact format. Good operators leave behind enough context for the next person to act safely.

## Check Your Understanding

- Why can a Linux outage require data center information?
- What is risky about vague physical-hardware instructions?
- Why should redundant power supplies use independent power paths?
- How can poor cooling appear as a Linux reliability problem?
- What inventory fields would you want before asking someone to reseat a cable?

<!-- lesson-index:start -->

## Lessons in this chapter

- [30.1 Racks](30.1_racks.md)
- [30.2 Power](30.2_power.md)
- [30.3 Cooling and Environment](30.3_cooling_and_environment.md)
- [30.4 Data Center Reliability Tiers](30.4_data_center_reliability_tiers.md)
- [30.5 Data Center Security: The Digital Armor 🛡️](30.5_data_center_security.md)
- [30.6 Tools](30.6_tools.md)
- [30.7 Recommended Reading](30.7_recommended_reading.md)

<!-- lesson-index:end -->
