---
archive_id: shamokaldarpon-299
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 299
title: স্টাট বাটনের নাম পরিবর্তন করা
slug: change-start-name
language: bn
status: publish
published_at: '2008-02-18T20:59:56'
published_at_gmt: '2008-02-18T14:59:56'
modified_at: '2008-02-18T20:59:56'
modified_at_gmt: '2008-02-18T14:59:56'
original_url: https://www.shamokaldarpon.com/299/change-start-name
author: admin
categories:
- টিপস এন্ড ট্রিকস
- হ্যাকিং / নিরাপত্তা
tags:
- Hack
- Start Button
- উইন্ডোজ
- বাটন
content_hash: f62deb464ef852e0d15161f2a74b55958cad43910aa11a5e22c319aae7e27c2d
archived_at: '2026-11-12T08:34:30.655068+00:00'
---

স্টাট বাটনের নাম পরিবর্তন করতে হলে উইন্ডোজের explorer.exe প্রোগ্রামটিকে সম্পাদনা করতে হবে। এজন্য Resource Hacker সফটওয়্যারটি www.users.on.net/johnson/resourcehacker থেকে ডাউনলোড করে নিন। উইন্ডোজের কোন রিসোর্স ফাইল পরিবর্তন করা ঝুকিপূর্ণ, তাই সতর্কতার সাথে এবং নিজ দায়িত্বে কাজ করতে হবে।  
প্রথমে Resource Hacker সফটওয়্যারটি খুলুন এবং ফাইল মেনু থেকে ওপেনে ক্লিক করে C:\Windows\explorer.exe (উইন্ডোজ যদি C: ড্রাইভে থাকে) ফাইলটি আনুন (এর আগে explorer.exe ফাইলটি ব্যাকআপ করে রাখুন)। এবার বাদিকের পেনে রিসোর্স তালিকা থেকে String Table ট্রিতে দুইবার ক্লিক করে ৩৭ ফ্লোডারে দুইবার ক্লিক করে ১০৩৩ ক্লিক করুন এবং ৫৭৮ কলামে start এর পরিবর্তে Mehdi (আপনার নাম) লিখুন এরপর Compile Script বাটনে ক্লিক করে কম্পাইল করুন এবং একই ভাবে এবার ৩৮ ফ্লোডারে দুইবার ক্লিক করে ১০৩৩ ক্লিক করে ৫৯৫ কলামে start এর পরিবর্তে Mehdi (আপনার নাম) লিখে Compile Script বাটনে ক্লিক করে কম্পাইল করুন। এবার C:\Windows এ Mehdiexplorer.exe নামে সেভ করুন। এখন স্টাট থেকে রান এ ক্লিক করে (start + R চেপে) regedit লিখুন এবং Registry Editor এ HKEY\_LOCAL\_MACHINE > SOFTWARE > Microsoft > Windows NT > CurrentVersion > Winlogon এবং ডানে Shell এ দুইবার ক্লিক করে explorer.exe পরিবর্তে Mehdiexplorer.exe লিখে OK করুন এবং Registry Editor বন্ধ করে কম্পিউটার রিস্টাট করুন।
