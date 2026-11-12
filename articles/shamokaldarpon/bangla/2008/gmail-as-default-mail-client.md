---
archive_id: shamokaldarpon-616
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 616
title: ফায়ারফক্সের ডিফল্ট মেইল ক্লাইন্ট হিসাবে জিমেইলের ব্যবহার
slug: gmail-as-default-mail-client
language: bn
status: publish
published_at: '2008-07-04T08:34:07'
published_at_gmt: '2008-07-04T02:34:07'
modified_at: '2008-07-04T08:34:07'
modified_at_gmt: '2008-07-04T02:34:07'
original_url: https://www.shamokaldarpon.com/616/gmail-as-default-mail-client
author: admin
categories:
- ইমেইল
- টিপস এন্ড ট্রিকস
tags:
- Firefox
- Internet
- mail client
- Mozilla Firefox
- Tips
- ওপেন সোর্স
- জিমেইল
- টিপস
- ফায়ারফক্স
- মেইল ক্লাইন্ট
content_hash: 70bbe68e4c1bdea9ed1ec50cc4684cd2257a70500b117eabd6ef4c8566865d7e
archived_at: '2026-11-12T08:34:35.027731+00:00'
---

ইমেইলের কোন লিংকে ক্লিক করলে তা ডিফল্ট মেইল ক্লাইন্টের কম্পোজারে খোলে। ফায়ারফক্সের জন্য আপনি যদি জিমেইলকে ডিফল্ট মেইল ক্লাইন্ট হিসাবে ব্যবহার করতে চান তাহলে প্রথমে জিমেইলে সাইন ইন করুন এবং এড্রেস বাসে নিচের কোড লিখুন  
javascript:window.navigator.registerProtocolHandler(“mailto”,”https://mail.google.com/mail/?extsrc=mailto&url=%s”,”Gmail”)  
আর আপনি যদি নিজস্ব ডোমেইন ব্যবহার করেন তাহলে নিচের কোড লিখুন  
javascript:window.navigator.registerProtocolHandler(“mailto”,”https://mail.google.com/a/yourdomain.com/mail/?extsrc=mailto&url=%s”,”Gmail”) এবং এন্টার করুন। এখন উপরে একটা মেসেজ আসবে সেখানে ডান দিক থেকে Add Application বাটনে ক্লিক করুন। এবার যেকোন মেইল লিংকে ক্লিক করুন তাহলে Launch Application আসবে। এখান থেকে জিমেইল নির্বচিন করে নিচের Remember my choice for mailto links চেক বক্স চেক করে Ok করুন। এখন Tools> Options থেকে Applications ট্যাবে গিয়ে mailto অপশনের ড্রপ ডাউন থেকে নির্বাচন Application details করুন এবং সেটিং পেজ থেকে জিমেইল এবং অনান্য এ্যাপলিকেশনগুলো মুছে দিন। তাহলে এরপর থেকে কোন ইমেইলের লিংকে ক্লিক করলে জিমেইল কম্পোজারে সরাসরি চলে আসবে।
