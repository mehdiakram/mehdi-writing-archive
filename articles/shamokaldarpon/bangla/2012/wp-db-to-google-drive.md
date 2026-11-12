---
archive_id: shamokaldarpon-3100
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 3100
title: ওয়ার্ডপ্রেসের ডাটাবেজ এবং ডাটাকে সয়ংক্রিয়ভাবে ব্যাকআপ রাখুন গুগল ড্রাইভে
slug: wp-db-to-google-drive
language: bn
status: publish
published_at: '2012-08-02T07:29:44'
published_at_gmt: '2012-08-02T01:29:44'
modified_at: '2014-10-12T17:51:50'
modified_at_gmt: '2014-10-12T11:51:50'
original_url: https://www.shamokaldarpon.com/3100/wp-db-to-google-drive
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- Backup
- plugin
- ওয়ার্ডপ্রেস
- গুগল ড্রাইভ
- ব্যাকআপ
content_hash: 9f79e6fd180146498417a655b64f5a04ae4fc14634e8a99e08e1d609576d4a0d
archived_at: '2026-11-12T08:35:14.566893+00:00'
---

ওয়েবসাইটকে নিয়মিত ব্যাকআপ রাখা বাঞ্চনিয়। ওয়েবমাষ্টাররা বিভিন্নভাবে তাদের ওয়েবসাইট ব্যাকআপ রাখতে পারেন। জনপ্রিয় ব্লগিং সিএমএস ওয়ার্ডপ্রেস এর ডাটাবেজ সহ ফাইল/ফোল্ডারগুলোকে নিয়মিত মেইলে বিভিন্ন প্লাগইনস দ্বারা। মেইলে ব্যাকআপের ৰেত্রে সাইট বড় হয়ে মেইল আসে না সেৰেত্রে নিয়মিত ব্যাকআপ রাখা হয় না সেৰেত্রে গুগল ড্রাইভে ব্যাকআপ নেওয়া যেতে পারে। গুগল ড্রাইভে ব্যাকআপ নেওয়ার দারুন একটি সফটওয়্যার হচ্ছে Google Drive for WordPress।  
> প্রথমে <http://wordpress.org/extend/plugins/wp-google-drive/> থেকে প্লাগইনটি ইনস্টল করে অ্যাকটিভ করুন।  
> এবার বাম পাশের প্যানেলে Configure Google এ ক্লিক করে Client ID এবং Client secret লিখুন।  
![wp-google](http://farm9.staticflickr.com/8019/7696284906_a69ce12aa0_b.jpg)  
> Client ID এবং Client secret পাবার জন্য Google API Console লিংকে ক্লিক করে অথবা সরাসরি https://code.google.com/apis/console/ সাইটে গিয়ে লগইন করুন।  
> এখন Create project… বাটনে ক্লিক করে বাম পাশের প্যানেল থেকে API Access এ ক্লিক করুন এবং Create an OAuth 2.0 client ID বাটনে ক্লিক করুন তাহলে পপআপ উইন্ডো আসবে।  
> এখানে প্রোডাক্টের নাম এবং লগো দিয়ে Next বাটনে ক্লিক করুন।  
> এবার Web Application নির্বাচিত রেখে Your site or hostname অপশনের More Options ক্লিক করুন এবং Authorized Redirect URIs এ পৱাগইন কনফিগারের লিংক এবং Authorized JavaScript Origins এ সাইটের ঠিকানা লিখে Create Client ID বাটনে ক্লিক করুন।  
![wp-google](http://farm9.staticflickr.com/8024/7696284780_a4141b5c8b_b.jpg)  
> এখানে Client ID এবং Client secret পাবেন যা পৱাগইন কনফিগারে লিখে Allow Access বাটনে ক্লিক করুন।  
> এবার গুগলের Allow Access বাটনে ক্লিক করুন।  
> সবশেষে Backup Settings, Manage Database, Manage Files, One-Time Full Backup গুলোতে গিয়ে ব্যাকআপ সিডিউল, ফোল্ডারের নাম ইত্যাদি সেট করুন।  
এখন থেকে নিয়মিত সাইটের ব্যাকআপ গুগল ড্রাইভে চলে আসবে।
