---
archive_id: shamokaldarpon-1072
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 1072
title: সহজেই উইন্ডোজের পাসওয়ার্ড হ্যাক করা
slug: hack-windows-password
language: bn
status: publish
published_at: '2009-01-29T12:40:18'
published_at_gmt: '2009-01-29T06:40:18'
modified_at: '2023-11-01T09:53:43'
modified_at_gmt: '2023-11-01T03:53:43'
original_url: https://www.shamokaldarpon.com/1072/hack-windows-password
author: admin
categories:
- অপারেটিং সিস্টেম
tags:
- administrator
- Administrator Password
- Hack
- Hacking
- Password
- Tips
- Windows XP Hack
- XP
- উইন্ডোজ
- এ্যাডমিনিষ্ট্রেটর
- টিপস
- ডাউনলোড
- পাসওয়ার্ড
content_hash: 19bd195f0047129f963fe79faa96ff01e42cccab30f0cd8eebf999fb7b8408a1
archived_at: '2026-11-12T08:35:30.592909+00:00'
---

উইন্ডোজের পাসওয়ার্ড হ্যাক করা নিয়ে এর আগেও দুটা পোস্ট করেছি। তবে এটাই সবচেয়ে কার্যকর এবং সহজ পদ্ধতি।  
হ্যাকিং করতে হলে আপনার লাইভ অপারেটিং সিস্টেম দরকার হবে।  
আপনি [XP Live CD](http://www.shamokaldarpon.com/?p=675) বা [Slax Live CD](http://www.shamokaldarpon.com/?p=981) বা [Hiren Boot CD](http://www.shamokaldarpon.com/1964/hirensbootcd) দ্বারা কম্পিউটার বুট করুন।  
এবার সরাসরি যে ড্রাইভে উইন্ডোজ ইনস্টল করা আছে সেই ড্রাইভের উইন্ডোজের সিস্টেম৩২ ফোল্ডারে ঢুকে sethc.exe ফাইলকে রিনেম করে sethcold.exe করুন। এবার cmd.exe ফাইলকে কপি করে sethc.exe নামে রিনেম করুন। এবার কম্পিউটার রিস্টার্ট করুন লাইভ সিডিটি বের করে আগের উইন্ডোজে ঢুকুন। এবং কম্পিউটার লগঅন স্ক্রিন আসলে শিফট (Shift) কী পাঁচবার চাপুন তাহলে কমান্ড প্রোম্পট খুলবে।  
এখন এ্যাডমিনিষ্ট্রেটর এর পাসওয়ার্ড পরিবর্তন করতে net user administrator 2007 লিখুন তাহলে এ্যাডমিনিষ্ট্রেটর এর পাসওয়ার্ড পরিবর্তন হয়ে 2007 হয়ে যাবে।  
আর আপনি যদি পাসওয়ার্ড পরিবর্তন না করে নতুন ইউজার খুলতে চান তাহলে net user mehdi /add লিখে এন্টার করুন তাহলে mehdi নামে নতুন একটি ইউজার তৈরী হবে।  
এবার mehdi ইউজারকে এ্যাডমিনিষ্ট্রেটর হিসাবে ব্যবহার করতে হলে net localgroup administrator mehdi /add লিখুন এবং এন্টার করুন। তাহলে আপনার বর্তমান ইউজার (mehdi) এ্যাডমিনিষ্ট্রেটর হিসাবে ব্যবহার করা যাবে।  
একইভাবে বর্তমান ব্যবহার করা যে কোন লিমিটেড ইউজারকে এ্যাডমিনিষ্ট্রেটর হিসাবে ব্যবহার করতে পারেন।
