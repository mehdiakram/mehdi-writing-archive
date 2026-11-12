---
archive_id: shamokaldarpon-50
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 50
title: ফ্লাশে নিয়ন্ত্রনের বোতাম
slug: button-in-flash
language: bn
status: publish
published_at: '2007-03-05T12:38:44'
published_at_gmt: '2007-03-05T06:38:44'
modified_at: '2023-11-01T10:21:45'
modified_at_gmt: '2023-11-01T04:21:45'
original_url: https://www.shamokaldarpon.com/50/button-in-flash
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Flash
- ফ্লাশ
content_hash: b8d0704f02364d858ada50cef4fa329dcb92977a00acaa0580dafe68312c8dfc
archived_at: '2026-11-12T08:35:57.308586+00:00'
---

ফ্লাশ দ্বারা আমরাতো সুন্দর সুন্দর অ্যানিমেশন তৈরী করতে পারি। আর এই সব অ্যানিমেনে বিভিন্ন দরকারী বোতাম যুক্ত করা যায়। আমরা এখন (Exit) বন্ধ করার, (Full Screen) পর্দাজুড়ে দেখার এবং (Restore) পূর্বের অবস্থায় ফিরিয়ে আনার বোতাম তৈরী করবো। এজন্য ফ্লাশ তৈরী করে পছন্দমত অ্যানিমেশন তৈরী করুন। এবার তিনটি বোতাম তৈরী করুন বা কমন লাইবে্ররী থেকে তিনটি বাটন নিন। এবার Actions প্যানেল বের করুন (WindowActions বা F9 চাপুন)। এখন Restore বাটনটি নির্বাচন করে Actions প্যানেলে Expert মোডে  
on (release, keyPress “r”)  
{  
fscommand(“fullscreen”, “False”);  
}  
লিখুন, Full Screen বাটনটি নির্বাচন করে Expert মোডে  
on (release, keyPress “f”) { fscommand(“fullscreen”, “true”);}লিখুন এবং Exit বাটনটি নির্বাচন করে Expert মোডে  
on (release, keyPress “”)  
{  
fscommand(“quit”);  
লিখুন। ব্যাস এবার File মেনু থেকে Export Movie নির্বাচন করলে Export Movie ডায়ালগ বক্স আসবে। এখানে .swf ফরমেট নির্বাচন করে সেভ ControlButton নামে করুন। এবার ControlButton.swf ফাইলটি চালিয়ে বোতামগুলো পরীক্ষা করে দেখুন।
