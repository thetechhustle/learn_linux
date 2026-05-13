# Chapter 25: Containers

Containers are a Linux operations topic before they are a developer convenience. A
container is still a process tree using the host kernel, filesystems, networks,
credentials, limits, logs, and security policy. The packaging is different, but
the troubleshooting still depends on evidence.

This chapter teaches containers as repeatable runtime environments. You will
learn what the container engine manages, what the host still owns, and how to
inspect a running container without treating it like a tiny virtual machine.

!!! abstract "What you will learn"
    - Explain how namespaces, cgroups, images, layers, registries, and runtimes
      fit together.
    - Compare containers with virtual machines and traditional service
      deployments.
    - Build, run, inspect, stop, and remove containers in a disposable lab.
    - Recognize common operational risks around tags, volumes, ports, secrets,
      privilege, resource limits, and stale images.
    - Describe when a single container is enough and when clustering or
      orchestration becomes part of the design.

!!! warning "Production caution"
    Containers make deployment repeatable, not automatically safe. Before you
    run a container on a real host, know which image you are using, who published
    it, what ports it exposes, what filesystems it mounts, which user it runs as,
    and what happens to its data when the container is replaced.

## The operating model

Most container incidents still reduce to familiar Linux questions:

- **Process:** What is running, which user owns it, and what signals stop it?
- **Image:** Which filesystem layers and application version produced this
  runtime?
- **Network:** Which ports are listening, where are they published, and what
  network namespace is involved?
- **Storage:** Is the data inside an ephemeral container layer, a bind mount, or
  a named volume?
- **Resources:** Are CPU, memory, process, and file descriptor limits visible
  and enforced?
- **Security:** Is the container privileged, running as root, or mounting host
  paths that increase blast radius?
- **Logs:** Where does standard output go, and what evidence survives a restart
  or replacement?

Treat those as your checklist when a containerized service behaves differently
from the same service installed directly on a host.

## A safe lab path

Use a disposable VM, cloud instance, or local lab machine. Do not use a shared
production host for first experiments.

1. Install or identify the container engine used by your lab environment.
2. Run a small, trusted image and record the exact image name and tag.
3. Inspect the container's process, network, logs, mounts, and resource settings.
4. Publish one port deliberately, test it locally, then stop the container.
5. Repeat the run with a named volume or bind mount and observe what data
   persists after replacement.
6. Remove the lab container and unused image only after you have captured your
   notes.

Useful evidence commands vary by engine, but the habit is the same:

```bash
docker ps
docker inspect CONTAINER
docker logs CONTAINER
docker stats --no-stream CONTAINER
docker image ls
docker volume ls
```

When Docker is not the local standard, map the same questions to Podman, nerdctl,
containerd tooling, or the platform your team operates.

## Common failure patterns

- The service works on a laptop because `latest` points to a different image
  than production.
- Data disappears because it was written to the container layer instead of a
  volume.
- A port is listening inside the container but was never published on the host.
- File permissions break because the container user does not match the mounted
  directory ownership.
- A container can consume too much memory because no limit was set or monitored.
- A restart loop hides the original error because logs were not collected soon
  enough.
- A privileged container or broad host bind mount turns an app bug into a host
  security problem.

## Hands-on practice

Create a short lab note with:

1. The image and tag you ran.
2. The command used to start the container.
3. The process, port, mount, and log evidence you collected.
4. One thing that persisted after replacement and one thing that did not.
5. One risk you would check before approving the same container for a shared
   environment.

## Check your understanding

- Why is a container not the same thing as a small virtual machine?
- Which parts of a containerized workload are still owned by the host?
- What evidence would you collect before restarting a failing container?
- Why are image tags, bind mounts, and privileged mode important review points?
- When would you move from a single container command to a compose file,
  service manager, or orchestrator?

<!-- lesson-index:start -->

## Lessons in this chapter

- [25.1 Background and Core Concepts](25.1_background_and_core_concepts.md)
- [25.2 Docker: The Open Source Container Engine](25.2_docker-_the_open_source_container_engine.md)
- [25.3 Containers in Practice](25.3_containers_in_practice.md)
- [25.4 Container Clustering and Management](25.4_container_clustering_and_management.md)
- [25.5 Recommended Reading](25.5_recommended_reading.md)

<!-- lesson-index:end -->
