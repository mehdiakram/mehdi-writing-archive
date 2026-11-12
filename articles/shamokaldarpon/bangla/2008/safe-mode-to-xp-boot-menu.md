---
archive_id: shamokaldarpon-383
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 383
title: বুট মেনুতে সেফ মুড যোগ করা
slug: safe-mode-to-xp-boot-menu
language: bn
status: publish
published_at: '2008-03-31T19:02:11'
published_at_gmt: '2008-03-31T13:02:11'
modified_at: '2023-11-01T09:54:10'
modified_at_gmt: '2023-11-01T03:54:10'
original_url: https://www.shamokaldarpon.com/383/safe-mode-to-xp-boot-menu
author: admin
categories:
- অপারেটিং সিস্টেম
tags:
- Boot Menu
- Safe Mode
- Tips
- উইন্ডোজ
- টিপস
- বুট মেনু
- সেফ মুড
content_hash: cc21a007c0b3d0282d1c1657d583be7b6b7ff3660e41415c317c85d446f1650b
archived_at: '2026-11-12T08:35:36.618170+00:00'
---

একাধিক অপারেটিং সিস্টেম থাকলে কম্পিউটার খোলার সময় বুট মেনুতে কোন অপারেটিং সিস্টেম চালু করবেন তা নির্ধারন করা যায়। আর আপনি যদি উক্ত অপারেটিং সিস্টেম (এক্সপির জন্য) সেফ মুডে খুলতে চান তাহলে F8 চেপে সেফ মুড নির্বাচন করে সেফ মুডে প্রবেশ করতে হয়। কিন্তু আপনি চাইলে বুট মেনুতে সেফ মুড যোগ করতে পারেন ফলে সহজেই উক্ত নির্দিষ্ট উইন্ডোজে সেফ মুডে প্রবেশ করতে পারবেন।  
এজন্য মাই কম্পিউটারে মাউসের ডান বাটন ক্লিক করে Properties এ ক্লিক করুন। এখন Advanced থেকে Start Up and Recovery এর Settings বাটনে ক্লিক করুন। এবার Edit বাটনে ক্লিক করলে boot.ini ফাইলটি নোটপ্যাডে খুলবে। এবার সবশেষে multi(0)disk(0)rdisk(0)partition(1)\WINDOWS=”Microsoft Windows XP Safe Mode” /safeboot:minimal /sos /bootlog লিখুন (যদি উইন্ডোজ সি ড্রাইভে হয়) এবং সেভ করুন। এবার কম্পিউটার রিস্টার্ট দিলে দেখা যাবে বুট মেনুতে নতুন Microsoft Windows XP Safe Mode নামে নতুন অপারেটিং সিস্টেম দেখাচ্ছে। এবার এটিতে ক্লিক করলে সি ড্রাইভের উইন্ডোজটি সেভ মুডে খুলবে।
