---
archive_id: royaltechbd-3525
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 3525
title: XAMPP specific port for specific folder
slug: xampp-specific-port-for-specific-folder
language: en
status: publish
published_at: '2024-01-04T19:31:21'
published_at_gmt: '2024-01-04T13:31:21'
modified_at: '2026-09-28T09:03:12'
modified_at_gmt: '2026-09-28T03:03:12'
original_url: https://www.royaltechbd.com/xampp-specific-port-for-specific-folder/
author: Mehdi Akram
categories:
- Tips
tags:
- apache
- ports
- Windows
- XAMPP
content_hash: 00b93271de88dd839bc6ba82fe8ed10dea7d7caf20d46f0d5906396c02238faa
archived_at: '2026-11-12T08:30:52.018600+00:00'
---

By default xampp ports are 80 and 443. If you have many project and want to setup project with difference port in xampp called “Virtual Hosts” this is how to setup virtual host in xampp for difference port.

[![](https://www.royaltechbd.com/wp-content/uploads/2024/01/xampp-1024x570.png)](https://www.royaltechbd.com/wp-content/uploads/2024/01/xampp.png)

Now we want to add port **81** for **C:\xampp\htdocs\whois**

Step 1 : Update **“C:\xampp\apache\conf\httpd.conf”** add new listening port. Add this line after **Listen 80**

```
Listen 81
```

Step 2: Update **“C:\xampp\apache\conf\extra\httpd-vhosts.conf”** add new virtual host config. If you want to

```
<VirtualHost *:81> 
    DocumentRoot "C:\xampp\htdocs\whois"
    ServerName 127.0.0.1:81
</VirtualHost>
```

Step 3 : Update **“C:\Windows\System32\drivers\etc\hosts”** add new host and port in this file. Add bellowe code after # ::1 localhost

```
127.0.0.1      127.0.0.1:81
```

Step 4 : Restart apache and test **127.0.0.1:81** in browser.
