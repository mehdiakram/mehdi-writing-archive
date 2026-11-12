---
archive_id: shamokaldarpon-1762
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 1762
title: ভাইরাসের কারণে ফোল্ডার হিডেন হলে ফিরে পাওয়া
slug: show-virus-related-hidden-files-from-flash-disk
language: bn
status: publish
published_at: '2009-10-12T23:04:55'
published_at_gmt: '2009-10-12T17:04:55'
modified_at: '2023-11-01T10:24:00'
modified_at_gmt: '2023-11-01T04:24:00'
original_url: https://www.shamokaldarpon.com/1762/show-virus-related-hidden-files-from-flash-disk
author: মেহেদী আকরাম
categories:
- টিপস এন্ড ট্রিকস
tags:
- Attribute
- Attribute Changer
- files
- Folder
- Freeware
- Hidden
- Hidden Attribute
- Hidden Files
- Hide
- petges
- Software
- System
- Unhide
- Virus
- এট্রিবিউট
- এট্রিবিউট চেঞ্জার
- চেঞ্জ
- ভাইরাস
content_hash: 9c9ae06298aa52e8db99fc7aeeeab852be5b8b736dcb5581c0ba779dec52d1fe
archived_at: '2026-11-12T08:35:57.826229+00:00'
---

ভাইরাসের কারণে অনেক সময় হার্ডডিক্সের বা ফ্লাশ ডিক্স (পেন ড্রাইভ) এর ফোল্ডার হিডেন হয়ে যায়। ফলে এই ফোল্ডারগুলো যেমন আনহাইড করা যায় না তেমনই সার্চ করলে ফলাফলও পাওয়ার যায় না।  
**পদ্ধতি ১)**  
ফোল্ডারগুলো খুঁজে পেতে Control Panel থেকে Folder Options খুলুন। এবার View ট্যাবে গিয়ে Show hidden files and folders এবং Hide protected operating system files আনচেক করুন। এবার উক্ত ফোল্ডারে সার্চ (Advanced Options থেকে Search hidden files and folders চেক করে) করুন তাহলে হিডেন হওয়া ফোল্ডারগুলো দেখা যাবে।  
ভাইরাস জনিত কারনে ফোল্ডারগুলো হিডেন অপশন ডিজেবল হলে উক্ত ফোল্ডারগুলোর প্রোপাটিস থেকে হিডেন চেক বক্স আনচেক করা যাবে না ফলে ফোল্ডারগুলো স্বাভাবিকভাবে প্রদর্শিত হবে না। হিডেন অপশন সক্রিয় এবং আনচেক করতে পারবেন এট্রিবিউট চেঞ্জার সফটওয়্যার দ্বারা। ১.০৬ মেগাবাইটের ফ্রিওয়্যার এট্রিবিউট চেঞ্জার সফটওয়্যারটি [www.petges.lu](http://www.petges.lu) থেকে ডাউনলোড করে ইনস্টল করে নিন। এখন যে ফোল্ডারের এট্রিবিউট পরিবর্তন করতে চান সেই ফোল্ডারের উপরে মাউসের ডান বাটন ক্লিক করে Change Attributes এ ক্লিক করুন এবং Folder Properties ট্যাব থেকে System, Hidden আনচেক Ok করে করুন।  
ব্যাস এবার দেখুন ফোল্ডারগুলো স্বাভাবিকভাবে দেখা যাচ্ছে। এখন Folder Options এর View ট্যাবে গিয়ে Show hidden files and folders এবং Hide protected operating system files চেক করে আসুন।  
**পদ্ধতি ২)**  
এছাড়াও কমান্ড প্রোমম্টে গিয়ে (run এ গিয়ে cmd লিখে enter করে) ড্রাইভে প্রবেশ করে (পেনড্রাইভ বা মেমোরি কার্ড যে ড্রাইভ যদি I হয় তাহলে I: লিখে এন্টার করতে হবে) attrib -s -r -h -a /s /d এন্টার করুন তাহলে হিডেন হওয়া ফাইল এবং ফোল্ডার ফিরে আসবে।

**কমান্ড বিশ্লেষণ হচ্ছে:**   
attrib = attribute  
s = system file  
r = read only  
h = hidden  
a = archive  
/d = directory  
/s = sub directory
