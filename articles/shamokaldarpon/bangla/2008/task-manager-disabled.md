---
archive_id: shamokaldarpon-381
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 381
title: টাস্ক ম্যানেজার নিস্ক্রিয় হলে
slug: task-manager-disabled
language: bn
status: publish
published_at: '2008-03-30T08:22:09'
published_at_gmt: '2008-03-30T02:22:09'
modified_at: '2008-03-30T08:22:09'
modified_at_gmt: '2008-03-30T02:22:09'
original_url: https://www.shamokaldarpon.com/381/task-manager-disabled
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Registry
- Tips
- Virus
- উইন্ডোজ
- টিপস
- ভাইরাস
- রেজিষ্ট্রি
content_hash: 2ba1c64eede4401bc38d418298f0af2abdfea8937508a0b7a1aa5c37c23fb0c8
archived_at: '2026-11-12T08:34:30.907614+00:00'
---

![taskmanager.jpg](http://mehdiakram.files.wordpress.com/2008/03/taskmanager.jpg)ভাইরাসের কারণে অনেক সময় দেখা যায় টাস্ক ম্যানেজার ডিজেবল বা নিস্ক্রিয় হয়। ফলে টাস্ক ম্যানেজার খুলতে গেলে Task Manager has been disable by your asministrator মেসেজ আসে। বিভিন্ন ভাবে টাস্ক ম্যানেজার সক্রিয় করতে পারেন।  
**পদ্ধতি ১:** এজন্য নোটপ্যাড খুলে নিচের সংকেত লিখুন এবং TMEnabled.reg নামে সেভ করুন।  
Windows Registry Editor Version 5.00  
[HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System]  
“DisableTaskMgr”=dword:00000000  
এবার TMEnabled.reg ফাইলটি চালু করলে রেজিষ্ট্রি এডিট হবে এবং টাস্ক ম্যানেজার সক্রিয় হবে।  
**পদ্ধতি ২:** রানে গিয়ে REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG\_DWORD /d 0 /f লিখে এন্টার করলে রেজিস্ট্রি এডিট হবে এবং এবং টাস্ক ম্যানেজার সক্রিয় হবে।  
**পদ্ধতি ৩:** প্রথমে রানে গিয়ে gpedit.msc লিখে এন্টার করুন তাহলে গ্রুফ পলিসি চালু হবে। এবার User Configuration/Administrative Templates/System/Ctrl+Alt+Del Options থেকে Remove Task Manager এর উপরে মাউসের বাম বাটন দুইবার ক্লিক করে Disable বা Not Configured অপশন সিলেক্ট করে ওকে করুন এবং গ্রুফ পলিসি বন্ধ করুন। তাহলে টাস্ক ম্যানেজার সক্রিয় হবে।
