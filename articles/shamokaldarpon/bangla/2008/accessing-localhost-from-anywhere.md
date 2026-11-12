---
archive_id: shamokaldarpon-714
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 714
title: লোকালহোস্ট যেকোন জায়গা থেকে এক্সেস করা
slug: accessing-localhost-from-anywhere
language: bn
status: publish
published_at: '2008-08-19T22:03:51'
published_at_gmt: '2008-08-19T16:03:51'
modified_at: '2023-11-01T10:14:47'
modified_at_gmt: '2023-11-01T04:14:47'
original_url: https://www.shamokaldarpon.com/714/accessing-localhost-from-anywhere
author: admin
categories:
- কম্পিউটার ও প্রযুক্তি
tags:
- Add-Ons
- Search
- Yahoo
- ইয়াহু
- গুগল
- ফায়ারফক্স
- সার্চ
content_hash: ea95bb437ba824e96db1e11d1879d8123cccb645bdc0737091e1c23e74a862fd
archived_at: '2026-11-12T08:35:51.901484+00:00'
---

লোকালহোস্ট শব্দটা ডেভেলপমেন্টারদের কাছে খুবই পরিচিত। রিমোট লোকেশন বা ইন্টারনেটের মাধ্যমে যদি আপনার লোকালহোস্টকে এক্সেস করা যায় তাহলে কেমন হয়! সিকিউর টানেল তৈরির মাধ্যমে লোকালহোস্টকে অনলাইনে আনা যায়।  
এমনই কিছু সফট‌ওয়্যারের তালিকা নিচে রয়েছে।

1. [ngrok](https://ngrok.com/)
2. [PageKite](https://pagekite.net/)
3. [Forward](https://forwardhq.com/)
4. [ProxyLocal](http://proxylocal.com/)
5. [BrowserStack](http://www.browserstack.com/)

ধরে নিচ্ছি আপনার কম্পিউটার লোকালহোস্টের সফট‌ওয়্যার [wamp](http://www.wampserver.com/en/) বা [xampp](https://www.apachefriends.org/index.html) ইনস্টল করা আছে এবং আপনি http://localhost/ বা http://127.0.0.1/ ব্রাউজ করতে পারছেন। এখন আপনি লোকালহোস্টকে রিমোট লোকেশন থেকে এক্সেস করতে চাচ্ছেন।

**ngrok দ্বারা:**  
ধাপ১) প্রথমে [ngrok.com](https://ngrok.com) থেকে ngrok ডাউনলোড করে আনজিপ করুন। এরপর কমান্ড প্রোম্পট থেকে যেখানে ngrok রেখেছেন সেই ডিরেক্টরিতে যান। (ধরি আপনি ডি ড্রাইভের ngrok ফোল্টারে ngrok ফাইলটি আছে) এজন্য প্রথমে d: লিখে এন্টার দিয়ে cd ngrok এন্টার দিন।

ধাপ২) এবার টানেল তৈরি করার জন্য ngrok http 80 লিখে এন্টার করুন তাহলে দেখবেন নিচের মতো একটি টানেল তৈরী হয়েছে।  
![The ngrok console UI](https://mehdiakram.files.wordpress.com/2015/12/ngrok1.png)

ধাপ৩) এখন আপনি উল্লেখিত ইউআরএল দিয়ে যেকোন যায়গা থেকে ব্রাউজ করতে পরবেন।  
![Inspecting your traffic](https://mehdiakram.files.wordpress.com/2015/12/ngrok2.png)  
*নোট: http://localhost:4040/ ব্রাউজ করে আপনি ট্রাফিক সম্পর্কে জানতে পারবেন।*
