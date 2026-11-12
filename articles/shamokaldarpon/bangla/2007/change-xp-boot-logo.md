---
archive_id: shamokaldarpon-172
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 172
title: এক্সপির বুট লগো পরিবর্তন করা
slug: change-xp-boot-logo
language: bn
status: publish
published_at: '2007-12-02T21:04:00'
published_at_gmt: '2007-12-02T15:04:00'
modified_at: '2007-12-02T21:04:00'
modified_at_gmt: '2007-12-02T15:04:00'
original_url: https://www.shamokaldarpon.com/172/change-xp-boot-logo
author: admin
categories:
- টিপস এন্ড ট্রিকস
- হ্যাকিং / নিরাপত্তা
tags:
- উইন্ডোজ
content_hash: 134c1cdc07c9b342bebf2879afb061e936c873dc7480376ea1ecedaaf60d601b
archived_at: '2026-11-12T08:34:26.851047+00:00'
---

![boot-logo.jpg](http://mehdiakram.files.wordpress.com/2007/12/boot-logo.jpg)উইন্ডোজ এক্সপির বুট লগোতে সাধারণত এক্সপির নিজস্ব ছবি দেখা যায়। আপনি চাইলে উক্ত ছবিটি পরিবর্তন করে নিজের পছন্দের ছবি দিতে পারেন। সিস্টেম৩২ ফেল্ডারের (windows\system32) ntoskrnl.exe ফাইলে উক্ত ছবি রয়েছে, যা পরিবর্তন করতে হবে। রিসোর্স হ্যকারের সাহায্যে সহজে এই ছবি পরিবর্তন করা যায়। এজন্য আপনার প্রয়োজন 640 X 480 সাইজের ১৬ কালারের (১৬ বিটের নয়) ছবি। ছবিটি তৈরীর জ্য আপনি MS Paint খুলে ইমেজ সাইজ 640 X 480 নিন। এবার সেভ করুন 16 Color Bitmap হিসাবে। তাহলে ছবিটি ১৬ কালারে সেভ হবে। এবার উক্ত ইমেজে ইচ্ছামত কিছু লেখুন বা পছন্দের ছবি কপি করে এনে পেষ্ট করতে পারেন। ছবিটি পেষ্ট করলে মূল কালার পরিবর্তন হয়ে ১৬ কালারে হবে।  
এবার ছবিটি পরিবর্তনের জন্য প্রথমে ntoskrnl.exe ফাইলটি ব্যাকআপ করুন (কপি করে newntoskrnl.exe নামে রিনেম করুন তথ্য পরিবর্তনের জন্য)। এবার Resource Hacker সফটওয়্যারটি খুলুন। (Resource Hacker সফটওয়্যারটি www.users.on.net/johnson/resourcehacker থেকে বিনামূল্যে ডাউনলোড করা যাবে)। এখন ফাইল মেনু থেকে ওপেনে ক্লিক করে system32 ফোল্ডার থেকে newntoskrnl.exe ফাইলটি খুলুন। এবার বাদিকের পেনে রিসোর্স তালিকা থেকে Bitmap ফোল্ডারটি দুবার ক্লিক করে ১ নামের ফোল্ডারটি দুবার ক্লিক করে ১০৩৩ নামের রিসোর্স ফাইলটি সিলেক্ট করুন তাহলে ডানে উইন্ডোজের বুট লগোর ছবি দেখা যাবে। এখন Action মেনু থেকে Replace Bitmap… ক্লিক করুন তাহলে Replace Bitmap in.. ডায়ালগ বক্স আসবে। এখানে Open file with new bitmap বাটনটিতে ক্লিক করে আপনার ছবিটি সিলেক্ট করে ওপেন করুন। এখন Select bitmap to replace এ ১ সিলেক্ট রেখে Replace বাটনে ক্লিক করে সেভ করুন। এবার কম্পিউটার পূনরায় চালু (রিস্টার্ট) করে সেভমোডে (উইন্ডোজ চালু হওয়ার আগেই F8 চেপে) খুলুন। কম্পিউটার সেভমোডে চালু হলে windows\system32 ঢুকে ntoskrnl.exe ফাইলটি mainntoskrnl.exe নামে রিনেম করুন এবং newntoskrnl.exe ফাইলটি ntoskrnl.exe নামে রিনেম করুন। এবার কম্পিউটার পূনরায় চালু করলে দেখবেন উইন্ডোজের বুট লগো এর পরিবর্তে আপনার পছন্দের ছবিটি দেখা যাচেছ।
