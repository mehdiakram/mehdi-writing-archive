---
archive_id: shamokaldarpon-1711
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 1711
title: ইউএসবি ডিভাইসের Safely Remove আইকন ফিরিয়ে আনা
slug: safely-remove-icon-for-usb-device
language: bn
status: publish
published_at: '2009-09-14T21:19:36'
published_at_gmt: '2009-09-14T14:19:36'
modified_at: '2012-10-05T23:05:23'
modified_at_gmt: '2012-10-05T17:05:23'
original_url: https://www.shamokaldarpon.com/1711/safely-remove-icon-for-usb-device
author: মেহেদী আকরাম
categories:
- টিপস এন্ড ট্রিকস
tags:
- Device
- Icon
- Missing
- Remove
- Safely
- Safely Remove
- System try
- Tips
- USB
- USB Drive
- আইকন
- ইউএসবি ডিভাইস
- উইন্ডোজ
- সিস্টেম ট্রে
content_hash: c375b043b8fd175d7e78a45406cc5acb7f843c8134076229f4b8385b0bafb502
archived_at: '2026-11-12T08:35:08.154713+00:00'
---

উইন্ডোজ অপারেটিং সিস্টেমে ইউএসবি ডিভাইস যুক্ত করলে সিস্টেম ট্রেতে Safely Remove আইকন থাকে। উক্ত আইকনে ক্লিক করে ইউএসবি ডিভাইসকে নিরাপদের সাথে বিযুক্ত করা হয়। কিন্তু কোন কারণে যদি ইউএসবি ডিভাইস সংযুক্ত করলে উক্ত আইকন না আসে তাহলে সরাসরি ডিভাইসটি খুলতে বাধ্য হতে হয়। কিন্তু সহজেই উক্ত Safely Remove আইকন ফিরে আনা যায়। এজন্য রানে (Start>Run) গিয়ে rundll32 shell32.dll,Control\_RunDLL hotplug.dll লিখে এন্টার করুন। ব্যস এরপর থেকে ইউএসবি ডিভাইস যুক্ত করলে সিস্টেম ট্রেতে Safely Remove আইকন আসবে।
