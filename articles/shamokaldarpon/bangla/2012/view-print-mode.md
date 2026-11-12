---
archive_id: shamokaldarpon-3155
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 3155
title: ওয়ার্ডপ্রেস ব্লগের লেখা প্রিন্ট মোডে দেখা
slug: view-print-mode
language: bn
status: publish
published_at: '2012-08-14T05:16:45'
published_at_gmt: '2012-08-13T23:16:45'
modified_at: '2015-02-03T10:30:42'
modified_at_gmt: '2015-02-03T04:30:42'
original_url: https://www.shamokaldarpon.com/3155/view-print-mode
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- Blog
- Print mode
- ওয়ার্ডপ্রেস
- প্রিন্ট মোড
- ব্লগ
content_hash: 4e9ce949ff456cc34395a3a8bf727d3602fd6f0e3a7436e4b645b6550b029234
archived_at: '2026-11-12T08:35:14.734684+00:00'
---

জনপ্রিয় ব্লগিং সিএমএস হচ্ছে [ওয়ার্ডপ্রেস](http://www.shamokaldarpon.com/tag/wordpress)। যারা নিজস্ব হোস্টে ওয়ার্ডপ্রেস ব্যাবহার করছেন তারা চাইলে ইচ্ছামত পরিবর্তন করতে পারেন। ব্যাবহারকারীরা অনেক সময় ব্লগের লেখা প্রিন্ট করতে চাই, তারা সাধারণত File > Print গিয়ে প্রিন্ট করে ফলে সাইটের মূল লেখা ছাড়াও হেডার, ফুডার, সাইডবার ইত্যাদি প্রিন্ট হয়। এ থেকে মুক্তি পেতে ব্লগে Print Mode যুক্ত করা যেতে পারে যাতে শুধুমাত্র মূল লেখাটি দেখাবে যা থেকে ব্যবহারকারীরা প্রিন্ট করতে পারে।  
> এজন্য প্রথমে Pages > Add New গিয়ে একটি পেজ তৈরী করুন এবং পেজের সৱাগ read দিন (যেমন, www. shamokaldarpon.com/read)|  
> এবার .htaccess এর ফাইলটি খুলে তাতে নিচের লাইনটি যোগ করুন।

```
RewriteRule ^read/([0-9]+)/?$ /read/?u=$1 [QSA,L]
```

> এরপরে <http://db.tt/mQLlUNTu> থেকে ডাউনলোড করা page-read.zip ফাইলটি আনজিপ করে page-read.php ফাইলটি থীমের ফোল্ডারে আপলোড করুন।  
> এখন পোস্টের যে স্থানে লিংকটি রাখতে চান সেখাবে নিচের কোড দিন।

```
<a href="/read/<?php the_ID(); ?>/">Print Mode</a>
```

এবার Print Mode লিংকে ক্লিক করলে পোষ্টটি হেডার, ফুডার, সাইডবার ছাড়াই দেখাবে।
