---
archive_id: shamokaldarpon-185
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 185
title: সাজিয়ে নিন সিস্টেম প্রোপার্টিসের ছবি ও তথ্য
slug: rearrange-system-properties
language: bn
status: publish
published_at: '2007-12-11T02:00:13'
published_at_gmt: '2007-12-10T20:00:13'
modified_at: '2007-12-11T02:00:13'
modified_at_gmt: '2007-12-10T20:00:13'
original_url: https://www.shamokaldarpon.com/185/rearrange-system-properties
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Tips
- উইন্ডোজ
- টিপস
content_hash: 21c3007d300f445e9a70c6d9923afe6cc4441de7dbea56070f21ade68b388a29
archived_at: '2026-11-12T08:34:26.890046+00:00'
---

উইন্ডোজ এক্সপি’র সিস্টেম প্রোপার্টিসের জেনারেল ট্যাবে যে ছবি এবং তথ্য থাকে সেগুলো পরিবর্তন করে আপনি আপনার পছন্দের ছবি এবং তথ্য যোগ করতে পারেন।  
**উপরের ছবি পরিবর্তন:** উপরের ছবি পরির্তনের জন্য আপনার দরকার (সর্বোচ্চ) 180×158 পিক্সেলের বিটম্যাপ (.bmp) ছবি। আর এই ছবি পরিবর্তন করতে হলে windows (WinNT) এর system32 ফোল্ডারের sysdm.cpl ফাইলটি পরিবর্তন করতে হবে। এজন্য প্রথমে ফাইলটির ব্যাক-আপ করে নিন।  
এবার Resource Hacker সফটওয়্যারটি খুলুন। (Resource Hacker সফটওয়্যারটি www.users.on.net/johnson/resourcehacker থেকে ডাউনলোড করে নিতে পারেন)। এখন ফাইল মেনু থেকে ওপেনে ক্লিক করে system32 ফোল্ডার থেকে sysdm.cpl ফাইলটি খুলুন। এবার বাদিকের প্যানে রিসোর্স তালিকা থেকে Bitmap ফোল্ডারটি দুবার ক্লিক করে ১ নামের ফোল্ডারটি দুবার ক্লিক করে ১০৩৩ নামের রিসোর্স ফাইলটি সিলেক্ট করুন তাহলে ডানে কম্পিউটারের ছবি দেখা যাবে। এখন Action মেনু থেকে Replace Bitmap… ক্লিক করুন। এমতবস্থায় Open file with new bitmap বাটনটিতে ক্লিক করে আপনার ছবিটি নির্বাচন করে খুলুন। এখন Select bitmap to replace এ ১ সিলেক্ট রেখে Replace বাটনে ক্লিক করে সেভ করুন এবং ডেক্সটপে My Computer আইকনে ডান বাটন ক্লিক করে (start + Pause Break চেপে) Properties ক্লিক করলে System Properties এ আপনার ছবি দেখা যাবে।  
**নিচে ছবি এবং তথ্য যোগ করা:** এজন্য প্রথমে উইন্ডোজের সিস্টেম ফোল্ডার (C:\WINDOWS\system) খুলুন। এবার OEMINFO.INI নামের ফাইলটি নোটপ্যাডে খুলে পূর্বের তথ্য মুছে ফেলে নিচের সংকেত লিখে সেভ করুন।  
[General]  
Manufacturer=S. M. Mehdi Akram [ROYAL]  
[Support Information]  
Line1=”S. M. Mehdi Akram [ROYAL]”  
Line2=”Mobile No: +8801552333272″  
Line3=”http://www.mehdi-akram.tk”  
আপনি চাইলে General বা Support Information অংশের পরে আরো তথ্য যোগ করতে পারেন। এবার OEMLOGO.BMP নামের (210×105 পিক্সেলের একটি বিটম্যাপ .bmp ছবি) একটি ছবি একই ফোল্ডারে রাখুন এবং সিস্টেম প্রোপাটিস খুলে দেখুন পরিবর্তনটা।
