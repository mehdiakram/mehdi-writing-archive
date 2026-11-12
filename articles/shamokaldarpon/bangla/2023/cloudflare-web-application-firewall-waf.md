---
archive_id: shamokaldarpon-5930
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 5930
title: ক্লাউডফ্লেয়ারের ওয়েব অ্যাপ্লিকেশন ফায়ারওয়াল (WAF)
slug: cloudflare-web-application-firewall-waf
language: bn
status: publish
published_at: '2023-12-10T09:50:43'
published_at_gmt: '2023-12-10T03:50:43'
modified_at: '2023-12-09T15:03:13'
modified_at_gmt: '2023-12-09T09:03:13'
original_url: https://www.shamokaldarpon.com/5930/cloudflare-web-application-firewall-waf
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
- ওয়েবসাইট
- হ্যাকিং / নিরাপত্তা
tags:
- admin
- Allow
- Block
- Bots
- Challenge
- cloudflare
- Login
- Managed
- Security
- WAF
- wp-admin
- wp-login
- xmlrpc
- ওয়েব অ্যাপ্লিকেশন
- ক্লাউডফ্লেয়ার
- নিরাপত্তা
- ফায়ারওয়াল
content_hash: 8f23e38583c512f134d2c0c5fc8b850b0f974e418c75adf950f9958dbafa2c29
archived_at: '2026-11-12T08:36:39.542002+00:00'
---

আপনি যদি একজন ওয়েবমাস্টার হন তাহলে ওয়েবসাইটের নিরাপত্তা আপনার শীর্ষ অগ্রাধিকারগুলির মধ্যে একটি হতে হবে। আপনার ওয়েবসাইট ক্লাউডফ্লেয়ার এ যুক্ত থাকলে ক্লাউডফ্লেয়ারের ওয়েব অ্যাপ্লিকেশন ফায়ারওয়াল (WAF) এর মাধ্যমে আপনার সাইটের নিরাপত্তা আরো উন্নত করতে পারেন।

![](https://www.shamokaldarpon.com/wp-content/uploads/2023/12/Cloudflare-WAF-1024x510.png)

**কিভাবে রুল তৈরী করবেন?**  
আমরা ওয়েবসাইট লগইন করতে গেলে যেন ক্যাপচা চাই এমন একটি রুল তৈরী করে দেখবো।

প্রথমে ক্লাউডফ্লেয়ারে লগইন করুন এবং নির্দিষ্ট ওয়েবসাইট ক্লিক করুন।  
এবার বাম পাশের মেনু থেকে Security > WAF এ ক্লিক করুন।  
এখন Custom rules ট্যাব থেকে +Create rule বাটনে ক্লিক করুন।  
এখানে রুলের নাম দিন , আমরা Login Challenge নামটি দিলাম।  
If incoming requests match… এর Field থেকে URI Path নির্বাচন করে Operator এ equals রেখে Value তে /admin লিখে Or বাটনে ক্লিক করবো। এভাবে আবার URI Path এ /login লিখে Or বাটনে ক্লিক করবো। একই ভাবে /wp-admin, /wp-login.php, /xmlrpc.php দিবো ।  
অথবা Edit expression এ ক্লিক করে নিচের কোডগুলো লিখবো।

```
(http.request.uri.path eq "/admin")
or (http.request.uri.path eq "/login")
or (http.request.uri.path eq "/wp-admin")
or (http.request.uri.path eq "/wp-login.php")
or (http.request.uri.path eq "/xmlrpc.php")
```

![](https://www.shamokaldarpon.com/wp-content/uploads/2023/12/Login-Challenge-1024x840.jpg)

উপরোক্ত কোড ওয়ার্ডপ্রেস সাইটের জন্য, আপনি চাইলে অনান্য লগইন ইউআআরএল ব্যবহার করতে পারেন।

> > এবার নিচের Then take action… এর Choose action এ Managed Challenge নির্বাচন করে Deploy বাটনে ক্লিক করবো।

তাহলে উপরোক্ত লিংকে গেলে ক্লাউডফ্লেয়ারে এর Managed Challenge পার হয়ে আসতে হবে ফলে বট দ্বারা লগইন করতে গেলে ব্যর্থ হবে।  
পরর্তীতে বাম পাশের মেনু থেকে Security > Events এ ক্লিক করে দেখতে পারবেন কতগুলো ইভেন্ট তৈরী হয়েছে।

**বাংলাদেশের বাইরে থেকে লগইন ব্লক করার রুল তৈরী করা**

```
((http.request.uri.path contains "/xmlrpc.php") 
or (http.request.uri.path contains "/wp-login.php")
or (http.request.uri.path contains "/login")
or (http.request.uri.path contains "/wp-admin/" and not http.request.uri.path contains "/wp-admin/admin-ajax.php" and not http.request.uri.path contains "/wp-admin/theme-editor.php")) 
and ip.geoip.country ne "BD"
```

![](https://www.shamokaldarpon.com/wp-content/uploads/2023/12/Login-Block-without-BD-1024x520.jpg)

**Spam Comment রুল তৈরী করা**

Field: URI  
Operator: equals  
Value: wp-comments-post.php

AND

Field: Request Method  
Operator: equals  
Value: POST

AND

Field: Referer  
Operator: does not contains  
Value: [example.com]

```
(http.request.uri eq "wp-comments-post.php" and http.request.method eq "POST" and not http.referer contains "example.com")
```

![](https://www.shamokaldarpon.com/wp-content/uploads/2023/12/Spam-Comment-1024x769.jpg)

এখানে example.com এর যায়গায় আপনার ওয়েবসাইট ইউআরএল দিবেন। এরপরে Then take action এ JS Challenge নির্বাচন করে Deploy বাটনে ক্লিক করবো।

**HTTP 1.0 ব্লক রুল তৈরী করা**

![](https://www.shamokaldarpon.com/wp-content/uploads/2023/12/HTTP1-1024x569.jpg)

ক্লাউডফ্লেয়ারের ফ্রি প্ল্যান ব্যবহার করলে ৫টি কাষ্টম রুল তৈরী করা যাবে।  
এছাড়াও নিচের রুল বা ফিচার সেট করে রাখবেন।

\* Security > Bots থেকে বট ফাইট মোড অন করে রাখবেন।

\* আপনার নির্দিষ্ট দেশ বা আইপিকে যদি Allow/Block/Challenge সেট করাতে চান তাহলে , ড্যাশবোর্ড বামপাশের মেনু থেকে Security > WAF এ যান এবং Tools ট্যাবে গিয়ে IP, IP range, country name, or ASN এ ক্লিক করুন এবার এবং উক্ত দেশ বা IP লিখুন এবং Action এর ড্রপ-ডাউন মেনু থেকে Allow/Block/Challenge নির্বাচন করুন।
