---
archive_id: shamokaldarpon-142
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 142
title: ড্রাইভ নিয়ে লুকোচুরি
slug: hide-hard-disk-drive
language: bn
status: publish
published_at: '2007-11-06T22:23:59'
published_at_gmt: '2007-11-06T16:23:59'
modified_at: '2007-11-06T22:23:59'
modified_at_gmt: '2007-11-06T16:23:59'
original_url: https://www.shamokaldarpon.com/142/hide-hard-disk-drive
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Drive
- hard disk
- Hide
- উইন্ডোজ
- ড্রাইভ
content_hash: 8fb4f923249092c1e56df3011e4153d2d67d1624de999f7ac0f2c6a48f9f02c7
archived_at: '2026-11-12T08:34:26.777736+00:00'
---

নিরাপত্তা বা অনান্য সুবিধার কারণে আপনার কম্পিউটারের হার্ডডিক্সের ড্রাইভ হইতো লুকিয়ে রাখার প্রয়োজন হতে পারে। আপনি চাইলে খুব সহজেই আপনার কম্পিউটারের হার্ডডিক্সের যেকোন ড্রাইভ বা সকল ড্রাইভ লুকিয়ে রাখতে পারেন।  
পদ্ধতি ১: প্রথমে স্টার্ট মেনু থেকে রানে যান এবং gpedit.msc লিখে Ok করুন, তাহলে গ্রুপ পলিসি এডিটর খুলবে। এখানে User Configuration –> Administrative Templates –> Windows Components –> Windows Explorer এ যান এবং ডান দিকের Hide these specified drives in My Computer নির্বাচন করুন এবং দুইবার ক্লিক করে উইন্ডো খুলুন। এবার Setting ট্যাবে থেকে enable অপশন বাটন নির্বাচন করে নিচের ড্রপ ডাউন মেনু থেকে Restric all deives বা পছন্দমত ড্রাইভ নির্বাচন করে Apply এবং Ok করুন এবং মাই কম্পিউটার খুলে দেখুন উক্ত ড্রাইভ নেই। আবার উক্ত লুকানো ড্রাইভ ফিরে পেতে একইভাবে Setting ট্যাবে থেকে disable অপশন বাটন নির্বাচন করে Apply এবং Ok করলেই হবে।  
পদ্ধতি ২: www.mehdi-akram.tk ওয়েব সাইটে গিয়ে Hide Drive জিপ ডাউনলোড করে আনজিপ করুন। এবার যে ড্রাইভটি লুকাতে চান সেই রেজিষ্ট্রিটি রান করুন। এবান পুনরায় লগঅন কনে দেখুন উক্ত ড্রাইভটি নেই। আর ড্রাইভ ফিরিয়ে আনতে Recover All Hidden Drive রেজিষ্ট্রিটা চালালেই হবে।  
পদ্ধতি ৩: রানে গিয়ে regedit লিখে রেজিষ্টি এডিটর খুলুন। এবার HKEY\_LOCAL \_MACHINE \SOFTWARE \Microsoft \Windows \CurrentVersion\ policies \Explorer গিয়ে ডানের প্যানেলে মাউসের বাটন ক্লিক করে new নির্বাচন করে DWORD Value ক্লিক করুন এবং লিখুন NoDrive| এবার NoDrive দুইবার ক্লিক করে Value data অংশে ড্রাইভের মান দিন। (ড্রাইভ A=1, B=2, C=4, D=8, E=16, F=32, G=64, H=128, I=256 এভাবে পরবর্তী ড্রাইভের মান বের করতে পারেন। আপনি যদি দুটি বা তার বেশী ড্রাইভ একই সাথে লুকাতে চান তাহলে ঐ ড্রাইভগুলোর মান যোগ করে মোট মান লিখুন)। আবার ড্রাইভ ফিরিয়ে আনতে NoDrive মুছে দিলেই হবে।
