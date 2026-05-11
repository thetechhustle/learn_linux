## Chapter 13: TCP/IP Networking

Linux systems rarely fail in isolation. A server might be healthy locally while users still cannot reach the service because an address changed, a route disappeared, DNS points at the wrong host, a firewall blocks a port, or a cloud security group no longer matches the host policy. This chapter gives you a practical path for proving where a network problem starts and where it stops.

By the end of this chapter, you should be able to:

- Explain the TCP/IP layers that matter during Linux operations.
- Inspect interface addresses, routes, neighbor tables, sockets, DNS resolution, and packet flow with read-only commands first.
- Separate local host problems from upstream routing, name service, firewall, NAT, and cloud-network issues.
- Make small, reversible network changes and verify them before calling an incident resolved.
- Write a useful handoff note that includes the commands run, the evidence found, and the remaining uncertainty.

## Operator Workflow

Use a consistent troubleshooting order before changing configuration:

1. Confirm the symptom: source host, destination name or address, protocol, port, and exact error.
2. Check local interface state and addresses with commands such as `ip link`, `ip addr`, and `ip route`.
3. Verify name resolution separately from reachability with tools such as `getent hosts`, `dig`, or `resolvectl`.
4. Test the path and service separately with tools such as `ping`, `tracepath`, `ss`, `nc`, and `curl`.
5. Inspect host firewalls, NAT rules, and cloud network controls before assuming the application is broken.
6. Change one thing at a time, keep a rollback note, and re-run the same verification command.

Prefer read-only inspection until you know which layer is implicated. Commands that alter addresses, routes, firewall policy, DHCP state, or cloud networking can disconnect active sessions, so practice those changes in a VM or disposable lab network first.

## Lab Notes

For each lesson, keep a short note with:

- The host, interface, address, gateway, and DNS server you inspected.
- The command output that proves the current state.
- The expected packet path or service path.
- The smallest reversible test you performed.
- What changed after the test, and what you would hand off to the next operator.

## Common Failure Patterns

- The service is listening only on `127.0.0.1` instead of the intended interface.
- The default route points at the wrong gateway or is missing entirely.
- DNS returns an old address, but direct IP testing succeeds.
- A firewall allows inbound traffic on the host but the cloud security group blocks it first.
- DHCP or router advertisements changed the address after a reboot.
- NAT hides the real source address needed for logs or access rules.
- IPv6 is enabled, preferred by clients, and broken in a different way than IPv4.

<!-- lesson-index:start -->

## Lessons in this chapter

- [13.1 TCP/IP and Its Relationship to the Internet](13.1_tcp-ip_and_its_relationship_to_the_internet.md)
- [13.2 Networking Basics](13.2_networking_basics.md)
- [13.3 Packet Addressing](13.3_packet_addressing.md)
- [13.4 IP Addresses: The Gory Details](13.4_ip_addresses-_the_gory_details.md)
- [13.5 Routing](13.5_routing.md)
- [13.6 IPv4 ARP and IPv6 Neighbor Discovery](13.6_ipv4_arp_and_ipv6_neighbor_discovery.md)
- [13.7 DHCP: The Dynamic Host Configuration Protocol](13.7_dhcp-_the_dynamic_host_configuration_protocol.md)
- [13.8 Security Issues](13.8_security_issues.md)
- [13.9 Basic Network Configuration](13.9_basic_network_configuration.md)
- [13.10 Linux Networking](13.10_linux_networking.md)
- [13.11 FreeBSD Networking](13.11_freebsd_networking.md)
- [13.12 Network Troubleshooting](13.12_network_troubleshooting.md)
- [13.13 Network Monitoring](13.13_network_monitoring.md)
- [13.14 Firewalls and Network Address Translation](13.14_firewalls_and_nat.md)
- [13.15 Cloud Networking](13.15_cloud_networking.md)
- [13.16 Recommended Reading](13.16_recommended_reading.md)

<!-- lesson-index:end -->
