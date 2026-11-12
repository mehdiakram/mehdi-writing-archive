---
archive_id: shamokaldarpon-136
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 136
title: সমস্যা যখন ফোল্ডার অপশন্সের
slug: folder-options-problem
language: bn
status: publish
published_at: '2007-11-04T21:41:58'
published_at_gmt: '2007-11-04T15:41:58'
modified_at: '2007-11-04T21:41:58'
modified_at_gmt: '2007-11-04T15:41:58'
original_url: https://www.shamokaldarpon.com/136/folder-options-problem
author: admin
categories:
- টিপস এন্ড ট্রিকস
- হ্যাকিং / নিরাপত্তা
tags:
- Tips
- Virus
- টিপস
- ভাইরাস
content_hash: 15eaa854a58653b803a56f4fc33ed9eb49b6ba51e4079ccadccdff12360478eb
archived_at: '2026-11-12T08:34:23.846843+00:00'
---

অনেক সময় ভাইরাস বা অনান্য কারণে আপনার কম্পিউটারের ফোল্ডার অপশন হারিয়ে যেতে পারে। সেক্ষেত্রে আপআকে বেশ বিপাকে পড়তে হয়। আপনার হিডেন করা ফোল্ডার/ফাইলগুলো প্রয়োজনের সময় হয়তো আর আন-হিডেন করে দেখতে পারছেন না বা হিডেন করা ফোল্ডার/ফাইলগুলো সর্বদা দেখা যাচ্ছে। এছাড়াও ফাইলের এক্সটেনশনগুলো দেখা যেতে পারে। এসব থেকে সহজেই মুক্তি পেতে পারেন। এজন্য [http://www.esnips.com/web/mehdiakramFreeDownload](http://www.esnips.com/doc/1245f0bb-cfe9-42a6-b626-5cd2c460a82a/RecoverFolderOptions) থেকে RecoverFolderOptions ফাইলটি ডাউনলোড করে নিন এবং চালু করুন। এরপর কম্পিউটার রিস্টার্ট হলে দেখবেন ফোল্ডার অপশন ফিরে এসেছে এবং অনান্য সমস্যাগুলোর সমাধান হয়ে গেছে।  
এছাড়াও ফোল্ডার অপশন ইচ্ছাকৃত লুকিয়ে রাখতে চাইলে রানে গিয়ে gpedit.msc লিখে ওকে করুন এবং গ্রুপ পলিসি এডিটরে User Configuration >> Administrative Templates >> Windows Components >> Windows Explorer যান। এবার ডান দিকের প্যানেল থেকে Removes the Folder Options menu from the Tools Menu দুইবার ক্লিক করে (Settings ট্যাবে থাকা অবস্থায়) অপশন Enable বাটন সিলেক্ট করে ওকে করুন। এবার দেখুন ফোল্ডার অপশনস নেই। আবার ফোল্ডার অপশনস ফিরিয়ে আনতে হলে Settings ট্যাব থেকে Not Configured সিলেক্ট করে থাকা ওকে করলেই হবে।
