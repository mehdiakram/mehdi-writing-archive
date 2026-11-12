---
archive_id: shamokaldarpon-5874
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 5874
title: Google Workspace ও Zoho মেইল ডুয়েল ডেলিভারি
slug: google-workspace-zoho-mail-split-delivery
language: bn
status: publish
published_at: '2023-11-26T15:26:14'
published_at_gmt: '2023-11-26T09:26:14'
modified_at: '2023-11-26T15:32:41'
modified_at_gmt: '2023-11-26T09:32:41'
original_url: https://www.shamokaldarpon.com/5874/google-workspace-zoho-mail-split-delivery
author: মেহেদী আকরাম
categories:
- টিপস এন্ড ট্রিকস
tags:
- Google
- Mail
- MX
- split delivery
- Two Mail Server
- txt
- Workspace
- zoho
- ডুয়েল ডেলিভারি
- মেইল
content_hash: f262821a491a6bf4ac080dc73d5bb330a95ec9b48d05b24f5a3689a77207b5f0
archived_at: '2026-11-12T08:36:38.606619+00:00'
---

কখনও কখনও আমাদের একটি ডোমেইনে একাধিক মেইল সার্ভার ব্যবহার করতে চাই। ধরি আপনার ১টি ইমেইল info@royaltechbd.com গুগল ওয়ার্কস্পেসে ব্যবহার করছেন, এখন চাচ্ছেন অফিসের অনান্য কর্মকর্তারা Zoho মেইল সার্ভার ব্যবহার করুক। তাহলে আপাকে মেইল ডুয়েল ডেলিভারি বা স্প্লিট ডেলিভারি চালু করতে হবে।  
এই ডুয়েল ডেলিভারি বা স্প্লিট ডেলিভারি দুইভাবে করা যায় Google Workspace কে প্রাইমারি ধরে অথবা Zoho কে প্রাইমারি ধরে।  
আমরা এখনে দেখবো কিভারে Google Workspace কে প্রাইমারি ধরে মেইল ডুয়াল ডেলিভারি বা split delivery সেটআপ করা যায়।

![](https://www.shamokaldarpon.com/wp-content/uploads/2023/11/Split-delivery.png)

ধাপ ১. এজন্য প্রথমে <https://admin.google.com> এ লগইন করুন।  
ধাপ ২. Admin console বাম পাশের মেনু থেকে App > Google Workspace > Gmail এ ক্লিক করে Hosts সেকশনে ক্লিক করুন।  
ধাপ ৩. এবার Add Route এ ক্লিক করুন।  
ধাপ ৪. Add mail route ক্লিক করে হোষ্টের একটি নাম দিন (Zoho Mail) এবং 1. Specify email server এ Multiple hosts নির্বাচন করুন। এখানে Zoho এর MX দিতে হবে, mx.zoho.com 25 50, mx2.zoho.com 25 40, mx3.zoho.com 25 10 দিন এবং সেভ করুন।

![](https://www.shamokaldarpon.com/wp-content/uploads/2023/11/Host-Zoho-Mail.jpg)

ধাপ ৫. এবার Admin console বাম পাশের মেনু থেকে App > Google Workspace > Gmail এ ক্লিক করে Routing সেকশনে ক্লিক করুন।  
ধাপ ৬. এবার Routing সেকশনে এ Add Another Rule বাটনে ক্লিক করুন এবং Routing এর নাম দিন (Inbound Route) ।  
ধাপ ৭. এবার 1. Email messages to affect এ Inbound এবং Internal – Receiving নির্বাচন করুন।

![](https://www.shamokaldarpon.com/wp-content/uploads/2023/11/Route-1-Inbound.jpg)

ধাপ ৮. 2. For the above types of messages, do the following এ Modify message নির্বাচিত রেখে Route এ Change route নির্বাচন করুন এবং ড্রপডাউন থেকে Zoho Mail হোষ্ট নির্বাচন করুন।

![](https://www.shamokaldarpon.com/wp-content/uploads/2023/11/Route-2-Route.jpg)

ধাপ ৯. এরপরে নিচের Show options এ ক্লিক করে Account types to affect এর Unrecognized/Catch-all box নির্বাচিত রাখুন এবং Users/Groups রেখে সেভ করুন.  
ব্যাস হয় গেলো Google Workspace এর ডুয়াল ডেলিভারি বা split delivery।

নোট: ডোমেইনের TXT রেকর্ড হিসাবে v=spf1 include:zoho.com include:\_spf.google.com +a +mx ~all ব্যবহার করতে হবে এবং Google Workspace এর MX রেকর্ড ব্যবহার করতে হবে।
