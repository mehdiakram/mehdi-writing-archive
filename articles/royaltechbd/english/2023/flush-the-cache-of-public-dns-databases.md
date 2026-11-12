---
archive_id: royaltechbd-3440
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 3440
title: Flush the cache of public DNS databases
slug: flush-the-cache-of-public-dns-databases
language: en
status: publish
published_at: '2023-11-13T12:39:00'
published_at_gmt: '2023-11-13T06:39:00'
modified_at: '2026-09-28T09:03:18'
modified_at_gmt: '2026-09-28T03:03:18'
original_url: https://www.royaltechbd.com/flush-the-cache-of-public-dns-databases/
author: Mehdi Akram
categories:
- Online
tags:
- cache
- DNS
- DNS cache
- Flush
- OpenDNS
- public DNS
content_hash: 275000b5bf9f9720afc8f8d55d5577361f2b254fee26a18c74c6bc983d34b0a9
archived_at: '2026-11-12T08:31:00.807751+00:00'
---

Another way to speed up DNS propagation is to flush the DNS cache from popular public databases like Google or OpenDNS. This ensures that these databases use the most recent version of your domain’s DNS records. Hence, it promotes both accurate search results and a positive customer experience.

**[Clear Google’s public DNS cache.](https://developers.google.com/speed/public-dns/cache)**  
To do that, navigate to [Google’s Public DNS console](https://developers.google.com/speed/public-dns/cache), type your domain with record type, then click the Flush cache button.

[![](https://www.royaltechbd.com/wp-content/uploads/2023/11/Google-Public-DNS-Flush-Cache.png)](https://www.royaltechbd.com/wp-content/uploads/2023/11/Google-Public-DNS-Flush-Cache.png)

By doing that, you are prompting Google to update its DNS cache with the present-day information.

**[Flush OpenDNS cache](https://cachecheck.opendns.com/)**  
OpenDNS has a large DNS cache database that improves your internet experience by streamlining DNS resolution. Thus, clearing the cache of this public DNS database for your domain name can help expedite propagation.

To flush the [OpenDNS cache](https://cachecheck.opendns.com/), simply enter your domain name and click the Check this domain button.

Screenshot of OpenDNS on how to flush OpenDNS cache  
OpenDNS checks whether your domain resolves with the same result for all locations and if it is a valid one. Then click the Refresh the cache button to update OpenDNS’ records database for your domain, which may take up to 20 seconds.

[![](https://www.royaltechbd.com/wp-content/uploads/2023/11/Flush-OpenDNS-cache.png)](https://www.royaltechbd.com/wp-content/uploads/2023/11/Flush-OpenDNS-cache.png)

Screenshot of the Refresh OpenDNS cache button for your domain to speed up DNS propagation  
Taking these steps ensures faster and smoother propagation for your domain name. Read further to learn how to check whether your domain has propagated correctly.

**[1.1.1.1’s Purge Cache](https://1.1.1.1/purge-cache/)**

[1.1.1.1’s Purge Cache](https://1.1.1.1/purge-cache/) tool allows you to refresh 1.1.1.1’s DNS cache for domain names. To refresh the cache for a domain name, enter the name for the domain below, pick the DNS record type and then hit the Purge Cache.

[![](https://www.royaltechbd.com/wp-content/uploads/2023/11/1.1.1.1s-Purge-Cache-tool.png)](https://www.royaltechbd.com/wp-content/uploads/2023/11/1.1.1.1s-Purge-Cache-tool.png)
