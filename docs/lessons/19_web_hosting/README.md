## Chapter 19: Web Hosting

Web hosting turns a Linux system into an Internet-facing service. That sounds
simple until you operate it: DNS must point to the right place, HTTP and HTTPS
must behave correctly, the web server must survive traffic and bad requests,
certificates must renew, logs must be useful, and every exposed service becomes
part of the attack surface.

This chapter treats web hosting as an operations problem. The goal is not just
to install Apache or Nginx. The goal is to understand the request path, choose
the right serving model, configure it safely, verify it from outside the host,
and know where to look when users say the site is down.

!!! abstract "What you will learn"
    - Trace a request from DNS to the web server and back to the client.
    - Distinguish static hosting, reverse proxying, load balancing, and cloud
      hosting.
    - Compare Apache HTTPD, Nginx, and HAProxy by operational role.
    - Verify ports, TLS certificates, response headers, logs, and service
      health.
    - Apply a safe change workflow before exposing a site to the Internet.

## The web request path

A typical HTTPS request crosses several layers:

1. The user enters a hostname such as `www.example.com`.
2. DNS resolves the hostname to one or more IP addresses.
3. The client opens a TCP connection to port `443`.
4. TLS negotiates encryption and validates the certificate.
5. HTTP carries the request method, path, headers, and body.
6. A web server, reverse proxy, load balancer, or application handles the
   request.
7. The response travels back with a status code, headers, and body.

When a site fails, collect evidence at each layer instead of guessing:

```bash
dig www.example.com
curl -I https://www.example.com/
curl -vk https://www.example.com/
ss -ltnp | grep -E ':(80|443)\b'
systemctl status nginx apache2 httpd haproxy --no-pager
```

Each command answers a different question. DNS output does not prove the web
server is listening. A listening socket does not prove TLS works. A successful
local request does not prove the firewall or public DNS path works.

## Common hosting roles

Linux web hosts usually fit one or more of these roles:

| Role | What it does | Common tools |
| --- | --- | --- |
| Static file server | Serves HTML, CSS, JavaScript, images, and downloads | Nginx, Apache, object storage plus CDN |
| Application host | Runs application code behind an HTTP interface | systemd services, containers, app servers |
| Reverse proxy | Receives public requests and forwards to backend services | Nginx, Apache, Caddy, Traefik |
| TLS terminator | Handles HTTPS certificates and encryption | Nginx, Apache, HAProxy, load balancers |
| Load balancer | Distributes traffic across multiple backends | HAProxy, Nginx, cloud load balancers |
| Edge/cache layer | Caches responses near users or filters traffic | CDN, reverse proxy cache |

Do not choose software before choosing the role. A small static site, a Python
API, a WordPress host, and a multi-node SaaS app have different needs even if
they all use port `443`.

## Baseline evidence for a web host

Before changing a web server, capture the current state:

```bash
hostnamectl
ip addr
ip route
ss -ltnp
systemctl list-units --type=service --state=running
curl -I http://127.0.0.1/
curl -I https://127.0.0.1/ --insecure
```

Then inspect the public path:

```bash
dig A example.com
dig AAAA example.com
dig CNAME www.example.com
curl -I https://example.com/
curl -I https://www.example.com/
```

Save this evidence in your change notes. It gives you something concrete to
compare after editing configuration.

## Apache, Nginx, and HAProxy at a glance

### Apache HTTPD

Apache is a general-purpose web server with a long history, rich module
ecosystem, and flexible per-directory configuration. It is common for shared
hosting, PHP applications, and legacy sites.

Operator questions:

- Which virtual host serves this hostname?
- Are `.htaccess` files part of the configuration path?
- Which modules are enabled?
- Where are access and error logs written?

### Nginx

Nginx is commonly used as a static file server and reverse proxy. It handles
concurrent connections efficiently and has a clear server/location matching
model.

Operator questions:

- Which `server` block matched this hostname and port?
- Is the request served locally or proxied upstream?
- Are `Host`, `X-Forwarded-For`, and `X-Forwarded-Proto` passed correctly?
- Are upload limits, timeouts, and buffering appropriate?

### HAProxy

HAProxy is usually a load balancer or TCP/HTTP proxy rather than a full site
content server. It is strong when you need health checks, backend pools, and
explicit traffic routing.

Operator questions:

- Which frontend accepted the connection?
- Which backend and server were selected?
- Are health checks passing?
- Is TLS terminated at HAProxy or passed through to backends?

## DNS and TLS are part of hosting

A web server configuration is incomplete without DNS and TLS.

Check DNS:

```bash
dig A example.com
dig AAAA example.com
dig CAA example.com
```

Check certificates:

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null
curl -Iv https://example.com/
```

Check renewal timers if Let's Encrypt or another ACME client is used:

```bash
systemctl list-timers | grep -Ei 'certbot|acme|lego'
systemctl status certbot.timer --no-pager
certbot certificates
```

Certificate failures often look like web server failures to users. Treat
certificate inventory and renewal checks as part of normal hosting operations.

## Logs and status codes

HTTP status codes are operational signals:

| Status | Meaning | Common first check |
| --- | --- | --- |
| 200 | Request succeeded | Confirm content and headers are correct |
| 301/302 | Redirect | Check scheme and hostname redirect loops |
| 400 | Bad request | Inspect client, proxy, and header limits |
| 401/403 | Unauthorized or forbidden | Check auth rules, file permissions, allow/deny rules |
| 404 | Not found | Check routing, document root, app routes |
| 429 | Rate limited | Check proxy/app rate-limit rules |
| 500 | Application/server error | Check app and web server error logs |
| 502/504 | Bad gateway or timeout | Check upstream service, proxy settings, backend health |

Common log paths include:

```text
/var/log/nginx/access.log
/var/log/nginx/error.log
/var/log/apache2/access.log
/var/log/apache2/error.log
/var/log/httpd/access_log
/var/log/httpd/error_log
/var/log/haproxy.log
```

Systemd logs can fill in service-level failures:

```bash
journalctl -u nginx --since "30 minutes ago" --no-pager
journalctl -u apache2 --since "30 minutes ago" --no-pager
journalctl -u httpd --since "30 minutes ago" --no-pager
journalctl -u haproxy --since "30 minutes ago" --no-pager
```

## Safe change workflow

Use this workflow for production web hosting changes:

1. Capture current DNS, port, service, and HTTP evidence.
2. Back up the configuration file or commit the change in version control.
3. Edit the smallest relevant server, virtual host, frontend, or backend block.
4. Run the tool's configuration test:

    ```bash
    nginx -t
    apachectl configtest
    httpd -t
    haproxy -c -f /etc/haproxy/haproxy.cfg
    ```

5. Reload instead of restart when possible:

    ```bash
    systemctl reload nginx
    systemctl reload apache2
    systemctl reload httpd
    systemctl reload haproxy
    ```

6. Verify from the host and from outside the host.
7. Watch access logs, error logs, and backend health after the change.

## Lessons in this chapter

- [19.1 HTTP: The Hypertext Transfer Protocol](19.1_http-_the_hypertext_transfer_protocol.md)
- [19.2 Web Software Basics](19.2_web_software_basics.md)
- [19.3 Web Hosting in the Cloud](19.3_web_hosting_in_the_cloud.md)
- [19.4 Apache HTTPD](19.4_apache_httpd.md)
- [19.5 Nginx](19.5_nginx.md)
- [19.6 HAProxy](19.6_haproxy.md)
- [19.7 Recommended Reading](19.7_recommended_reading.md)

## Check your understanding

- Which commands would you run to prove DNS, TLS, and HTTP are all working?
- Why can a successful `curl http://127.0.0.1/` still leave a public site down?
- When would you use HAProxy instead of Nginx alone?
- What is the difference between a reload and a restart during a hosting
  change?
- Which logs would you inspect first for a `502 Bad Gateway` report?
