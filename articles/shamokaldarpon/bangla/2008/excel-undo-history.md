---
archive_id: shamokaldarpon-410
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 410
title: এক্সেলে আনডু বৃদ্ধি করা
slug: excel-undo-history
language: bn
status: publish
published_at: '2008-04-18T01:44:19'
published_at_gmt: '2008-04-17T19:44:19'
modified_at: '2012-10-03T11:33:18'
modified_at_gmt: '2012-10-03T05:33:18'
original_url: https://www.shamokaldarpon.com/410/excel-undo-history
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Excel
- Tips
- Undo
- আনডু
- এক্সেল
- এম এস অফিস
- টিপস
content_hash: 6895efa23185cd3d58d072ffeed301894f1c7053b1fda8e54d52a1bad2909a97
archived_at: '2026-11-12T08:35:08.082270+00:00'
---

কম্পিউটারে কাজ করার সময় ভুল ত্রুটি হলে আনডু করার প্রয়োজন হয়। মাইক্রোসফট এক্সেলে আনুমানিক ১৬ বার আনডু করা যায়। কিন্তু আপনি চাইলে এই আনডুর পরিমান বৃদ্ধি করা যায়। এজন্য নোটপ্যাড খুলে (অফিস এক্সপির ক্ষেত্রে)  
Windows Registry Editor Version 5.00  
[HKEY\_CURRENT\_USER\Software\Microsoft\Office\10.0\Excel\Options]  
“UndoHistory”=dword:00000040  
লিখুন ExcelUndo.reg এবং নামে সেভ করুন। এবার ExcelUndo.reg চালু করলে রেজিষ্ট্রি পরিবর্তন হবে তাহলে ৪০টি পর্যন্ত আনডু হবে। আপনি চাইলে আনডু আরো বেশী বা কম করতে পারেন। আপনি যদি অফিস ২০০০ এর জন্য করতে চান তাহলে নোটপ্যাডে 10.0Gi 9.0 পরিবর্তে লিখুন।
