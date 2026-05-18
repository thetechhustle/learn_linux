# Continuous Integration and Delivery

Continuous integration and delivery, usually shortened to CI/CD, is the
discipline of proving software changes before they reach users and moving those
changes through release steps in a repeatable way.

For Linux operators, CI/CD is not only a developer topic. It affects how
packages are built, how configuration is validated, how containers are produced,
how infrastructure changes are reviewed, how secrets are handled, and how
incidents are rolled back.

This chapter focuses on the operational side of CI/CD: what the pipeline says
should happen, what actually happened, and what evidence lets you trust or stop
a release.

!!! abstract "What this chapter covers"
    - The difference between continuous integration, delivery, and deployment.
    - How pipeline stages turn source changes into tested release artifacts.
    - How Jenkins and other automation systems coordinate jobs, agents, secrets,
      artifacts, logs, and approvals.
    - How containers make build and runtime environments more repeatable.
    - How to inspect failed jobs, blocked deployments, and unsafe release
      assumptions.

!!! success "Operator principle"
    A pipeline is an operating contract.

    It should show what changed, what was tested, what artifact was produced,
    where it was promoted, and what evidence supports the release decision.

## Why CI/CD matters to Linux operators

Manual release steps work until the system becomes busy, distributed, or
regulated. Then small differences between machines, shells, package versions,
credentials, and human habits start to create outages.

CI/CD reduces that drift by making common release steps explicit:

- fetch the source
- install dependencies
- run tests and linters
- build packages, images, or documentation
- publish versioned artifacts
- deploy to a controlled environment
- run smoke checks
- pause for approval when risk is high
- record logs, versions, and results

The point is not automation for its own sake. The point is a repeatable evidence
trail that lets the team move faster without guessing.

## CI, delivery, and deployment

The words are often used loosely, so keep these distinctions clear:

- Continuous integration means changes are merged frequently and automatically
  checked with tests or validation.
- Continuous delivery means the system can produce a deployable artifact and
  move it toward release with controlled promotion steps.
- Continuous deployment means passing changes can automatically reach users
  without a manual approval gate.

Many serious production systems use continuous integration and continuous
delivery, but keep a manual approval before production. That is still CI/CD.
The right gate depends on blast radius, confidence, compliance, and rollback
quality.

## What a pipeline proves

A good pipeline answers practical questions:

- Which commit or change set ran?
- Which tests passed, failed, or were skipped?
- Which artifact was produced?
- Which dependency versions were used?
- Which environment received the artifact?
- Who approved the risky step?
- Which logs explain a failure?
- How do we roll back or rerun safely?

If a pipeline cannot answer those questions, it may be automating work without
providing enough operational truth.

## Typical pipeline stages

Pipeline names vary, but the pattern is familiar:

1. Source checkout

    The system fetches the repository and identifies the commit, branch, tag, or
    pull request under test.

2. Dependency setup

    The job installs language packages, system packages, tools, or a container
    image needed for the build.

3. Static checks

    Linters, formatters, policy checks, type checks, secret scans, and
    configuration validators catch mistakes before runtime.

4. Tests

    Unit, integration, contract, smoke, and end-to-end tests prove different
    parts of the system.

5. Build

    The pipeline creates a package, binary, container image, documentation site,
    VM image, or other artifact.

6. Publish

    Artifacts are pushed to a registry, package repository, object store, or
    release page with a stable version.

7. Deploy or promote

    The artifact moves to staging, production, or another environment.

8. Verify

    Smoke checks, health checks, logs, metrics, and synthetic probes confirm the
    release is behaving as expected.

9. Rollback or follow-up

    If verification fails, the team restores a known-good version or records the
    next remediation step.

## What can go wrong

CI/CD failures usually fall into a few categories:

- the source changed, but the pipeline ran against the wrong ref
- dependencies changed outside the repository
- tests pass locally but fail in the pipeline environment
- secrets or credentials are missing, expired, or overexposed
- artifacts are built but not traceable to a commit
- deployments succeed but smoke checks fail
- rollback exists in theory but was never tested
- flaky tests hide real risk or train people to ignore failures
- build agents differ from production in important ways

The operator response is to collect evidence before rerunning blindly.

## First checks during a failed run

When a job fails, start with the facts:

- repository and branch
- commit SHA
- pipeline run ID
- failed stage and step
- exact error text
- runner or agent name
- recent changes to dependencies, secrets, or infrastructure
- whether the same commit passed before

For GitHub Actions, examples include:

```bash
gh run list --limit 10
gh run view <run-id> --log-failed
gh pr checks <pr-number>
```

For Jenkins, examples include:

```bash
curl -s "$JENKINS_URL/job/<job-name>/<build-number>/api/json"
```

Or inspect the build page, console log, agent, workspace, artifacts, and
environment variables through the Jenkins UI.

## Security and secrets

CI/CD systems often hold powerful credentials. Treat them as production
infrastructure.

Basic rules:

- never commit secrets to the repository
- avoid printing secrets in logs
- scope tokens to the narrowest permissions possible
- rotate credentials after exposure or role changes
- separate read-only validation tokens from deployment tokens
- require approvals for high-risk production changes
- know who can edit pipeline definitions

Pipeline configuration is code with operational power. A malicious or careless
pipeline change can exfiltrate secrets, publish bad artifacts, or deploy broken
software.

## What to read first

Use this chapter as a path from concepts to operations:

1. Start with **26.1 CI/CD Essentials** to learn the vocabulary and boundaries.
2. Read **26.2 Pipelines** to understand stages, jobs, artifacts, and evidence.
3. Read **26.3 Jenkins** to study a classic automation server and its operator
   concerns.
4. Read **26.4 CI/CD in Practice** to connect failures and release flow to
   real operational decisions.
5. Read **26.5 Containers and CI/CD** to see how image builds and repeatable
   environments fit into release systems.
6. Finish with **26.6 Recommended Reading** to build your own reference path.

## Hands-on practice

Use a lab repository, not a production service.

1. Create or inspect a simple pipeline that runs a lint check and build.
2. Record the commit SHA, run ID, failed or passed stage, and produced artifact.
3. Intentionally break a small check and read the failed logs.
4. Fix the change and confirm the same pipeline passes.
5. Write a short release note that includes source ref, artifact, tests, and
   rollback plan.

## Check your understanding

- What evidence proves which commit produced a release artifact?
- Why is continuous delivery different from continuous deployment?
- What information should you collect before rerunning a failed job?
- Why are CI/CD secrets especially sensitive?
- What would make you pause a pipeline before production promotion?

<!-- lesson-index:start -->

## Lessons in this chapter

- [26.1 CI/CD Essentials](26.1_ci-cd_essentials.md)
- [Subchapter: Pipelines](26.2_pipelines.md)
- [26.3 Jenkins: The Open Source Automation Server](26.3_jenkins-_the_open_source_automation_server.md)
- [CI/CD in Practice](26.4_ci-cd_in_practice.md)
- [26.5 Containers and CI/CD](26.5_containers_and_ci-cd.md)
- [26.6 Recommended Reading](26.6_recommended_reading.md)

<!-- lesson-index:end -->
