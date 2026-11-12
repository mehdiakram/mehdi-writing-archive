---
archive_id: shamokaldarpon-665
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 665
title: ফায়ারফক্সের গতি বাড়িয়ে নিন
slug: increase-firefox-speed
language: bn
status: publish
published_at: '2008-07-28T13:49:01'
published_at_gmt: '2008-07-28T07:49:01'
modified_at: '2008-07-28T13:49:01'
modified_at_gmt: '2008-07-28T07:49:01'
original_url: https://www.shamokaldarpon.com/665/increase-firefox-speed
author: admin
categories:
- টিপস এন্ড ট্রিকস
- ব্রাউজার
tags:
- Firefox
- Increase
- Speed
- Tips
- ওপেন সোর্স
- গতি
- টিপস
- ফায়ারফক্স
- ব্রাউজার
- মজিলা
content_hash: 0e8305a14edd777a28988caefab7cf04acac5508d42f80cee2fb1cd463bbc194
archived_at: '2026-11-12T08:34:35.052743+00:00'
---

জনপ্রিয় ওয়েব ব্রাউজার মজিলা ফায়ারফক্সের সবচেয়ে বড় সুবিধা হচ্ছে নতুন নতুন বিভিন্ন বৈশিষ্ট যোগ করার ব্যবস্থা। মুক্ত এবং ফ্রি এই ব্রাউজারের গতি বাড়িয়ে নিতে ম্যানুয়ালী কিছু কনফিগার করে নিতে পারেন। এজন্য এড্রেসবারে about:config লিখে এন্টার করুন, তাহলে ফায়ারফক্স কনফিগারেশন আসবে।  
এখন network.http.pipelining এর মান true দিন (Preference এর উপরে মাউস দ্বারা দুইবার ক্লিক করলেই false থেকে true হবে)। একই ভাবে network.http.proxy.pipelining, network.dns.disableIPv6 এবং plugin.expose\_full\_path এর মান true নির্ধারণ করুন। এছাড়াও network.http.pipelining.maxrequests এর মান ৪ এর পরিবর্তে ৮ দিন।  
এবার nglayout.initialpaint.delay নামে নতুন ইন্টিজার Preference তৈরী করুন এবং মান দিন ০। Preference তৈরী করতে মাউসের ডান বাটন ক্লিক করে New এ ক্লিক করুন এবং ডান থেকে String/integer/boolean নির্বাচন করুন, এরপরে Preference এর নাম লিখে Ok করুন এবং পরবর্তি উইন্ডোতে ভ্যালু লিখে বা নির্বাচন করে Ok করুন।  
একই ভাবে content.notify.backoffcount নামে নতুন ইন্টিজার Preference তৈরী করুন এবং মান দিন ৫, ui.submenuDelay নামে নতুন ইন্টিজার Preference তৈরী করুন এবং মান দিন ০, content.max.tokenizing.time নামে নতুন ইন্টিজার Preference তৈরী করুন এবং মান দিন 2250000, content.notify.interval নামে নতুন ইন্টিজার Preference তৈরী করুন এবং মান দিন 750000, browser.cache.memory.capacity নামে নতুন ইন্টিজার Preference তৈরী করুন এবং মান দিন 65536|  
এবার content.interrupt.parsing এবং content.notify.ontimer নামে নতুন বুলিয়েন Preference তৈরী করুন এবং মান true দিন। ব্যাস এবার দেখুন ফায়ারফক্সের গতি আগের তুলনায় বেড়েছে।
