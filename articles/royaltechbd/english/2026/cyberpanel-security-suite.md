---
archive_id: royaltechbd-4004
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 4004
title: CyberPanel Security Suite – Ultimate Fail2ban & Security Manager for CyberPanel
slug: cyberpanel-security-suite
language: en
status: publish
published_at: '2026-02-26T23:24:45'
published_at_gmt: '2026-02-26T17:24:45'
modified_at: '2026-09-28T09:02:47'
modified_at_gmt: '2026-09-28T03:02:47'
original_url: https://www.royaltechbd.com/cyberpanel-security-suite/
author: S M Mehdi Akram
categories:
- Tools
tags:
- cpanel
- CyberPanel
- free
- github
- hosting panel
- open-souce
- Plugin
- security
content_hash: d2c68d7badbb80f2924bd0ecedd50280a1cf8bfa288b4fa42a42f1feeff763c6
archived_at: '2026-11-12T08:38:55.907965+00:00'
---

If you are managing servers using **CyberPanel** and **OpenLiteSpeed**, you know how crucial it is to secure your server against brute-force attacks and malicious bots. While CyberPanel is fantastic, managing Fail2ban via the terminal can be tedious and prone to errors.

Enter **CyberPanel Security Suite** — a powerful, open-source plugin developed by [S M Mehdi Akram](https://www.facebook.com/smmehdiakram) (from [Royal Technologies](https://royaltechbd.com/)). This plugin seamlessly integrates into the CyberPanel dashboard, giving you a beautiful, modern GUI to manage your server’s security effortlessly.

![](https://www.royaltechbd.com/wp-content/uploads/2026/02/Cyberpanel-Security-Suite.jpg)

## Key Features

- **✓ Beautiful Dashboard:** Real-time overview of active jails, total banned IPs, and Fail2ban service status directly within CyberPanel.
- **✓ Advanced Jail Manager:** View all your Fail2ban jails, check their current status, and see exactly how many IPs are currently blocked.
- **✓ Intuitive IP Management:** Easily search, manually ban, or instantly unban IP addresses with a single click. No more complex CLI commands.
- **✓ Live Log Viewer:** Read your `/var/log/fail2ban.log` directly from the interface with an auto-refreshing UI.
- **✓ CyberPanel 2.4.4+ Ready:** Fully compatible with the latest CyberPanel versions and its new HTML structure.
- **✓ 100% Native Feel:** Designed to look and feel exactly like a native CyberPanel module.

## Why You Need This Plugin

Out of the box, managing security on Linux servers requires constant terminal access. If an important client accidentally gets banned, SSH-ing into the server to unban them takes time. With the Security Suite, you can instantly search for their IP and click **“Unban”** right from your browser.

Furthermore, the upcoming features on the roadmap—like **GeoIP Analytics** and full **Country Blocking**—will make this the ultimate firewall extension for any CyberPanel administrator.

## How to Install (Takes 30 seconds)

Installation is completely automated. Just SSH into your server as `root` and run:

```
bash <(curl -s https://raw.githubusercontent.com/mehdiakram/cyberpanel-security-suite/main/install.sh)
```

The installer will automatically handle Fail2ban dependencies, register the Python module, inject the sidebar UI, and restart LiteSpeed. It’s safe and reversible!

Full code from **<https://github.com/mehdiakram/cyberpanel-security-suite>**
