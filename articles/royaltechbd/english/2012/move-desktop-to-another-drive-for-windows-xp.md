---
archive_id: royaltechbd-450
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 450
title: Move Desktop to Another Drive for Windows XP
slug: move-desktop-to-another-drive-for-windows-xp
language: en
status: publish
published_at: '2012-06-11T17:16:44'
published_at_gmt: '2012-06-11T11:16:44'
modified_at: '2026-09-28T09:04:54'
modified_at_gmt: '2026-09-28T03:04:54'
original_url: https://www.royaltechbd.com/move-desktop-to-another-drive-for-windows-xp/
author: Mehdi Akram
categories:
- Tips
tags:
- Desktop
- Windows
- Windows XP
- XP
content_hash: 308a1051279fc80c8b5d11ecabd2f19e4f30c4a0172b838a0a473eae2ee5743c
archived_at: '2026-11-12T08:31:13.127353+00:00'
---

If you are using Microsoft Windows XP normally your desktop is in system folder (c:). For new XP setup user loss their data with desktop folder. To avoid loss data of Desktop you can change desktop location system drive to another drive.

**Method 1:**  
Now download the Tweak Ui Power toy from <http://windows.microsoft.com/en-US/windows/downloads/windows-xp> (Direct Link: <http://goo.gl/aB3jF>).  
After download install Tweak.  
Click My Computer and then Special Folders.  
Now click drop-down in right site in Special Folders and click Desktop.  
Now set a new desktop location and save (Yes).  
Now enjoy your desktop to another drive.

**Method 2:**  
Copy past the following code to notepad and save **Desktop.reg** name and run and marge registry. So your desktop location will set D:Desktop. You can set another location.  
[sourcecode language=”plain”]  
Windows Registry Editor Version 5.00  
[HKEY\_CURRENT\_USERSoftwareMicrosoftWindowsCurrentVersionExplorerShell Folders]  
"Desktop"="D:\Desktop"  
[/sourcecode]
