---
archive_id: shamokaldarpon-605
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 605
title: একাধিক কম্পিউটারে ইন্টারনেট শেয়ার করা
slug: share-internet-connection
language: bn
status: publish
published_at: '2008-06-29T10:56:07'
published_at_gmt: '2008-06-29T04:56:07'
modified_at: '2023-11-01T10:21:38'
modified_at_gmt: '2023-11-01T04:21:38'
original_url: https://www.shamokaldarpon.com/605/share-internet-connection
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Internet
- Internet Connection
- Mobile
- Share
- Sharing
- Tips
- ইন্টারনেট
- টিপস
- শেয়ার
content_hash: 4976bedf22cb2237dfed71537298f8c0c70cabcdba15963956941dc7aae65d1b
archived_at: '2026-11-12T08:35:52.132941+00:00'
---

আমরা যারা মোবাইল বা মডেম দ্বারা ইন্টারনেট ব্যবহার করি তারা চাইলে অনান্য লোকাল কম্পিউটারে ইন্টারনেট শেয়ার করে ব্যবহার করতে পারি। ধরি আপনার কম্পিউটারটি আরো দুটি কম্পিউটারের সাথে ল্যানের সাহায্যে সংযোগ স্থাপন করা আছে। আপনি আপনার কম্পিউটারে এডজ মডেম দ্বারা ইন্টারনেটের সংযোগ নিয়েছেন। এখন আপনি চাইলে অনান্য কম্পিউটারগুলোতেও ইন্টারনেটের সংযোগ দিতে পারেন শেয়ার করে। এতে অবশ্য গতি কিছুটা কমে যাবে।এজন্য আপনি আপনার লোকাল এরিয়া নেটওয়ার্কের আইপি এড্রেস দেখে নিন। ধরি আপনার লোকাল এরিয়া নেটওয়ার্কের আইপি এড্রেস হচ্ছে ১৯২.১৬৮.১.১২।

![](http://mehdiakram.files.wordpress.com/2008/06/share-your-mobile-internet1.jpg)

![](http://mehdiakram.files.wordpress.com/2008/06/share-your-mobile-internet2.jpg)  
প্রথমে আপনি আপনার কম্পিউটারে এডজ মডেম দ্বারা ইন্টারনেটের সংযোগ স্থাপন করুন। এরপরে সিস্টেম ট্রেতে থাকা উক্ত সংযোগের আইকনের উপরে মাউসের ডান বাটন ক্লিক করে Status এ ক্লিক করুন। অথবা Control Panel থেকে Network Connections এ গিয়ে উক্ত সংযোগের আইকনের উপরে মাউসের ডান বাটন ক্লিক করে Status এ ক্লিক করুন একটি স্টেটাস উইন্ডো আসবে। এবার General ট্যাবে থেকে Properties বাটনে ক্লিক করুন তাহলে প্রোপার্টিস উইন্ডো আসবে। এবার Advance ট্যাবে ক্লিক করে Internet Connection Sharing অংশে Allow other network users to connect through this computer’s internet connection চেক (যদি আপনার একাধিক লোকাল এরিয়ার সংযোগ থাকে তাহলে একটি ম্যাসেজ আসবে যে আপনি কোন লোকাল এরিয়াতে ইন্টারনেট শেয়ার দিবেন, আপনি আপনার পছন্দেরটি নির্বাচন করবেন।) করে Ok করুন। তাহলে Network Connections এর পরপর তিনটি ম্যাসেজ আসবে যেগুলোতে ধারাবাহিক ভাবে Ok Yes Ok করুন। এখন দেখুন আপনার কম্পিউটারের লোকাল আইপি পরিবর্তন হয়ে ১৯২.১৬৮.০.১ হয়েছে।

[![](http://mehdiakram.files.wordpress.com/2008/06/share-your-mobile-internet3.jpg)](http://mehdiakram.files.wordpress.com/2008/06/share-your-mobile-internet3.jpg)

এখন আপনি লোকাল এরিয়ার Status এ গিয়ে Properties বাটনে ক্লিক করে General ট্যাবে থেকে This connection uses the following items অংশের Internet Protocol (TCP/IP) নির্বাচন করে Properties বাটনে ক্লিক করুন। এবার আইপি ১৯২.১৬৮.০.১ পরিবর্তন করে পূর্বের আইপি ১৯২.১৬৮.১.১২ দিন এবং Ok করুন।  
এবার যে কম্পিউটারে আপনি ইন্টারনেট সংযোগ পেতে চান সেই কম্পিউটারের লোকাল এরিয়ার Status এ গিয়ে Properties বাটনে ক্লিক করে General ট্যাবে থেকে This connection uses the following items অংশের Internet Protocol (TCP/IP) নির্বাচন করে Properties বাটনে ক্লিক করুন। এবার Default gateway এর আইপি এড্রেস হিসাবে ১৯২.১৬৮.১.১২ লিখুন। এরপরে Use the flowing DNS server addresses অপশন বাটন চেক করে Preferred DNS server এর আইপি এড্রেস হিসাবেও ১৯২.১৬৮.১.১২ লিখে Ok Ok Ok করুন।  
এবার দেখুন আপনার এই কম্পিউটারে ইন্টারনেটের সংযোগ এসেছে। এভাবে আপনি অন্য আরেকটি কম্পিউটারে সংযোগ নিতে পারনে। ব্রডব্যান্ডের সংযোগও এভাবে শেয়ার করে ব্যবহার করা যাবে।
