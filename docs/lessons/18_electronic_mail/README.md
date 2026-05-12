# Chapter 18: Electronic Mail

Email is old infrastructure, but it is still one of the most important services a Linux administrator touches. It carries password resets, alerts, invoices, customer messages, cron output, monitoring notifications, and automated reports. When mail breaks, the symptoms often show up outside the server first: users stop receiving messages, alerts disappear, a domain starts landing in spam, or a vendor rejects messages from your application.

This chapter treats email as an operational system, not just a protocol history lesson. You will learn how messages move between clients, transfer agents, delivery agents, mailboxes, DNS records, spam controls, encryption layers, aliases, and common Linux mail servers. The goal is to give you enough structure to troubleshoot a real problem without making random changes to a production mail host.

!!! abstract "What you will learn"
    - Explain the path an email takes from sender to recipient.
    - Identify the roles of MUAs, MTAs, MDAs, mailbox storage, DNS, and filtering systems.
    - Inspect headers, SMTP conversations, aliases, queues, and mail logs.
    - Distinguish local delivery problems from remote delivery, DNS, reputation, and filtering problems.
    - Compare Sendmail, Exim, and Postfix at a practical operator level.

!!! success "Operator principle"
    Email reliability is evidence work. Before changing configuration, collect the message ID, headers, queue state, DNS answers, server logs, and the exact rejection or delay reason.

## Why email administration is tricky

Email looks simple from the user's perspective: write a message, press send, wait for delivery. Behind that simple workflow is a chain of systems that must agree on identity, routing, policy, storage, and trust.

A delivery failure can come from many places:

- a local application using the wrong relay host
- a blocked outbound TCP/25 path
- an invalid recipient address or alias
- a full mailbox or permission problem
- a broken MX, SPF, DKIM, or DMARC record
- a remote server greylisting or rejecting the message
- a spam filter changing placement after successful delivery
- a TLS or certificate mismatch
- a mail queue stuck behind DNS or network failure

The useful habit is to separate "message was generated" from "message was accepted by the next hop" and "message reached the intended inbox." Each step has different evidence.

## The basic mail path

Most mail systems involve these components:

- **Mail User Agent (MUA):** the client a person uses, such as Thunderbird, Apple Mail, Outlook, webmail, `mutt`, or `mail`.
- **Mail Submission Agent (MSA):** the service that accepts outbound mail from authenticated users or applications, usually on port 587.
- **Mail Transfer Agent (MTA):** the server that routes mail between systems. Common Linux MTAs include Postfix, Exim, and Sendmail.
- **Mail Delivery Agent (MDA):** the local component that places accepted mail into a mailbox or hands it to filtering tools.
- **Mailbox store:** the place mail is stored, such as mbox, Maildir, or a server-side IMAP-backed store.
- **DNS records:** MX, A/AAAA, PTR, SPF, DKIM, and DMARC records that help other systems route and evaluate mail.
- **Filtering and policy layers:** spam scanners, malware scanners, rate limits, blocklists, allowlists, and content rules.

When troubleshooting, draw the path first. A short diagram in your notes often saves more time than another command.

```text
sender or app
  -> submission service
  -> outbound MTA queue
  -> DNS lookup for recipient domain
  -> remote MTA
  -> remote filtering and delivery
  -> recipient mailbox
```

## What to inspect first

Start with read-only checks. The exact commands vary by distribution and MTA, but the evidence categories stay consistent.

```bash
# Identify the active mail service.
systemctl status postfix
systemctl status exim4
systemctl status sendmail

# Inspect recent mail logs.
journalctl -u postfix --since "30 minutes ago"
journalctl -u exim4 --since "30 minutes ago"

# Check the local queue for stuck messages.
mailq

# Inspect DNS routing for a recipient domain.
dig MX example.com
dig TXT example.com

# Test whether a remote SMTP service is reachable.
nc -vz mail.example.com 25
nc -vz mail.example.com 587
```

Do not treat these commands as a magic sequence. Use them to answer specific questions:

- Did the local system accept the message?
- Which queue ID or message ID identifies it?
- Which next hop did the MTA choose?
- Did DNS return the expected MX records?
- Did the remote server accept, defer, or reject the message?
- Was the final problem transport, policy, authentication, content, or mailbox storage?

## Safety habits

Mail servers can affect a whole organization, so make changes deliberately.

- Prefer a test recipient and a known message subject while debugging.
- Save the pre-change configuration before editing.
- Make one change at a time and record the evidence before and after.
- Avoid open-relay behavior; never accept unauthenticated third-party relay traffic.
- Be careful with DNS and reputation records because mistakes can affect every outbound message.
- Treat spam and malware controls as production security controls, not cosmetic filters.

## How this chapter is organized

The first lessons build the model: mail architecture, message anatomy, and SMTP. The middle lessons cover common operational risks: spam, malware, privacy, encryption, aliases, and Linux email configuration. The later lessons introduce the major Linux MTAs you are likely to encounter: Sendmail, Exim, and Postfix.

By the end of the chapter, you should be able to explain the mail path, inspect a message's evidence trail, recognize the difference between local and remote delivery failures, and choose the next troubleshooting step without guessing.

## Hands-on practice

Use a lab VM, container, or disposable test system for mail experiments. Avoid turning a public host into an internet-facing mail server until you understand relay policy, DNS, abuse controls, and monitoring.

1. Pick a test domain or lab hostname.
2. Identify which MTA, if any, is installed.
3. Send a local test message and capture the queue ID or log entry.
4. Inspect the message headers.
5. Look up MX and TXT records for a real domain.
6. Write a short delivery path note that separates local acceptance, routing, remote acceptance, and mailbox delivery.

## Check your understanding

- Why is "the email did not arrive" not specific enough for troubleshooting?
- What evidence proves that your local server handed a message to a remote server?
- How do MX records differ from SPF, DKIM, and DMARC records?
- Why is an open relay dangerous?
- When would you inspect headers instead of the mail queue?

<!-- lesson-index:start -->

## Lessons in this chapter

- [18.1 Mail System Architecture](18.1_mail_system_architecture.md)
- [Understanding an Email](18.2_anatomy_of_a_mail_message.md)
- [18.3 The SMTP Protocol](18.3_the_smtp_protocol.md)
- [18.4 Spam and Malware](18.4_spam_and_malware.md)
- [Sub-Chapter 18.5: Message Privacy and Encryption](18.5_message_privacy_and_encryption.md)
- [The Power of Mail Aliases](18.6_mail_aliases.md)
- [Setup of Email System on Linux](18.7_email_configuration.md)
- [18.8 Sendmail](18.8_sendmail.md)
- [18.9 Exim: The Flexible Mail Transfer Agent](18.9_exim.md)
- [18.10 Postfix: The Easy and Efficient MTA](18.10_postfix.md)
- [18.11 Recommended Reading](18.11_recommended_reading.md)

<!-- lesson-index:end -->
