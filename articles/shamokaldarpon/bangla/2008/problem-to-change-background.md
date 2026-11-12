---
archive_id: shamokaldarpon-600
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 600
title: ডিসপ্লে প্রোপার্টিসের সাহায্যে ডেক্সটপের পটভুমি পরবির্তনে সমস্যা হলে
slug: problem-to-change-background
language: bn
status: publish
published_at: '2008-06-23T20:07:17'
published_at_gmt: '2008-06-23T14:07:17'
modified_at: '2009-11-18T12:04:09'
modified_at_gmt: '2009-11-18T05:04:09'
original_url: https://www.shamokaldarpon.com/600/problem-to-change-background
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Desktop
- Display Properties
- gpedit
- Group Policy
- Prevent Changing Wallpaper
- Registry
- Tips
- Wallpaper
- উইন্ডোজ
- টিপস
- ডিসপ্লে পোপার্টিস
- ডিসপ্লে প্রোপার্টিস
- রেজিষ্টি
content_hash: abc665ced560f1d2221661374b3bdf24f52e23174f901ffa914774c02d3b5e07
archived_at: '2026-11-12T08:34:46.394478+00:00'
---

অনেক সময় দেখা যায় ভাইরাসের কারণে ডিসপ্লে প্রোপার্টিসে গিয়ে ডেক্সটপের পটভুমির ওয়ালপেপার পরিবর্তন করা যাচ্ছে না। Display Properties এর Desktop সক্রিয় করা যায় বিভিন্ন ভাবে। নিচের দুটি পদ্ধতি অবলম্বন করতে পারেন।

![](http://mehdiakram.files.wordpress.com/2008/06/nochangingwallpaper.jpg)

**পদ্ধতি ১:** নিচের কোড নোটপ্যাডে লিখে ChangingWallPaper.reg নামে সেভ করুন এবং সেভ করা ফাইলটি চালু করুন। তাহলে সমস্যার সমাধান হবে।  
Windows Registry Editor Version 5.00  
[HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\policies\ActiveDesktop]  
“NoChangingWallPaper”=dword:00000000  
**পদ্ধতি ২:** রানে গিয়ে gpedit.msc লিখে এন্টার করলে Group Policy চালু হবে।এখানে Local Computer Policy এর User Configuration> Administrative Templates> Control Panel এ যান। এবার ডানের Prevent Changing Wallpaper এ দুইবার ক্লিক করে Setting ট্যাব থেকে Disabled অপশন বাটন নির্বাচন করে OK করুন।
