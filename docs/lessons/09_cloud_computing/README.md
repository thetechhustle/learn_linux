# Chapter 09: Cloud Computing

Cloud computing does not replace Linux administration. It changes where the machines live, how they are created, how access is granted, how costs appear, and how failures are investigated.

In earlier chapters, you learned how to inspect accounts, processes, filesystems, packages, scripts, and system configuration on a machine you can touch directly. In the cloud, you still need those skills, but they sit inside a larger operating model:

- instances are created from images and templates
- networks are software-defined
- storage can be attached, detached, snapshotted, and billed separately
- identity and access are controlled both inside Linux and through the cloud provider
- observability often lives outside the host
- small mistakes can create real spend

This chapter is about becoming useful and careful in that environment.

## Operator Principle

Treat cloud resources as real infrastructure with real blast radius. Before changing anything, know the account, region, resource name, owner, access path, cost impact, and rollback path.

## What Changes in the Cloud

On a local server, the boundary is often obvious: one machine, one disk, one network, one console.

In the cloud, the boundary is spread across several layers:

- **Provider account**: the AWS, Azure, Google Cloud, DigitalOcean, Linode, or other account that owns the resources.
- **Region and zone**: the physical cloud location where resources run.
- **Compute**: virtual machines, containers, serverless functions, and managed runtimes.
- **Network**: VPCs, subnets, security groups, firewalls, load balancers, DNS, and private links.
- **Storage**: boot disks, block volumes, object buckets, snapshots, backups, and database storage.
- **Identity**: Linux users and SSH keys plus provider IAM roles, groups, policies, and service accounts.
- **Billing**: usage meters, committed spend, storage retention, data transfer, and idle resources.

A good Linux operator learns to move between these layers without confusing them.

## What Stays the Same

Your Linux fundamentals still matter:

- `ssh` still gets you onto many systems.
- `systemctl status` still helps explain services.
- `journalctl` still tells you what happened on the host.
- `/etc/passwd`, `/etc/group`, and PAM still shape local login behavior.
- package managers still install and update software.
- shell scripts still automate repeatable work.
- logs, metrics, and process state still separate guesses from evidence.

The cloud adds more places to check. It does not remove the need to check the host.

## Chapter Map

### 09.1 The Cloud in Context

Cloud computing is a way to rent infrastructure and platform services through APIs. This lesson explains where cloud fits, what problem it solves, and why Linux skills remain central.

### 09.2 Cloud Platform Choices

Different providers have different strengths, pricing models, default networks, IAM systems, and managed services. This lesson helps you compare platforms without treating provider choice like a popularity contest.

### 09.3 Cloud Service Fundamentals

Compute, storage, networking, identity, databases, observability, and managed services form the basic cloud vocabulary. This lesson connects those concepts to the Linux operator's daily work.

### 09.4 Clouds: VPS Quick Start by Platform

Virtual private servers are the simplest cloud entry point. This lesson focuses on creating a small server, connecting safely, proving what changed, and avoiding common first-server mistakes.

### 09.5 Cost Control

Cloud resources are easy to create and easy to forget. This lesson covers budgets, alerts, idle resources, snapshots, data transfer, right-sizing, and cleanup habits.

### 09.6 Recommended Reading

Cloud tooling changes quickly. This lesson points to references worth checking when you need current provider-specific details.

## First Questions to Ask

Before touching a cloud system, ask:

- Which provider account am I in?
- Which region and project/subscription/account owns this resource?
- Is this production, staging, lab, or personal infrastructure?
- How do I get emergency console access if SSH breaks?
- How is access controlled: SSH keys, IAM, SSO, local users, or all of them?
- What will this cost if I leave it running?
- How will I prove the change worked?
- How will I roll it back?

These questions prevent expensive and embarrassing mistakes.

## Safe Practice Path

Use a small disposable lab account or low-cost VPS when practicing.

1. Create the smallest reasonable Linux server.
2. Record the provider, region, instance name, image, size, and estimated price.
3. Connect with SSH.
4. Run basic Linux inspection commands:

    ```bash
    hostnamectl
    ip addr
    df -h
    free -h
    systemctl --failed
    ```

5. Shut the resource down or destroy it when the lab is complete.
6. Check the provider console or billing view afterward to confirm cleanup.

Do not practice in a production account unless the task is explicitly approved.

## What Good Looks Like

By the end of this chapter, you should be able to:

- explain the difference between local Linux state and provider-managed cloud state
- create and inspect a small cloud server safely
- identify the access path for a cloud Linux host
- recognize common cloud service categories
- avoid leaving costly resources behind
- document cloud changes with enough detail for another operator to audit them

<!-- lesson-index:start -->

## Lessons in this chapter

- [The Cloud in Context](09.1_the_cloud_in_context.md)
- [09.2 Cloud Platform Choices](09.2_cloud_platform_choices.md)
- [09.3 Cloud Service Fundamentals](09.3_cloud_service_fundamentals.md)
- [09.4 Clouds: VPS Quick Start by Platform](09.4_clouds-_vps_quick_start_by_platform.md)
- [09.5 Cost Control](09.5_cost_control.md)
- [Recommended Reading](09.6_recommended_reading.md)

<!-- lesson-index:end -->
