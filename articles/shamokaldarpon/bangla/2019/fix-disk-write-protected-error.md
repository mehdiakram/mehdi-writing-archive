---
archive_id: shamokaldarpon-4774
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4774
title: ডিক্স রাইট প্রটেক্টেড হলে করনিয়
slug: fix-disk-write-protected-error
language: bn
status: publish
published_at: '2019-09-03T13:51:44'
published_at_gmt: '2019-09-03T07:51:44'
modified_at: '2019-09-03T13:54:40'
modified_at_gmt: '2019-09-03T07:54:40'
original_url: https://www.shamokaldarpon.com/4774/fix-disk-write-protected-error
author: মেহেদী আকরাম
categories:
- হ্যাকিং / নিরাপত্তা
tags:
- Attribute
- Attribute Changer
- files
- Folder
- Freeware
- Hidden
- Hidden Attribute
- Hidden Files
- Hide
- petges
- System
- Unhide
- Virus
- write-protected
- write-protected error
- এট্রিবিউট
- চেঞ্জ
- ভাইরাস
content_hash: d2aedf1462ffaa1076e9a457a26f123e9b6eb67384fe216d88529111c464b035
archived_at: '2026-11-12T08:35:28.212153+00:00'
---

ভাইরাস বা অন্য কোন কারনে অনেক সময় পেনড্রাইভ/ফ্লাশ ডিক্স রাইট প্রটেক্টেড হয়ে যায়। ফরম্যেট করলেই হয় না, এরর দেখায়। তখন চাইলে কমান্ড প্রোমম্টের মাধ্যমে পেনড্রাইভ/ফ্লাশ ডিক্স রাইট প্রটেক্টেড/রিডঅনলি রিমুভ করা যায়।  
এজন্য পেনড্রাইভ/ফ্লাশ ডিক্সটি কম্পিউটারে কানেক্ট করে কমান্ড প্রোমম্ট এ্যাডমিনিষ্ট্রেটর হিসাবে চালু করতে হবে।  
এবার diskpart লিখে এন্টার করুন।  
এরপরে list disk লিখে এন্টার করুন তাহলে যতগুলো ডিক্স আছে সবগুলোর লিষ্ট দেখাবে। হার্ডডিক্স আর পেনড্রাইভ/ফ্লাশ ডিক্সটি থাকলে হার্ডডিক্সটি disk 0 এবং পেনড্রাইভ/ফ্লাশ ডিক্সটি disk 1 হিসাবে দেখাবে।  
এবার select disk 1 লিখে এন্টার দিলে পেনড্রাইভ/ফ্লাশ ডিক্সটি সিলেক্ট হবে।  
এখন attributes disk clear readonly লিখে এন্টার দিলে পেনড্রাইভ/ফ্লাশ ডিক্সটি রিডঅনলি/রাইট প্রটেক্টেড ক্লিয়ার হয়ে যাবে।

![](http://www.shamokaldarpon.com/wp-content/uploads/2019/09/the-disk-is-write-protected.png)

**কমান্ড বিশ্লেষণ হচ্ছে:**  
diskpart = diskpart কমান্ডে প্রবেশ করা।  
list disk = সিস্টেমে থাকে সকল ডিক্সের লিষ্ট দেখা।  
select disk 1 = ডিক্স ১ নির্বাচন করা।  
attributes disk clear readonly = ডিক্স ১ এর রিডঅনলি/রাইট প্রটেক্টেড ক্লিয়ার করা।  
আর যদি আপনি কোন পেনড্রাইভ/ফ্লাশ ডিক্স/পোর্টেবল হার্ডডিক্সকে রিডঅনলি/রাইট প্রটেক্টেড করতে চান তাহলে attributes disk set readonly কমান্ডটি লিখে এন্টার করলেই উক্ত ডিক্সটি রিডঅনলি/রাইট প্রটেক্টেড হয়ে যাবে।  
এছাড়াও attributes disk এন্টার দিলে সিলেক্ট করা ডিক্সটির এট্রিবিউটসগুলো দেখা যাবে।
