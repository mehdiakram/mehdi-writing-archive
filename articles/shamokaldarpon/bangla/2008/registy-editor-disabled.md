---
archive_id: shamokaldarpon-386
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 386
title: রেজিস্ট্রি এডিটর নিস্ক্রিয় হলে
slug: registy-editor-disabled
language: bn
status: publish
published_at: '2008-04-01T19:52:41'
published_at_gmt: '2008-04-01T13:52:41'
modified_at: '2008-04-01T19:52:41'
modified_at_gmt: '2008-04-01T13:52:41'
original_url: https://www.shamokaldarpon.com/386/registy-editor-disabled
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Registry
- Tips
- Virus
- উইন্ডোজ
- টিপস
- ভাইরাস
- রেজিষ্ট্রি
content_hash: 75d3ce73408bbf4ee966d3ceabbead334fa610fcf4964be49f8d08c5aec21cce
archived_at: '2026-11-12T08:34:30.912640+00:00'
---

![regedit.jpg](http://mehdiakram.files.wordpress.com/2008/04/regedit.jpg)ভাইরাসের কারণে অনেক সময় দেখা যায় রেজিস্ট্রি এডিটর ডিজেবল বা নিস্ক্রিয় হয়। ফলে রেজিস্ট্রি এডিটর খুলতে গেলে Registry editing has been disable by your asministrator মেসেজ আসে। রেজিস্ট্রি এডিটর সক্রিয় করতে প্রথমে রানে গিয়ে gpedit.msc লিখে এন্টার করুন তাহলে গ্রুফ পলিসি চালু হবে। এবার User Configuration/Administrative Templates/System/Prevent access to registry editing tools এর উপরে মাউসের বাম বাটন দুইবার ক্লিক করুন। এখানে Enabled থাকলে Disable করুন। আর Not Configured থাকলে Enabled করে Apply করুন এবং Disable করুন এবং গ্রুফ পলিসি বন্ধ করুন। তাহলে রেজিস্ট্রি এডিটর সক্রিয় হবে।
