---
archive_id: shamokaldarpon-1321
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 1321
title: উইন্ডোজ থেকে লিনাক্স পার্টিশন দেখা
slug: view-linux-partition-from-windows
language: bn
status: publish
published_at: '2009-05-16T10:27:05'
published_at_gmt: '2009-05-16T04:27:05'
modified_at: '2023-11-01T10:25:08'
modified_at_gmt: '2023-11-01T04:25:08'
original_url: https://www.shamokaldarpon.com/1321/view-linux-partition-from-windows
author: মেহেদী আকরাম
categories:
- টিপস এন্ড ট্রিকস
tags:
- Access
- ext2
- ext3
- File System
- fs-driver
- Linux Partitions
- Partitions
- Software
- Tips
- উইন্ডোজ
- ডাউনলোড
- পার্টিশন
- লিনাক্স
content_hash: 7a76616a068d7fe2d700c22e14536165d6ed59c0e09ac79c331a0f3dfb4ab519
archived_at: '2026-11-12T08:36:03.570253+00:00'
---

উইন্ডোজ অপারেটিং সিস্টেমের সাথে অনেকেই লিনাক্স অপারেটিং সিস্টেম ব্যবহার করে থাকেন। লিনাক্সের ফাইল সিস্টেম সাধারণত ext2 বা ext3 হয়ে থাকে। ফলে লিনাক্স থেকে উইন্ডোজের NTFS বা FAT ড্রাইভগুলো দেখা গেলেও উইন্ডোজ থেকে ext2 বা ext3 ফাইল সিস্টেমের ড্রাইভগুলো দেখা যায় না। উইন্ডোজ থেকে লিনাক্সের ড্রাইভ দেখার বেশ কিছু সফটওয়্যার আছে। এগুলোর মধ্যে Ext2 Installable File System For Windows অন্যতম। ১.৩৯ মেগাবাইটের এই সফটওয়্যারটি [www.fs-driver.org](http://www.fs-driver.org) থেকে ডাউনলোড করুন। এবার সফটওয়্যারটি চালু করে উইজার্ডে ৫বার Next করুন। তাহলে কোন কোন ড্রাইভ ext2 বা ext3 আছে তা দেখাবে। এবার যে যে ড্রাইভগুলো দেখতে চান তার ড্রাইভ লেটার নির্বাচন করে ২বার Next করে Finish করুন। এবার দেখুন উক্ত ড্রাইভটি দেখা যাচ্ছে। এরপর থেকে নির্দিষ্ট ড্রাইভগুলো দেখাবে। এটি বন্ধ করতে চাইলে Control Panel/Add or Remove Programs থেকে আনইনস্টল করতে হবে।
