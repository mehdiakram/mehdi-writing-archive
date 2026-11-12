---
archive_id: shamokaldarpon-330
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 330
title: ফায়ারফক্স এবং ইউটিউব খুলতে সমস্যা
slug: problem-to-open-firefox-and-youtube
language: bn
status: publish
published_at: '2008-03-05T00:38:58'
published_at_gmt: '2008-03-04T18:38:58'
modified_at: '2008-03-05T00:38:58'
modified_at_gmt: '2008-03-04T18:38:58'
original_url: https://www.shamokaldarpon.com/330/problem-to-open-firefox-and-youtube
author: admin
categories:
- টিপস এন্ড ট্রিকস
- হ্যাকিং / নিরাপত্তা
tags:
- Firefox
- Internet
- Security
- Virus
- Youtube
- ইউটিউব
- ফায়ারফক্স
- ভাইরাস
content_hash: 9d3362742ca9d16d95412dd64b393e67744ab9773f5554a48f5cf000ca9ec252
archived_at: '2026-11-12T08:34:30.777874+00:00'
---

![use-ie.png](http://mehdiakram.files.wordpress.com/2008/03/use-ie.png)অনেকসময় দেখা যায় ফায়ারফক্স খুলতে গেলে তা না খুলে I dnt hate Mozilla but use IE or else… মেসেজ আসে। ফলে ফায়ারফক্স খোলা যায় না। আবার ইউটিউব সাইটটিতে ঢুকতে গেলে তা না খুলে Youtube is banned you fool মেসেজ আসে। এটি মুলত এর W32.USB worm কারনে হয়ে থাকে। বেশীরভাগ ক্ষেত্রে এন্টিভাইরাসে স্ক্যান করেও এই ভাইরাসটি মুছে ফেলা যায় না। এ থেকে বাঁচতে আপনি নিন্মাক্ত পথ অবলম্বন করতে পারেন।  
প্রথমে টাস্ক ম্যানেজার খুলে (Ctrl+Alt+Del চেপে) Processes ট্যাবে যান এবার Image name কলাম থেকে svchost.exe (যা ইউজারে চালু আছে, system, local বা অন্যকিছুতে নয়) নির্বাচন করে End Process বাটনে ক্লিক করে বন্ধ করুন। এবার মাই কম্পিউটারের এড্রেসবারে C:heap41a লিখে এন্টার করলে heap41a ফোল্ডার খুলবে এবার এই ফোল্ডারের সকল ফাইল (svchost.exe, script1.txt, standard.txt, reproduce.txt এবং একটি অডিও ফাইল) মুছে ফেলুন। ফোল্ডারসহ মুছে ফেললে ভাল হয়। এরপরে রানে গিয়ে regedit লিখে এন্টার করলে রেজিষ্ট্রি এডিটর খুলবে। এখন Edit মেনু থেকে Find এ ক্লিক করে heap41a লিখে সার্চ করুন। এর heap41a নামে পাওয়া তথ্যগুলো মুছে ফেলুন। এবার কম্পিউটার পুনরায় চালু করলে ফায়ারফক্স বা ইউটিউব খুলতে সমস্যা হবে না।  
তবে এ ওয়ার্ম থেকে মুক্তি পেতে আপনার ইউএসবি ড্রাইভ থেকে autorun এবং Microsoft Power Point.exe ফাইলটি মুছে ফেলুন।
