---
archive_id: royaltechbd-3501
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 3501
title: CyberPanel Cheatsheet
slug: cyberpanel-cheatsheet
language: en
status: publish
published_at: '2023-12-18T09:30:13'
published_at_gmt: '2023-12-18T03:30:13'
modified_at: '2026-09-28T09:03:14'
modified_at_gmt: '2026-09-28T03:03:14'
original_url: https://www.royaltechbd.com/cyberpanel-cheatsheet/
author: Mehdi Akram
categories:
- Tips
tags:
- CentOS
- Cheatsheet
- CyberPanel
- CyberPanel Cheatsheet
content_hash: 2aeccb12eec4127dce06a31ba22cb2871a71d19d327c6a5c37d638b8b4f0bf82
archived_at: '2026-11-12T08:30:52.562130+00:00'
---

A handy reference page for common CyberPanel commands and configurations.

I made a cheat sheet which is a list of the most common configurations that I deal with on CyberPanel servers. If you don’t find what you need here, check on CyberPanel [documentation](https://community.cyberpanel.net/docs) or [community](https://community.cyberpanel.net/).

[![](https://www.royaltechbd.com/wp-content/uploads/2023/12/CyberPanel-1024x597.png)](https://www.royaltechbd.com/wp-content/uploads/2023/12/CyberPanel.png)

**Change **CyberPanel** new website default page**

```
cd /usr/local/CyberCP
nano index.html
```

**Reset **CyberPanel** Admin Password**  
Change YOURNEWPASSWORD to your own

```
adminPass YOURNEWPASSWORD
```

**Remove CyberPanel two-step authentication**

```
sh <(curl https://raw.githubusercontent.com/mehdiakram/cyberpanel-tweaks/main/disable_2fa.sh || wget -O - https://raw.githubusercontent.com/mehdiakram/cyberpanel-tweaks/main/disable_2fa.sh)
```
