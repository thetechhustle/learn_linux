# 16. DNS: The Domain Name System

DNS turns names into the addresses, mail exchangers, service records, and policy hints that keep Linux systems useful on a network. When DNS is wrong, healthy services look broken: logins pause, mail queues grow, TLS validation fails, package installs stall, and users report "the site is down" even when the web server is fine.

This chapter treats DNS as an operational system. You will learn how to separate resolver problems from authoritative-zone problems, collect evidence before changing records, and make DNS updates with rollback in mind.

## What You Should Be Able To Do

By the end of this chapter, you should be able to:

- Explain the roles of stub resolvers, recursive resolvers, root servers, TLD servers, and authoritative name servers.
- Use tools such as `dig`, `host`, `resolvectl`, `rndc`, `journalctl`, and packet captures to prove where a lookup succeeds or fails.
- Read common DNS records, including `A`, `AAAA`, `CNAME`, `MX`, `NS`, `SOA`, `TXT`, `SRV`, and reverse-lookup records.
- Plan DNS changes around TTLs, serial numbers, caching behavior, and client impact.
- Recognize risky DNS patterns such as lame delegations, broken glue, split-horizon surprises, stale zone data, open recursion, and DNSSEC validation failures.
- Troubleshoot BIND without masking the difference between configuration syntax, zone contents, resolver reachability, and firewall policy.

## Safe DNS Workflow

DNS changes are small text edits with large blast radius. Before editing a zone, changing resolver configuration, or restarting a name server, build a short evidence trail:

1. Identify the failing name, record type, expected answer, and affected clients.
2. Query the same name through the local stub resolver, the configured recursive resolver, and an authoritative server.
3. Check TTLs and caches so you know whether an old answer may persist after the fix.
4. Validate zone syntax and serial-number changes before reloading BIND.
5. Reload the smallest possible service scope, then repeat the same queries from multiple vantage points.
6. Record the previous value and the rollback command or zone edit before closing the change.

Prefer read-only commands first:

```bash
dig example.com A
dig @8.8.8.8 example.com A
dig +trace example.com
resolvectl status
named-checkconf
named-checkzone example.com /etc/bind/zones/db.example.com
```

Use packet captures carefully. Capture only the traffic you need, limit duration, and avoid sharing payloads that may expose internal hostnames or user activity.

## Lab Notes For This Chapter

For each lesson, keep a short note with:

- The hostname or zone you tested.
- The resolver or authoritative server you queried.
- The command you ran and the exact answer you expected.
- The TTL, status code, and authority section when they matter.
- The change you made or simulated.
- The verification command that proved the result.

Those notes become your incident handoff when DNS behavior differs between laptops, servers, cloud networks, and public recursive resolvers.

## Lessons In This Chapter

<!-- lesson-index:start -->

- [16.1 DNS architecture](16.1_dns_architecture.md)
- [16.2 DNS for lookups](16.2_dns_for_lookups.md)
- [16.3 The DNS namespace](16.3_the_dns_namespace.md)
- [16.4 How DNS works](16.4_how_dns_works.md)
- [16.5 The DNS database](16.5_the_dns_database.md)
- [16.6 The BIND software](16.6_the_bind_software.md)
- [16.7 Split DNS and the view statement](16.7_split_dns_and_the_view_statement.md)
- [16.8 BIND configuration examples](16.8_bind_configuration_examples.md)
- [16.9 Zone file updating](16.9_zone_file_updating.md)
- [16.10 DNS security issues](16.10_dns_security_issues.md)
- [16.11 BIND debugging](16.11_bind_debugging.md)
- [16.12 Recommended reading](16.12_recommended_reading.md)

<!-- lesson-index:end -->
