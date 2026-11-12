---
archive_id: shamokaldarpon-2987
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 2987
title: এক্সপির ডেক্সটপকে অন্য ড্রাইভে রাখা
slug: move-windows-xp-desktop-to-another-drive
language: bn
status: publish
published_at: '2012-06-03T13:18:07'
published_at_gmt: '2012-06-03T07:18:07'
modified_at: '2023-11-01T09:53:09'
modified_at_gmt: '2023-11-01T03:53:09'
original_url: https://www.shamokaldarpon.com/2987/move-windows-xp-desktop-to-another-drive
author: মেহেদী আকরাম
categories:
- অপারেটিং সিস্টেম
tags:
- Desktop
- Tips
- XP
- উইন্ডোজ
- উইন্ডোজ এক্সপি
- এক্সপি
- ডেক্সটপ
content_hash: ab777328cfeea41291bc872fb8c1091a89e8783251a055c15e47d47be6afa2b2
archived_at: '2026-11-12T08:35:30.540327+00:00'
---

সাধারণত উইন্ডোজ এক্সপির ডেক্সটপ সি ড্রাইভে থাকে। ফলে কোন কারণে উইন্ডোজ নষ্ট হলে ডেক্সটপের ফাইলগুলো পাওয়া কষ্টকর হয়ে যায়। তবে যদি ডেক্সটপকে অন্য ড্রাইভের ফোল্ডার রাখা যায় তাহলে ডেক্সটপের ফাইলগুলো নিয়ে চিন্তা করতে হবে না। সি ড্রাইভ ফ্যরমেট দিলেও ডেক্সটপের ফাইল হারাবে না। এজন্য দরকার ছোট্ট একটি টুইক পাওয়ার টয় নামের সফটওয়্যার। এই Tweak Ui Power toy সফটওয়্যারটি <http://windows.microsoft.com/en-US/windows/downloads/windows-xp> থেকে (ডিরেক্ট লিংক: <http://goo.gl/aB3jF>) ডাউনলোড করে ইনস্টল করে নিন।  
সফটওয়্যারটি চালু করে My Computer এর Special Folders এ ক্লিক করুন।  
এবার ডানের Special Folders এর ড্রপ ডাউন থেকে Desktop নির্বাচন করে Change Location বাটনে ক্লিক করুন।  
এখন কোন ফোল্ডারে ডেক্সটপকে রাখতে চান সেই ফোল্ডারটি নির্বাচন করে Yes করুন।  
সবশেষে Yes করে Ok করুন।  
ব্যাস এখন ডেক্সটপে ফাইল রেখে দেখুন তা নতুন নির্বাচন করা ফোল্ডারে রয়েছে।  
অথবা নিচের কোডগুলো নোটপ্যাডে লিখে Desktop.reg নামে সেভ করুন এবং চালু করুন তাহলে D:\Desktop ডেক্সটপের নতুন লোকেশন হিসাবে সেট হবে।

```

[sourcecode language="plain"]
Windows Registry Editor Version 5.00
[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders]
"Desktop"="D:\\Desktop"
[/sourcecode]
```
