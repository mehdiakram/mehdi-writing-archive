---
archive_id: shamokaldarpon-4185
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4185
title: বাংলা ওয়েব সাইটে গুগল এ্যাডসেন্স এর বিজ্ঞাপন
slug: show-google-adsense-ads-in-bengali-website
language: bn
status: publish
published_at: '2014-05-25T09:22:58'
published_at_gmt: '2014-05-25T03:22:58'
modified_at: '2015-11-28T09:48:55'
modified_at_gmt: '2015-11-28T03:48:55'
original_url: https://www.shamokaldarpon.com/4185/show-google-adsense-ads-in-bengali-website
author: মেহেদী আকরাম
categories:
- টিপস এন্ড ট্রিকস
tags:
- Ad
- Adsense
- Google
- Google Adsense
- এ্যাডসেন্স
- গুগল
- গুগল এ্যাডসেন্স
- বিজ্ঞাপন
content_hash: 811f466b326002131ddfc767d8f7b0e183d58f4539959f3d5b85f8e6bcc8d276
archived_at: '2026-11-12T08:35:21.944640+00:00'
---

গুগল এ্যাডসেন্স নিয়ে নতুন করে বলার কিছু নেই। তবে গুগল এ্যাডসেন্স বাংলা ভাষা সমর্থন করে না বিধায় বাংলা ওয়েবসাইটে গুগল এ্যাডসেন্স এর বিজ্ঞাপন প্রদর্শিত হয় না। এছাড়াও বাংলা ভাষার ওয়েবসাইট দিয়ে গুগল এ্যাডসেন্স এ আবেদন করলে তা বাতিল হয়ে যায়। তবে চাইলে একটু চালাকি করে বাংলা সাইটে গুগল এ্যাডসেন্স এর বিজ্ঞাপন দেখানো যায়।  
গুগল এ্যাডসেন্স এর আরেকটি উল্লেখযোগ্য দিক হলো একটি সচল এ্যাডসেন্স একাউন্ট দিয়ে ৫০০টি ওয়েবসাইটে বিজ্ঞাপন প্রদর্শণ করানো যায়।  
এজন্য এ্যাডসেন্স এর Code Type : Synchronous মুডে নিন।  
![Code Type : Synchronous](https://mehdiakram.files.wordpress.com/2014/10/adsense.png)  
এবার কোড কপি করে আপনার সাইটে পেষ্ট করুন।  
এখন

```
google_ad_width = 300;
google_ad_height = 250;
```

এর নিচে

```
google_language = 'en';.
```

যুক্ত করুন।  
ফলে কোড হবে অনেকটা নিচের মত।

```
<script type="text/javascript">
google_ad_client = "ca-pub-xxxxxxxxxxxxxx";
google_ad_slot = "xxxxxxxxxx";
google_ad_width = 300;
google_ad_height = 250;
google_language = 'en';

</script>
<!-- 300x250 Text & Display -->
<script src="//pagead2.googlesyndication.com/pagead/show_ads.js" type="text/javascript">

// ]]></script>
```

ব্যাস, এবার দেখুন আপনার বাংলা সাইটেও গুগল এ্যাডসেন্স এর বিজ্ঞাপন দেখা যাচ্ছে।
