---
archive_id: shamokaldarpon-509
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 509
title: এ্যাড রিমুভ থেকে ইনষ্টল করা প্রোগ্রাম লুকিয়ে রাখা
slug: delete-programs-from-add-or-remove
language: bn
status: publish
published_at: '2008-05-15T17:43:42'
published_at_gmt: '2008-05-15T11:43:42'
modified_at: '2012-10-03T11:33:05'
modified_at_gmt: '2012-10-03T05:33:05'
original_url: https://www.shamokaldarpon.com/509/delete-programs-from-add-or-remove
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Add or Remove Programs
- Hide Program
- Tips
- এ্যাড রিমুভ
- টিপস
- প্রোগ্রাম লুকিয়ে রা
- রেজিষ্ট্রি এডিটর
content_hash: 2129da8cfebf1f062fd9548273ec1d1c9dae97cf386f1737b8147e48a997222d
archived_at: '2026-11-12T08:35:08.076264+00:00'
---

কোন প্রোগাম (সফটওয়্যার) ইনষ্টল করলে তা এ্যাড রিমুভে দেখা যায়, যেখান থেকে আনইনষ্টল করা যায়। আর সহজে বোঝা যায় সিস্টেমে কোন কোন প্রোগ্রাম ইনষ্টল করা আছে। কিন্তু আপনি চাইলে এ্যাড রিমুভ থেকে ইচ্ছামত কিছু প্রোগ্রাম লুকিয়ে রাখতে পারেন। এজন্য রেজিষ্ট্রি এডিটর (রানে গিয়ে regedit লিখে এন্টার করে) খুলে HKEY\_LOCAL\_MACHINE \ SOFTWARE \ Microsoft \ Windows \ CurrentVersion \ Uninstall এ যান। এবার যে প্রোগ্রামটি লুকিয়ে রাখতে চান সেটি নির্বাচন করে ডানের DisplayName এ দুইবার ক্লিক করে প্রোগ্রামটির নাম (ক্যাপশন) মুছে ফেলুন। তবে অনেক সময় এখানে কিছু কিছু প্রোগ্রামের নাম দেখা যায় না। তখন উপরের কোড নির্বাচন করে ডানের DisplayName নাম দেখে বুঝে নিন এবং DisplayName এর ক্যাপশন মুছে দিন। তাহলে সেটি আর এ্যাড রিমুভে তা দেখা যাবে না। আপনি চাইলে DisplayName এর ক্যাপশন মুছে অন্য নাম লিখে দিলে এ্যাড রিমুভে নতুন নাম দেখাবে।
