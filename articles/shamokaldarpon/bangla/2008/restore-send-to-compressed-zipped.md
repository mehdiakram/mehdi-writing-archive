---
archive_id: shamokaldarpon-824
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 824
title: সেন্ডটুতে কম্প্রেসড জিপড ফিরিয়ে আনা
slug: restore-send-to-compressed-zipped
language: bn
status: publish
published_at: '2008-10-10T18:54:32'
published_at_gmt: '2008-10-10T12:54:32'
modified_at: '2008-10-10T18:54:32'
modified_at_gmt: '2008-10-10T12:54:32'
original_url: https://www.shamokaldarpon.com/824/restore-send-to-compressed-zipped
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Compressed
- restore
- Send To
- Tips
- Zipped
- উইন্ডোজ
- কম্প্রেসড
- জিপড
- টিপস
- ফিরিয়ে আনা
- সেন্ডটু
content_hash: 5fd135d92010c268b50973479aa89f2ca8e6f141a44193d1cae1ed342c578766
archived_at: '2026-11-12T08:34:35.170820+00:00'
---

উইন্ডোজ এক্সপিতে সহজেই কোন ফোল্ডার বা ফাইলকে জিপ করা যায়। ফাইল বা ফোল্ডারের উপরে মাউসের ডান বাটন ক্লিক করে সেন্ডটু থেকে Compressed (zipped) Folder এ ক্লিক করলে সোর্স ফোল্ডারে জিপ ফাইল তৈরী হয়। কিন্তু কোন কারনে সেন্ডটু মেনু থেকে Compressed (zipped) Folder মুছে গেলে তা ফিরিয়ে আনা যায় না। তবে নিন্মাক্ত পদ্ধতিতে আপনি তা ফিরিয়ে আনতে পারেন। এজন্য রানে গিয়ে rundll32 zipfldr.dll,RegisterSendto লিখে এন্টার করুন তাহলে সেন্ডটুতে Compressed (zipped) Folder ফিরে আসবে।  
![](http://mehdiakram.files.wordpress.com/2008/10/compressedzippedfolder.png)
