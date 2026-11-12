---
archive_id: shamokaldarpon-851
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 851
title: যেকোন ফাইলের অটোরান সিডি তৈরী করুন
slug: autorun-for-all-applicatio
language: bn
status: publish
published_at: '2008-11-05T15:10:46'
published_at_gmt: '2008-11-05T09:10:46'
modified_at: '2008-11-05T15:10:46'
modified_at_gmt: '2008-11-05T09:10:46'
original_url: https://www.shamokaldarpon.com/851/autorun-for-all-applicatio
author: admin
categories:
- আমার দেশ
tags:
- Application
- Autorun
- CD
- DVD
- shellexe
- অটোরান
- সিডি
content_hash: e1ed4d4178cfadbedc12bff7a69bb65eaae6399623f2792b8e5e859c45bdbba2
archived_at: '2026-11-12T08:34:35.185576+00:00'
---

সিডি বা ডিভিডি চালু করলে পছন্দের প্রোগ্রাম খুলবে, এরকম অটোরান সিডি তৈরী করা যায় খুব সহজেই। স্বাভাবিকভাবে এক্সজিকিউটিভ ফাইলের অটোরান তৈরী করা হয়। যেমন আপনি যদি চান সিডি বা ডিভিডি রমে ডিক্স প্রবেশ করালে setup.exe ফাইলটি চলবে তাহলে নোটপ্যাডে  
[autorun]  
open = setup.exe  
লিখে autorun.inf নামে সেভ করে উক্ত সিডি বা ডিভিডিতে রেখে রাইট করলেই হবে।  
কিন্তু আপনি যদি চান সিডি বা ডিভিডিতে এক্সজিকিউটিভ ফাইলের পরিবর্তে ওয়ার্ড, এক্সেল, স্লাউড বা অন্য কোন ফাইল খুলেবে তাহলে উপরোক্ত পদ্ধতিতে কাজ হবে না। এজন্য <http://doiop.com/Autorun-for-all> থেকে shellexe.exe ফাইলটি ডাউনলোড করে নিন। এবার assignment.pps ফাইলটির জন্য নোটপ্যাডে  
[autorun]  
open = shellexe.exe assignment.pps  
লিখে autorun.inf নামে সেভ করুন। এবার assignment.pps, autorun.inf এবং shellexe.exe সহ সিডি/ডিভিডিতে রাইট করুন। এভাবে আপনি অনান্য ডকুমেন্ট, এইচটিএমএল বা অনান্য ফরম্যাটের ফাইলের অটোরান সিডি/ডিভিডি তৈরী করতে পারেন।
