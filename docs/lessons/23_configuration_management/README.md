## Chapter 23: Configuration Management

Configuration management is how teams keep Linux systems predictable after the second, tenth, or thousandth host enters the picture. Instead of relying on memory, shell history, or a copied checklist, you describe the intended state of a system and keep that description under review.

This chapter is about the operational habit behind the tools: define what should be true, apply it safely, detect drift, and prove the result. Ansible, Salt, Puppet, and similar systems are useful only when the process around them is disciplined enough to avoid turning one mistake into a fleet-wide outage.

!!! abstract "What you will learn"
    - Explain why manual configuration stops scaling as fleets grow.
    - Identify the moving parts of a configuration management workflow: inventory, desired state, secrets, change review, execution, and verification.
    - Compare common configuration management systems without treating tool choice as the whole strategy.
    - Use Ansible and Salt examples to reason about repeatable changes, drift, and rollback planning.
    - Build safety checks that limit blast radius before changing many machines.

!!! warning "Production safety"
    Configuration management can fail faster than manual work. Test against disposable systems first, limit early runs to a small inventory group, review diffs or planned changes where the tool supports them, and keep rollback steps close to the change.

## Why configuration management matters

A single server can be managed carefully by hand. A fleet cannot. Small differences accumulate: package versions drift, one host misses a firewall rule, a service restart happens on one machine but not another, or an emergency fix never makes it back into documentation.

Configuration management gives operators a way to answer practical questions:

- What state do we expect this host to be in?
- Who reviewed the change that created that state?
- Which machines have received it?
- What evidence shows that the change worked?
- How do we recover if the change was wrong?

The goal is not automation for its own sake. The goal is repeatable, reviewable administration.

## The operator workflow

Most configuration management work follows the same pattern, regardless of tool:

1. **Inventory**: decide which hosts are in scope and how they are grouped.
2. **Desired state**: write down packages, files, users, services, scheduled jobs, and policy settings in a form the tool can apply.
3. **Review**: put the configuration in version control so changes can be discussed before rollout.
4. **Dry run or small rollout**: test the change against a lab system or a limited set of hosts.
5. **Apply**: run the tool with clear targeting and a known maintenance window when risk requires it.
6. **Verify**: collect evidence from commands, service health checks, logs, or monitoring.
7. **Correct drift**: compare actual state against desired state and fix differences intentionally.

## Common failure modes

Configuration management reduces some risks and introduces others. Watch for these patterns:

- **Overbroad targeting**: a playbook, state, or manifest runs against more hosts than intended.
- **Hidden dependencies**: one role assumes packages, users, secrets, or directories that another role creates.
- **Unreviewed secrets**: passwords, tokens, or private keys are committed to a repository instead of stored in a secret system.
- **One-way changes**: the automation can deploy a setting but has no rollback or recovery path.
- **Environment drift**: production differs from the lab enough that a tested change behaves differently.
- **Tool worship**: the team debates Ansible versus Salt while ignoring inventory quality, review discipline, and verification.

## Chapter path

The lessons build from concepts to tool-specific practice:

- **23.1 Configuration Management in a Nutshell** introduces desired state, drift, and repeatability.
- **23.2 Dangers of Configuration Management** focuses on blast radius, secrets, and unsafe automation.
- **23.3 Elements of Configuration Management** breaks down inventories, roles, modules, templates, variables, and change review.
- **23.4 Popular CM Systems Compared** compares the major tool families and their operational tradeoffs.
- **23.5 Introduction to Ansible** covers a practical entry point for agentless automation.
- **23.6 Introduction to Salt** introduces Salt's execution model and fleet-oriented design.
- **23.7 Ansible and Salt Compared** helps choose based on team skill, scale, network shape, and change frequency.
- **23.8 Best Practices** collects habits that make automation safer.
- **23.9 Recommended Reading** points to documentation and references for deeper work.

## Hands-on direction

Use a disposable VM or container for the first exercises. Practice making one small, reversible change, such as installing a package, managing a test file, or ensuring a harmless service state. Capture the before-and-after evidence and keep the automation in version control.

By the end of this chapter, you should be able to treat configuration as a controlled engineering artifact instead of a pile of remembered commands.

<!-- lesson-index:start -->

## Lessons in this chapter

- [23.1 Configuration Management in a Nutshell](23.1_configuration_management_in_a_nutshell.md)
- [23.2 Dangers of Configuration Management](23.2_dangers_of_configuration_management.md)
- [23.3 Elements of Configuration Management](23.3_elements_of_configuration_management.md)
- [23.4 Popular Configuration Management Systems Compared](23.4_popular_cm_systems_compared.md)
- [23.5 Introduction to Ansible](23.5_introduction_to_ansible.md)
- [23.6 Introduction to Salt](23.6_introduction_to_salt.md)
- [23.7 Ansible and Salt Compared](23.7_ansible_and_salt_compared.md)
- [23.8 Best Practices](23.8_best_practices.md)
- [23.9 Recommended Reading](23.9_recommended_reading.md)

<!-- lesson-index:end -->
