---
archive_id: shamokaldarpon-2409
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 2409
title: ব্রাউজারের Ctrl + Enter এর মান পরিবর্তন করা
slug: '%e0%a6%ac%e0%a7%8d%e0%a6%b0%e0%a6%be%e0%a6%89%e0%a6%9c%e0%a6%be%e0%a6%b0%e0%a7%87%e0%a6%b0-ctrl-enter-%e0%a6%8f%e0%a6%b0-%e0%a6%ae%e0%a6%be%e0%a6%a8-%e0%a6%aa%e0%a6%b0%e0%a6%bf%e0%a6%ac%e0%a6%b0'
language: bn
status: publish
published_at: '2010-10-11T21:14:25'
published_at_gmt: '2010-10-11T15:14:25'
modified_at: '2010-10-11T21:15:40'
modified_at_gmt: '2010-10-11T15:15:40'
original_url: https://www.shamokaldarpon.com/2409/%e0%a6%ac%e0%a7%8d%e0%a6%b0%e0%a6%be%e0%a6%89%e0%a6%9c%e0%a6%be%e0%a6%b0%e0%a7%87%e0%a6%b0-ctrl-enter-%e0%a6%8f%e0%a6%b0-%e0%a6%ae%e0%a6%be%e0%a6%a8-%e0%a6%aa%e0%a6%b0%e0%a6%bf%e0%a6%ac%e0%a6%b0
author: মেহেদী আকরাম
categories:
- টিপস এন্ড ট্রিকস
- ব্রাউজার
tags:
- Ctrl + Enter
- Domain
- Firefox
- Internet Explorer
- QuickComplete
- Tips
- ইন্টারনেট এক্সপ্লোর
- ফায়ারফক্স
- ব্রাউজার
content_hash: e7dcf3522b18edcb625742cbe3b6bb838b7c559729f4815f8f25c97930e02b5f
archived_at: '2026-11-12T08:34:50.676945+00:00'
---

ওয়েব ব্রাউজারে শর্টকাট হিসাবে Ctrl + Enter বেশ ব্যবহৃত হয়। সাধারণত এড্রেসবারে কোন শব্দ লিখে Ctrl + Enter চাপলে উক্ত শব্দের শুরুতে http://www. এবং শেষে .com চলে আসে। যা ওয়েবসাইটে প্রবেশের ক্ষেত্রে দারুন কাজে দেয়। তবে চাইলে Ctrl + Enter এর মান পরিবর্তন করে ডোমেইন .com এর পরিবর্তেন অন্য ডোমেইন ব্যবহার করা যায়।  
ফায়ারফক্স: মজিলা ফায়ারফক্সে Ctrl + Enter এর মান পরিবর্তন করতে এড্রেসবারে about:Config লিখে এন্টার করুন। এবার I’ll be careful, I promise! বাটনে ক্লিক করে Filter এ browser.fixup লিখে সার্চ করুন। এখন browser.fixup.alternate.suffix এ দুইবার ক্লিক করে যে ডোমেইন লিখবেন সেটিই Ctrl + Enter করলে ব্যবহৃত হবে।  
ইন্টারনেট এক্সপ্লোরার: ইন্টারনেট এক্সপ্লোরারে Ctrl + Enter এর মান পরিবর্তন করতে (Start>Run) রানে গিয়ে regedit লিখে এন্টার করুন। এবার রেজিস্ট্রি এডিটরের HKEY\_CURRENT\_USER\Software\Microsoft\Internet Explorer\Toolbar এ গিয়ে QuickComplete নামে একটি কী তৈরী করতে হবে। এরপরে উক্ত কীতে একটি String Value নিয়ে মান হিসাবে http://www.%s.net নিন। তাহলে ইন্টারনেট এক্সপ্লোরারে Ctrl + Enter চাপলে .net আসবে। চাইলে http://www.%s.net এর মান পরিবর্তন করে অন্য ডোমেইনও ব্যবহার করা যাবে।
