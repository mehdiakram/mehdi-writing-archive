---
archive_id: shamokaldarpon-4263
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4263
title: ওয়ার্ডপ্রেসের পোষ্টের স্লাগের সীমা বৃদ্ধি করা
slug: increase-wp-post-slug-limit
language: bn
status: publish
published_at: '2015-04-10T15:40:09'
published_at_gmt: '2015-04-10T09:40:09'
modified_at: '2015-11-28T09:52:13'
modified_at_gmt: '2015-11-28T03:52:13'
original_url: https://www.shamokaldarpon.com/4263/increase-wp-post-slug-limit
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- slug
- WP
- ওয়ার্ডপ্রেস
- স্লাগ
content_hash: d8bf7d20727160c543fcec3380cd543b14268c9797e0fb3a460770a69d6a7f82
archived_at: '2026-11-12T08:35:21.961356+00:00'
---

ওয়ার্ডপ্রেসে কোন পোষ্ট করলে পোষ্টের স্লাগ সয়ংক্রিয়ভাবে ২০০ অক্ষর পর্যন্ত নির্ধারণ হয়ে যায়, (পার্মালিংক যদি Post name করা থাকে তাহলে দেখাবে)। পোষ্টের স্লাগ ২০০ অক্ষর পর্যন্ত হবার কারণ wp-posts এর post\_name এর Length/Values এর মান 200 আছে। বাংলাতে পোষ্ট করলে টাইটেল লিখলে তা ইউনিকোডে অনেক বড় হয়ে যায়। যেমন “কিডনির” বাংলা শব্দ হয়ে যায় “%E0%A6%95%E0%A6%BF%E0%A6%A1%E0%A6%A8%E0%A6%BF%E0%A6%B0” এত বড়। ফলে প্রথম ২০০ অক্ষর পর্যন্ত পোষ্টের স্লাগে থাকে।

কিন্তু আপনি যদি পোষ্টের স্লাগের সীমা বৃদ্ধি করতে চান তাহলে phpadmin থেকে wp-posts এর post\_name এর মান সীমা বৃদ্ধি করে করতে পারেন।

![Slug Screenshot 1](https://mehdiakram.files.wordpress.com/2015/05/slug-1.jpg)  
১. wp-posts টেবিলে ক্লিক করে Structure এ ক্লিক করুন। এখানে দেখুন post\_name এ varchar(200) আছে। এর ফলে পোষ্ট স্লাগে ২০০ অক্ষর পর্যন্ত দেখায়।

![Slug Screenshot 2](https://mehdiakram.files.wordpress.com/2015/05/slug-2.jpg)  
২. অক্ষর সীমা বাড়ানোর জন্য ডানের Change বাটনে ক্লিক করুন।

![Slug Screenshot 3](https://mehdiakram.files.wordpress.com/2015/05/slug-3.jpg)  
৩. এখন Length/Values এর মান ২০০ এর পরিবর্তে ২০০০ লিখে Save বাটনে ক্লিক করুন।

![Slug Screenshot 4](https://mehdiakram.files.wordpress.com/2015/05/slug-4.jpg)  
৪. এখন varchar(2000) দেখুন দেখাচ্ছে।

![Slug Screenshot 5](https://mehdiakram.files.wordpress.com/2015/05/slug-5.jpg)  
৫. এবার ২০০০ অক্ষর পর্যন্ত স্লাগ ব্যবহার করতে পারবেন।
