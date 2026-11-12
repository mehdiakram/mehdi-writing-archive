---
archive_id: royaltechbd-1513
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 1513
title: 'How to : FileZilla: ENETUNREACH – Network unreachable'
slug: how-to-filezilla-enetunreach-network-unreachable
language: en
status: publish
published_at: '2018-05-14T09:06:29'
published_at_gmt: '2018-05-14T03:06:29'
modified_at: '2026-09-28T09:03:29'
modified_at_gmt: '2026-09-28T03:03:29'
original_url: https://www.royaltechbd.com/how-to-filezilla-enetunreach-network-unreachable/
author: Mehdi Akram
categories:
- Tips
tags:
- File Zilla
- Filezilla
- ftp
- Kaspersky
content_hash: 947cf19be13328b5d4b10828e3f7b5e47c6f363d2b15dd53310d9632e49a0d64
archived_at: '2026-11-12T08:31:05.289106+00:00'
---

I was facing a problem when connecting fpt via Filezilla. The given error was the following:

> The data connection could not be established: ENETUNREACH – Network unreachable

Other fpt client was working fine but File zilla. I fount it turned out that the problem was related to the **Kaspersky** Antivirus TCP filter, which incorrectly behave with a File Zilla established connection breaking it out.

**Solution**  
Luckily enough this is a well-known problem on the FileZilla Project website, which even features a dedicated page explaining how to properly fix it. For your convenience, these are the required steps:  
Step 1: Double click on the Kasperskysystray icon (the red “K” near the system clock).  
Step 2: From the newly-opened windows, click on the “Settings” tab, then navigate to the “Anti-Virus protection” category.  
Step 3: In the new panel that will show, locate and click on “Firewall“.  
Step 4: To the right part of the new window, click to the “Application network rules…” button.  
Step 5: Click on the “Application” column to filter the items.  
Step 6: Browse the item list until you find “FILEZILLA PROJECT“: expand it by clicking to the “+” icon.  
Step 7: Click on the “filezilla.exe” entry: an info panel will appear.  
Step 8: Click on “Additional…” to show a new window, called “Application control rules“.  
Step 9: Click on the “Exclusions” tab and check the following options:  
**“Do not inherit restrictions of the parent process“** & **“Do not scan network traffic“**  
Now try to connect.
