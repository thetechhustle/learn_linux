## Chapter 14: Physical Networking

Physical networking is where software abstractions meet cables, radios, switches, racks, and buildings. A Linux administrator does not need to become a low-voltage installer, but you do need enough physical-layer judgment to recognize when a server problem is really a link, wireless, switch, cabling, power, or design problem.

This chapter shifts from host TCP/IP behavior to the infrastructure that carries packets before they reach your kernel. You will learn how Ethernet and wireless behave, how structured cabling limits what a network can do, how SDN changes the control surface, and how to test the physical path without guessing.

!!! abstract "What you will learn"
    - Explain how Ethernet, wireless, cabling, and switching shape Linux network reliability.
    - Use physical-layer evidence before blaming services, DNS, firewalls, or cloud configuration.
    - Build a practical checklist for debugging links, ports, cables, access points, and switch paths.
    - Connect physical network design decisions to operations, documentation, vendors, and lifecycle management.

!!! success "Operator principle"
    Start with link evidence before chasing higher layers. If the cable, port, radio, VLAN, duplex, speed, or switch path is wrong, every elegant software diagnosis above it is built on sand.

## Why physical networking matters

When a host cannot reach the network, the visible symptom often appears at a higher layer:

- `ssh` times out.
- DNS lookups fail.
- A Kubernetes node becomes unreachable.
- A monitoring agent stops reporting.
- A storage mount freezes.
- A user says "the Wi-Fi is bad."

Those symptoms may come from routing, firewall, DNS, or application bugs, but they can also come from simple physical facts: a bad patch cable, a disabled switch port, a wrong VLAN, a flapping access point, a failed transceiver, dirty fiber, overloaded uplink, loose wall jack, or undocumented wiring change.

The fastest operators do not jump straight to one favorite command. They walk the path:

1. Is the interface present?
2. Is the link up?
3. What speed and duplex did the link negotiate?
4. Are error counters increasing?
5. Is the host on the expected VLAN or wireless network?
6. Does the switch or access point agree with the host's view?
7. Is the cable, optics, patch panel, or radio environment suspect?

## Chapter map

### Ethernet

Ethernet is the default language of wired networks. You will learn what matters operationally: link negotiation, MAC addresses, switching, VLANs, trunks, access ports, MTU, error counters, and why "plugged in" is not the same as healthy.

### Wireless

Wireless is Ethernet with radio physics, shared airtime, roaming, interference, authentication, and access-point placement added to the problem. You will learn how to separate weak signal, congestion, client behavior, and network design issues.

### SDN

Software-defined networking moves more network intent into controllers, APIs, overlays, and policy engines. The lesson is not "SDN is magic." The lesson is that you still need to trace packets through physical links, virtual switches, tunnels, and policy rules.

### Network testing and debugging

Testing physical networks requires evidence from both endpoints and infrastructure. You will use interface counters, switch-port data, cable tests, packet captures, path probes, logs, and controlled swaps to narrow the fault.

### Building wiring

Structured cabling is operational debt or operational leverage, depending on how well it is labeled, tested, documented, and maintained. This section covers practical wiring realities that affect Linux systems: patch panels, runs, closets, PoE, fiber, grounding, and capacity planning.

### Design and management

Physical networks need ownership. Address plans, VLANs, switch stacks, wireless coverage, out-of-band access, spare parts, firmware, diagrams, and change control all become production concerns.

## Linux evidence for physical-layer questions

Start with read-only checks on the host:

```bash
ip link show
ethtool eth0
ip -s link show dev eth0
networkctl status eth0
nmcli device show eth0
journalctl -k --grep='link\\|eth\\|enp\\|wlan'
```

For wireless clients, add:

```bash
iw dev
iw dev wlan0 link
nmcli dev wifi list
journalctl -u NetworkManager --since -1h
```

These commands answer practical questions:

- Did the kernel detect the interface?
- Is carrier present?
- What speed, duplex, and autonegotiation state were selected?
- Are receive, transmit, CRC, drop, or carrier counters increasing?
- Did the link flap recently?
- Is the wireless client associated with the expected SSID and access point?
- Is signal quality good enough for the workload?

!!! warning "Be careful with interface changes"
    Commands that change link state, MTU, VLANs, NetworkManager profiles, or switch configuration can disconnect your current session. When working remotely, prepare rollback access before changing the path you are using.

## A practical troubleshooting flow

Use this order when the symptom might be physical:

1. Confirm the affected host, interface, location, switch port, VLAN, and time window.
2. Check host link state and counters.
3. Check whether the switch or access point sees the same device and link state.
4. Swap the easiest reversible component first: cable, port, adapter, patch-panel position, or access point association.
5. Compare with a known-good host on the same path.
6. Capture packets only after basic link evidence is understood.
7. Record the final root cause in the network map or runbook.

The goal is not to replace network engineers. The goal is to bring them better evidence and avoid wasting time debugging Linux services when the physical path is broken.

## What good documentation looks like

For every production network segment, keep enough documentation that a new operator can answer:

- Which switch and port serves this host?
- Which VLAN or SSID should it use?
- What speed, duplex, MTU, and PoE expectations are normal?
- Where does the cable run terminate?
- Which uplink carries this traffic upstream?
- Which monitoring system records link status and errors?
- Who owns switch, wireless, cabling, and ISP changes?

Good physical network notes are boring by design. They turn emergencies into checklists.

## Lessons in this chapter

- [14.1 Ethernet: The Swiss Army Knife of Networking](14.1_ethernet-_the_swiss_army_knife_of_networking.md)
- [14.2 Wireless: Ethernet for Nomads](14.2_wireless-_ethernet_for_nomads.md)
- [14.3 SDN: Software-Defined Networking](14.3_sdn-_software-defined_networking.md)
- [14.4 Network Testing and Debugging](14.4_network_testing_and_debugging.md)
- [14.5 Building Wiring](14.5_building_wiring.md)
- [14.6 Network Design Issues](14.6_network_design_issues.md)
- [14.7 Management Issues](14.7_management_issues.md)
- [14.8 Recommended Vendors](14.8_recommended_vendors.md)
- [14.9 Recommended Reading](14.9_recommended_reading.md)
