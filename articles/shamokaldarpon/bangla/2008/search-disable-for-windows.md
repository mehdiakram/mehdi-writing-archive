---
archive_id: shamokaldarpon-865
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 865
title: উইন্ডোজে সার্চ অপশন নিস্ক্রিয় হলে করণিয়
slug: search-disable-for-windows
language: bn
status: publish
published_at: '2008-11-08T15:36:36'
published_at_gmt: '2008-11-08T09:36:36'
modified_at: '2012-10-31T11:55:33'
modified_at_gmt: '2012-10-31T05:55:33'
original_url: https://www.shamokaldarpon.com/865/search-disable-for-windows
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Disable
- Find
- Search
- Virus
- উইন্ডোজ
- ভাইরাস
- সার্চ
content_hash: ee3e9e7e1b82714b4f607e8a0ee631bfa8cd3d54ea72d530d00714e3d267e6d3
archived_at: '2026-11-12T08:35:08.346176+00:00'
---

ভাইরাস জনিত কারনে উইন্ডোজের স্টার্ট মেনু থেকে সার্চ অপশনটি হারিয়ে গেলে বেশ বিপাকে পরতে হয়। এর ফলে ফোল্ডারের মেনুতে সার্চ থাকলেও তা নিস্ক্রিয় অবস্থায় থাকে। এমতবস্থায় আপনার কম্পিউটারে ফাইল বা ফোল্ডার খোঁজার সুযোগ থাকে না। এ থেকে মুক্তি পেতে হলে রেজিষ্ট্রি এডিট করতে হবে। এজন্য রানে গিয়ে  
REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoFind /t REG\_DWORD /d 0 /f  
লিখে এন্টার করুন এবার কম্পিউটার রিস্টার্ট করুন। তাহলে সার্চ অপশন ফিরে আসবে।  
এতে কাজ না হলে রানে গিয়ে services.msc লিখে এন্টার করুন। এবার সার্ভিসেস থেকে Indexing Service নির্বাচন করে Stop করুন।  
এছাড়াও রানে গিয়ে regsvr32 urlmon.dll লিখে এন্টার করুন। এভাবে regsvr32 jscript.dll লিখে এবং regsvr32 wshom.ocx লিখে এন্টার করুন।
