---
archive_id: shamokaldarpon-310
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 310
title: একসাথে একাধিক ম্যাসেঞ্জার খোলা
slug: multiple-messenger
language: bn
status: publish
published_at: '2008-02-24T00:18:32'
published_at_gmt: '2008-02-23T18:18:32'
modified_at: '2008-02-24T00:18:32'
modified_at_gmt: '2008-02-23T18:18:32'
original_url: https://www.shamokaldarpon.com/310/multiple-messenger
author: admin
categories:
- টিপস এন্ড ট্রিকস
- সফটওয়্যার রিভিউ
- হ্যাকিং / নিরাপত্তা
tags:
- Google
- Internet
- Massanger
- Tips
- Yahoo
- ইয়াহু
- গুগল
- টিপস
- ম্যাসেঞ্জার
content_hash: 33c1f7def647f2855862b21204f0169b691578316fd055d780b4da796686a6df
archived_at: '2026-11-12T08:34:30.697405+00:00'
---

সাধারণত একটি কম্পিউটার একসাথে একই ম্যাসেঞ্জার একাধিক খোলা যায় না। যেমন আপনি যদি ইয়াহু! ম্যাসেঞ্জারে লগইন করেন তাহলে আরেকটি আইডি ব্যবহার করতে নতুন আরেকটি ম্যাসেঞ্জার খুলতে পারবেন না। এমনই ভাবে গুগলেও একই সাথে একাধিক আইডি ব্যবহার করতে একাধিক ম্যাসেঞ্জার খোলা যায় না। আপনি যদি নতুন করে ম্যাসেঞ্জার খুলতে চান তাহলে পূর্বের খোলা ম্যাসেঞ্জারই চলে আসবে নতুন করে লগইন করার সুযোগ দেবে না। কিন্তু একটু ভিন্ন পন্থায় আপনি একাধিক আইডি ব্যবহার করতে একই সাথে একই কম্পিউটার ম্যাসেঞ্জার খুলতে এবং লগইন করে চ্যাটিং করতে পারবেন। ![yahoomessenger.jpg](http://mehdiakram.files.wordpress.com/2008/02/yahoomessenger.jpg)

এজন্য ডেক্সটপে (বা অন্য কোথাও) আপনার ম্যাসেঞ্জারের আরেকটি শর্টাকাট কপি তৈরী করুন এবং মাউসের ডান বাটন ক্লিক করে Properties এ ক্লিক করুন। এবার Target এর টেক্সট বক্সের শেষে /nomutex লিখুন। এরপরে নোটপ্যাড খুলুন এবং নিচের সংকেত লিখে YahooPlural.reg নামে নেভ করুন।

Windows Registry Editor Version 5.00  
[HKEY\_CURRENT\_USER\Software\yahoo\pager\Test]  
“Plural”=dword:00000001.

এবার YahooPlural.reg চালু করে নতুন তৈরী করা ইয়াহু! ম্যাসেঞ্জারের শর্টকাট চালু করুন এবং অন্য আরেকটি আইডি ব্যবহার করে লগইন করুন। একই ভাবে আপনি গুগলটক একাধিক খুলতে পারবেন।
