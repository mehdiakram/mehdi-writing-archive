---
archive_id: shamokaldarpon-4136
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4136
title: ওয়ার্ডপ্রেসে মোবাইল ডিভাইস চেক করা
slug: check-if-the-user-is-visiting-using-a-mobile-device
language: bn
status: publish
published_at: '2014-04-13T08:04:47'
published_at_gmt: '2014-04-13T02:04:47'
modified_at: '2015-11-28T09:48:49'
modified_at_gmt: '2015-11-28T03:48:49'
original_url: https://www.shamokaldarpon.com/4136/check-if-the-user-is-visiting-using-a-mobile-device
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- Android
- BlackBerry
- Device
- Function
- Kindle
- Mobile
- Mobile Device
- opera mini
- OperaMobi
- Silk
- ফাংশন
content_hash: 518120dc4d416b0a754ea36b0a75bdcb59a99f060c591510a6a8c4cddb3654d1
archived_at: '2026-11-12T08:35:21.936750+00:00'
---

অনেক সময় দেখা যায় ফেসবুক বা অন্য কোন ওয়েবসাইট মোবাইলে ব্রাউজ করলে একটি ব্যানার বা ম্যাসেজ আসে যা ডেক্সটপে ব্রাউজ করলে আসে না। এটি ওয়ার্ডপ্রেসের একটি ফাংশন ব্যাবহার করে করা যাবে।

```

<?php
if( wp_is_mobile() ) {
  /* Code for Mobile Device */
} else {
  /* Code for Non-Mobile Device */
}
?>
```

এখানে রেজুলেশন বা উইন্ডোর সাইজ বিবেচনা করা হয় না, শুধু মাত্র Mobile, Android, Silk/, Kindle, BlackBerry, Opera Mini, OperaMobi চেক করা হয়।  
বিস্তারিত : [ওয়ার্ডপ্রেস কোডেক্স](https://codex.wordpress.org/Function_Reference/wp_is_mobile)
