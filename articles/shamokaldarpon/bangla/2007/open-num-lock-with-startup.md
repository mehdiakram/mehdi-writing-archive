---
archive_id: shamokaldarpon-42
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 42
title: উইন্ডোজের শুরুতে নামলক চালু করা
slug: open-num-lock-with-startup
language: bn
status: publish
published_at: '2007-02-18T10:19:22'
published_at_gmt: '2007-02-18T04:19:22'
modified_at: '2012-10-31T11:47:13'
modified_at_gmt: '2012-10-31T05:47:13'
original_url: https://www.shamokaldarpon.com/42/open-num-lock-with-startup
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- NUM Lock
- NUMLOCK
- উইন্ডোজ
- নামলক
content_hash: a7251cf43b86bc17e204e00c5237e417a25ad929a5381f2ceb7268c5450a92d1
archived_at: '2026-11-12T08:35:08.321539+00:00'
---

উইন্ডোজ চালু হবার সময় সয়ংক্রিয়ভাবে নামলক চালু করতে পারেন রেজিস্টি সম্পাদনা করে বা ভিজুয়্যাল বেসিক স্ক্রিপ্ট ব্যবহার করে। প্রথমে স্টাট থেকে রান -এ ক্লিক করে regedit লিখে Ok করুন । উইন্ডোজ চালু হবার সময় নামলক চালু করতে হলে রেজিস্টি এডিটর থেকে HKEY CURRENT USERControl PanelKeyboard এ InitialKeyboardIndicators অথবা ওয়েলকাম স্ক্রিনের সময় নামলক চালূ করতে হলে HKEY USERS.DEFAULTControl PanelKeyboard এ InitialKeyboardIndicators তে ভ্যালু ২ দিন। ০ দিলে নামলক বন্ধ অবস্থায় চালু হবে।

এছাড়াও ভিজুয়্যাল বেসিক স্ক্রিপ্ট ব্যবহার করে নামলক চালু করা যায়। এ জন্য নোটপ্যাডে নিচের সংকেত লিখুন

set WshShell = CreateObject(“WScript.Shell”)  
WshShell.SendKeys “{NUMLOCK}”

এবং NumLock.vbs নামে সেভ করুন। এবার উক্ত সেভ করা ফাইলটি স্টাট মেনু এর প্রোগ্রামসে থাকা Startup ফোল্ডরে কপি করে রাখলে উইন্ডোজ চালূ হবার সময় উক্ত ফাইল চালু হলে নামলক চালু হবে।
