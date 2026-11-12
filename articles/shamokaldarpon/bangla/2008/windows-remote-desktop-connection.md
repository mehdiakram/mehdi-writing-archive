---
archive_id: shamokaldarpon-641
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 641
title: উইন্ডোজের রিমোট ডেস্কটপের মাধ্যমে লোকাল নেটওয়ার্কের কম্পিউটার নিয়ন্ত্রণ
slug: windows-remote-desktop-connection
language: bn
status: publish
published_at: '2008-07-17T00:55:36'
published_at_gmt: '2008-07-16T18:55:36'
modified_at: '2012-11-04T11:31:46'
modified_at_gmt: '2012-11-04T05:31:46'
original_url: https://www.shamokaldarpon.com/641/windows-remote-desktop-connection
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Connection
- Desktop
- LAN
- Remote
- Remote Desktop
- উইন্ডোজ
- কম্পিউটার ও প্রযুক্তি
- ডেস্কটপ
- নিয়ন্ত্রণ
- রিমোট
- লোকাল নেটওয়ার্ক
content_hash: bf74b2d2993a013cc3074e2521baa00ae90de72dc96e3d2b18a42669ddd380f3
archived_at: '2026-11-12T08:35:08.371876+00:00'
---

কয়েকটি কম্পিউটার লোকাল নেটওয়ার্কের দ্বারা সংযুক্ত থাকলে উইন্ডোজের বিল্টইন রিমোট ডেস্কটপের সাহায্যে অন্য যেকোন কম্পিউটার নিয়ন্ত্রণ করা যাবে। এজন্য অবশ্য উক্ত কম্পিউটারকে রিমোট ডেস্কটপ সক্রিয় থাকতে হবে।  
রিমোট ডেস্কটপ সক্রিয় করতে মাই কম্পিউটারের উপরে মাউসের ডান বাটন ক্লিক করে Properties এ ক্লিক করুন অথবা Control Panel থেকে System এ ক্লিক করুন তাহলে System Properties আসবে। এবার Remote ট্যাব থেকে Allow users to connect remotely to this computer চেক করুন। তাহলে এই কম্পিউটারের সকল এ্যাডমিনিষ্টেটর ইউজার স্বাভাবিকভাবে রিমোট ডেস্কটপের মাধ্যমে ঢুকতে পারবে। আর আপনি যদি অনান্য কোন ইউজারকে রিমোট ডেস্কটপ ব্যবহারের অনুমতি দিতে চান তাহলে Select Remote Users… বাটনে ক্লিক করে Add… বাটনে ক্লিক করুন। এবার Advanced বাটনে ক্লিক করে Select Users ডায়ালগ বক্স থেকে Find Now বাটনে ক্লিক করুন এবং নিচে থেকে পছন্দের ইউজার নির্বাচন করে সবগুলো উইন্ডো Ok করে শেষ করুন।  
এবার নেটওয়ার্কের যে কোন কম্পিউটার থেকে অন্য কম্পিউটারে ঢোকার জন্য Start Menu\Programs\Accessories\Communications এর Remote Desktop Connection এ ক্লিক করুন (অথবা রানে গিয়ে mstsc লিখে এন্টার করুন) তাহলে Remote Desktop Connection উইন্ডো আসবে। এবার আপনি যে কম্পিউটারে ঢুকতে চান সেই কম্পিউটারের আইপি এড্রেস লিখে Connect বাটনে ক্লিক (এন্টার চাপুন) করুন। তাহলে উক্ত রিমোট কম্পিউটারের সাথে সংযোগ স্থাপন করবে। (রিমোট কম্পিউটার যদি বন্ধ থাকে বা রিমোট ডেস্কটপ সক্রিয় না থাকে তাহলে Remote Desktop Disconnection ম্যাসেজ আসবে।) আর সব ঠিক মত থাকলে Log On to Windows আসবে। এখানে আপনি ইউজারের নাম এবং পাসওয়ার্ড লিখে Ok বটিনে ক্লিক (এন্টার চাপলে) করলে লগইন হবে। এখন আপনি স্বাভাবিকভাবে উক্ত কম্পিউটারের সকল কাজ (এমনকি বন্ধও) করতে পারবেন।  
আপনি যদি আপনার নিজের কম্পিউটারের ড্রাইভগুলোকে রিমোট কম্পিউটারে শেয়ার হিসাবে দেখতে চান তাহলে Remote Desktop Connection উইন্ডো থেকে Options>> বাটনে ক্লিক করে Local Resource থেকে Disk drives এ চেক করুন।

ভিডিও টিউটোরিয়াল
