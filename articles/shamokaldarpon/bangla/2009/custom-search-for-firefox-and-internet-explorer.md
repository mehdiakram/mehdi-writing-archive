---
archive_id: shamokaldarpon-1773
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 1773
title: ফায়ারফক্স এবং ইন্টারনেট এক্সপ্লোরারের জন্য কাস্টম সার্চ ইঞ্জিন
slug: custom-search-for-firefox-and-internet-explorer
language: bn
status: publish
published_at: '2009-10-15T00:02:23'
published_at_gmt: '2009-10-14T17:02:23'
modified_at: '2023-11-01T10:21:27'
modified_at_gmt: '2023-11-01T04:21:27'
original_url: https://www.shamokaldarpon.com/1773/custom-search-for-firefox-and-internet-explorer
author: মেহেদী আকরাম
categories:
- টিপস এন্ড ট্রিকস
tags:
- ৭+
- Custom
- Engine
- Explorer
- Firefox
- IE
- IE7+
- Internet
- Internet Explorer
- Search
- Search Engine
- SearchTerms
- XML
- ইঞ্জিন
- ইন্টারনেট
- ইন্টারনেট এক্সপ্লোর
- এক্সপ্লোরার
- কাস্টম
- ফায়ারফক্স
- ব্রাউজার
- সার্চ
- সার্চ ইঞ্জিন
content_hash: ba0ec4e1786ce5fc1c66b8b876f2717f6fadaa8fcbfa2efff5ae9145835c7b31
archived_at: '2026-11-12T08:35:52.083631+00:00'
---

ওপেন সোর্স ওয়েব ব্রাউজার মজিলা ফায়ারফক্স বা ইন্টারনেট এক্সপ্লোরারে (৭+) সার্চ ইঞ্জিনে না ঢুকে ব্রাউজারের যুক্ত থাকা কাস্টম সার্চ ইঞ্জিনের মাধ্যমে সার্চ করা যায়। এখানে কিছু সাইটের কাস্টম সার্চ ইঞ্জিন যুক্ত করা থাকে। ব্লগ বা যেসব ওয়েব সাইটে সার্চ করার সুযোগ আছে সেসব সাইটে এমন সার্চ ইঞ্জিন থাকলে তা মজিলা ফায়ারফক্সে বা ইন্টারনেট এক্সপ্লোরার ৭ বা পরবর্তী সংস্করণে কাস্টম সার্চ ইঞ্জিন হিসাবে যুক্ত করা যাবে। এখন দেখবো কিভাবে এমন কাস্টম সার্চ ইঞ্জিন তৈরী করে সাইটে যুক্ত করা এবং ব্রাউজারে যুক্ত করা যায়।  
প্রথমে নিচের সংকেত নোট প্যাডে লিখে search.xml নামে সেভ করুন এবং সাইটের মূল রুটে আপলোড করুন।  
[php]  
<?xml version="1.0" encoding="UTF-8"?>  
<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/" xmlns:moz="http://www.mozilla.org/2006/browser/search/">  
<!– Created on Tue, 10 Nov 2009 14:42:59 GMT –>  
<ShortName>Shamokal Darpon Search</ShortName>  
<Description>Shamokal Darpon Search</Description>  
<Url type="text/html" method="get" template="http://www.shamokaldarpon.com/?s={searchTerms}"/>  
<Contact>mehdi.akram@gmail.com</Contact>  
<Image width="16" height="16">http://mycroft.mozdev.org/updateos.php/id0/mehdiakram.ico</Image>  
<Developer>S.M. Mehdi Akram</Developer>  
<InputEncoding>UTF-8</InputEncoding>  
<moz:SearchForm>http://www.shamokalDarpon.com</moz:SearchForm>  
<Url type="application/opensearchdescription+xml" rel="self" template="http://mycroft.mozdev.org/updateos.php/id0/mehdiakram.xml"/>  
<moz:UpdateUrl>http://mycroft.mozdev.org/updateos.php/id0/mehdiakram.xml</moz:UpdateUrl>  
</OpenSearchDescription>  
[/php]  
**কোড বিশ্লেষণ:** ৩য় লাইনে সার্চ ইঞ্জিনের নাম দেওয়া হয়েছে। ৪র্থ লাইনে সার্চ ইঞ্জিনের বর্ণনা দেওয়া আছে। ৫ম লাইনে সার্চ ইঞ্জিনে কোন আইকন দেখাবে তার ঠিকানা দেওয়া আছে। ৬ষ্ট লাইনে সার্চের ফলাফল কোন পাতাতে দেখাবে তা দেওয়া হয়েছে ({searchTerms}এর আগের টুক)।  
এখন সাইটের মূল ফাইলে (হেডার) নিচের কোড যুক্ত করুন। যা আপলোড করা search.xml ফাইলের লোকেশন এবং টাইটেল দেওয়া আছে। যে সাইটের জন্য সার্চ ইঞ্জিন তৈরী করতে চান সেট সাইটের উপযোগী তথ্য দিতে হবে।  
[php]<link rel=”search” href=”http://www.shamokaldarpon.com/search.xml” title=”Shamokal Darpon Search” />[/php]  
এবার সাইটি ব্রাউজ করলে কাস্টম সার্চ ইঞ্জিনের যায়গায় উজ্জল তারকা দেখাবে যেখানে ক্লিক করে উক্ত সাইটের যুক্ত থাকা সার্চ ইঞ্জিনটি যুক্ত করা যাবে।  
বিস্তারিত সার্চ ইঞ্জিন ব্রাউজারে যুক্ত করার পদ্ধতি ভিডিওসহ পাবেন [www.shamokaldarpon.com/?p=1549](http://www.shamokaldarpon.com/?p=1549) এখানে।
