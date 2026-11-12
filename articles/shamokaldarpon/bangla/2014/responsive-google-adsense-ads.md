---
archive_id: shamokaldarpon-4220
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4220
title: গুগল এ্যাডসেন্স এর বিজ্ঞাপন রেসপনসিভ করা
slug: responsive-google-adsense-ads
language: bn
status: publish
published_at: '2014-01-27T11:08:50'
published_at_gmt: '2014-01-27T05:08:50'
modified_at: '2015-11-28T09:47:13'
modified_at_gmt: '2015-11-28T03:47:13'
original_url: https://www.shamokaldarpon.com/4220/responsive-google-adsense-ads
author: মেহেদী আকরাম
categories:
- টিপস এন্ড ট্রিকস
tags:
- Ad
- Adsense
- Google
- Google Adsense
- responsive
- এ্যাডসেন্স
- গুগল
- গুগল এ্যাডসেন্স
- বিজ্ঞাপন
- রেসপনসিভ
content_hash: 63a487b4a950eec731f5feaca41dd2364af45e899f59f1f7c751b540cd9bf6dc
archived_at: '2026-11-12T08:35:21.922578+00:00'
---

অনেক ওয়েবসাইটই দেখা যায় রেসপনসিভ কিন্তু গুগল এ্যাডসেন্সের বিজ্ঞাপন ব্যবহার করা ফলে আর রেসপনসিভ থাকছে না। তবে গুগল বেশ কিছুদিন আগে রেসপনসিভ অ্যাড স্লোট চালু করেছে, ফলে সহজেই রেসপনসিভ অ্যাড ওয়েবসাইটে ব্যবহার করা যায়। নিচের স্ক্রিনশট রেসপনসিভ অ্যাড স্লোটের।  
![Google Responsive Ad Slot](https://mehdiakram.files.wordpress.com/2014/10/responsive-ad1.png)  
এবার নিচে রেসপনসিভ অ্যাড স্লোটের কোডে দেখুন এখানে তিন সাইজের অ্যাড দেখা যাবে ৮০০ পিক্সেলের বেশী হলে ৭২৮\*৯০ সাইজের অ্যাড, ৫০০ পিক্সেলের বেশী হলে ৪৮০\*৬০ সাইজের অ্যাড এবং ৫০০ পিক্সেলের কম হলে ৩২০\*৫০ সাইজের অ্যাড প্রদর্শিত হয়।  
![Google Responsive Ad Code](https://mehdiakram.files.wordpress.com/2014/10/responsive-ad2.png)  
তবে চাইলে নিজের পছন্দমত অ্যাড স্লোট রেসপনসিভ করে ব্যবহার করা যায়। অনেক ভাবেই রেসপনসিভ অ্যাড ব্যবহার করা যায় তবে নিচের পদ্ধতি এখন পর্যন্ত উত্তম মনে হয়েছে। নিচের তিনটা সাইজের রেসপনসিভ অ্যাডের কোড দেখুন।

```
<script type="text/javascript">
google_ad_client = "ca-pub-xxxxxxxxxxxxx";
if (window.innerWidth >= 800) {
google_ad_slot = "7xxxxxxxxxx";
google_ad_width = 728;
google_ad_height = 90;
} else if (window.innerWidth < 400) {
google_ad_slot = "3xxxxxxxxxx";
google_ad_width = 300;
google_ad_height = 250;
} else {
google_ad_slot = "4xxxxxxxxxx";
google_ad_width = 468;
google_ad_height = 60;
}
google_language = 'en';
<script src="//pagead2.googlesyndication.com/pagead/show_ads.js" type="text/javascript"></script>
```

এখানে ব্রাউজারের ওয়াইড যদি ৮০০ পিক্সেল বা তার বেশী হয় তাহলে 7xxxxxxxxxx স্লোটের (৭৮৬\*৯০) অ্যাড দেখাবে।  
ব্রাউজারের ওয়াইড যদি ৪০০ পিক্সেলের কম হয় তাহলে 3xxxxxxxxxx স্লোটের (৩০০\*২৫০) অ্যাড দেখাবে।  
অন্যথায় (ব্রাউজারের ওয়াইড যদি ৪০০ থেকে ৭৯৯ পিক্সেল হয় তাহলে 4xxxxxxxxxx স্লোটের (৪৬৮\*৬৯০) অ্যাড দেখাবে।  
এভাবে আপনি চাইলে ইচ্ছামত সাইজ এবং অ্যাড স্লোট ব্যবহার করতে পারবেন।
