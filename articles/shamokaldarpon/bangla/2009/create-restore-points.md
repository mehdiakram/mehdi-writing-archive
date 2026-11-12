---
archive_id: shamokaldarpon-1089
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 1089
title: তৈরী করুন সিস্টেম রিস্টোর পয়েন্ট
slug: create-restore-points
language: bn
status: publish
published_at: '2009-02-14T09:38:20'
published_at_gmt: '2009-02-14T03:38:20'
modified_at: '2009-02-14T09:38:20'
modified_at_gmt: '2009-02-14T03:38:20'
original_url: https://www.shamokaldarpon.com/1089/create-restore-points
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Points
- restore
- System
- System Restore
- Tips
- উইন্ডোজ
- টিপস
- পয়েন্ট
- রিস্টোর
- সিস্টেম
content_hash: 1d20caa2e432d6c32075a15abdbfe8a4d086ad3cfef976358b1ef44b2187e9de
archived_at: '2026-11-12T08:34:41.258455+00:00'
---

উইন্ডোজে তথ্য মুছে গেলে বা ভাইরাসে আক্রান্ত হলে আমরা সাধারণত সিস্টেম রিস্টোর করে থাকি। সিস্টেম রিস্টোর সক্রিয় থাকলে আপনি এই সুবিধা পাবেন। আর এজন্য প্রয়োজন হয় সিস্টেম রিস্টোর পয়েন্ট। কিন্তু ম্যানুয়ালী সিস্টেম রিস্টোর পয়েন্ট তৈরী করার সাধারণ পথ নেই। কিন্তু একটি ভিবিএস ফাইলের দ্বারা আপনি সহজেই সিস্টেম রিস্টোর পয়েন্ট তৈরী করতে পারেন। এজন্য নিচের দুই লাইনের সংকেতগুলো নোটপ্যাডে লিখে RestorePoint.vbs নামে করুন।

Set IRP = getobject(“winmgmts:\\.\root\default:Systemrestore”)  
MYRP = IRP.createrestorepoint (“My Restore Point”, 0, 100)

ব্যাস এরপর থেকে যখনই আপনি RestorePoint ফাইলে ডাবল ক্লিক করবেন তখনই সিস্টেম রিস্টোর পয়েন্ট তৈরী হবে।
