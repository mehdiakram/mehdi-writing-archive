---
archive_id: shamokaldarpon-6313
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 6313
title: Cloudflare + Gmail দিয়ে আজীবন ফ্রি প্রফেশনাল ইমেইল
slug: cloudflare-gmail-free-professional-email-setup
language: bn
status: publish
published_at: '2026-03-01T16:17:16'
published_at_gmt: '2026-03-01T10:17:16'
modified_at: '2026-03-01T16:17:56'
modified_at_gmt: '2026-03-01T10:17:56'
original_url: https://www.shamokaldarpon.com/6313/cloudflare-gmail-free-professional-email-setup
author: মেহেদী আকরাম
categories:
- টিপস এন্ড ট্রিকস
- ডোমেইন হোষ্টিং
tags:
- cloudflare
- DNS
- Email
- gmail
- Google
- Mail
- MX
- professional-email
- split delivery
- Two Mail Server
- txt
- Workspace
- zoho
- ইমেইল
- জিমেইল
- ডুয়েল ডেলিভারি
- ফ্রি
- মেইল
content_hash: 17bf10b95bc697056189e5d9f16dc2bc7dc6109b1b5ce2004b43b86ab01e11fe
archived_at: '2026-11-12T08:36:44.642004+00:00'
---

আপনার ইমেইল এখনো যদি সাধারণ `@gmail.com` দিয়ে শেষ হয়, চিন্তার কিছু নেই। কিন্তু বাস্তবতা হলো—২০২৬ সালে ক্লায়েন্টরা ইমেইল দেখেই প্রফেশনালিজম আন্দাজ করে। অনেক সময় স্কিল দেখার আগেই তারা সিদ্ধান্ত নিয়ে ফেলে।

একটা কাস্টম ইমেইল যেমন `hello@yourname.com` আপনাকে আলাদা করে তুলে ধরে। আর ভালো খবর হলো, এর জন্য বছরে ৭২ ডলার দিয়ে সাবস্ক্রিপশন নেওয়া বাধ্যতামূলক না। অল্প সময় দিলেই ফ্রিতে সেটআপ করা যায়।

![](https://www.shamokaldarpon.com/wp-content/uploads/2026/03/Cloudflare-Gmail.jpg)

## ধাপ ১: ডোমেইনই আসল ভিত্তি

প্রথম কাজ হলো নিজের নামে একটি ডোমেইন নেওয়া। এটা আপনার অনলাইন পরিচয়ের কেন্দ্র।

আপনি চাইলে **[Royal Technologies](https://www.royaltechbd.com/)** থেকে ডোমেইন কিনতে পারেন।

ডোমেইন কেনার সময় .com পেলে ভালো, না হলে .co বা .net-ও নিতে পারেন। গুরুত্বপূর্ণ হলো—নামটা যেন পরিষ্কার, ছোট এবং ব্র্যান্ডেবল হয়।

## ধাপ ২: Cloudflare দিয়ে DNS নিয়ন্ত্রণে নিন

ডোমেইন কেনার পর সেটিকে কানেক্ট করতে হবে **Cloudflare**-এর সাথে।

Cloudflare-এ একটি ফ্রি অ্যাকাউন্ট খুলুন। তারপর “Add a Site” অপশনে গিয়ে আপনার ডোমেইন যুক্ত করুন।

Cloudflare আপনাকে দুটি নতুন nameserver দেবে।  
এগুলো কপি করে আপনার ডোমেইন প্রোভাইডারের DNS সেটিংসে বসিয়ে দিন।

সাধারণত ১০–৩০ মিনিটের মধ্যে আপডেট হয়ে যায়। এই ধাপটা গুরুত্বপূর্ণ, কারণ এখান থেকেই আমরা ইমেইল রাউটিং কন্ট্রোল করবো।

## ধাপ ৩: Email Routing চালু করুন

এখন মূল ম্যাজিক।

Cloudflare ড্যাশবোর্ডে গিয়ে Email → Email Routing অপশন চালু করুন।

এখানে আপনি যেমন চাইবেন তেমন কাস্টম ইমেইল তৈরি করতে পারবেন:

- hello@yourdomain.com
- contact@yourdomain.com
- support@yourdomain.com

Destination হিসেবে আপনার রেগুলার Gmail ঠিকানাটি দিন।

Cloudflare আপনার Gmail-এ একটি ভেরিফিকেশন মেইল পাঠাবে। সেটি কনফার্ম করলেই রাউটিং সক্রিয় হয়ে যাবে।

এখন থেকে আপনার ডোমেইনের যেকোনো ইমেইল সরাসরি Gmail-এ এসে পৌঁছাবে।

## ধাপ ৪: Gmail থেকে কাস্টম ইমেইল দিয়ে রিপ্লাই

শুধু রিসিভ করলে হবে না, ক্লায়েন্টকে রিপ্লাইও করতে হবে কাস্টম ঠিকানা থেকে।

Gmail ওপেন করুন → Settings → See all settings → Accounts and Import।

“Send mail as” থেকে নতুন ইমেইল অ্যাড করুন। সেখানে আপনার কাস্টম ইমেইলটি বসান।

এখানে Gmail SMTP ব্যবহার করা হবে, তাই সঠিক অথেনটিকেশন দরকার।

## ধাপ ৫: App Password ব্যবহার করুন

সাধারণ Gmail পাসওয়ার্ড এখানে কাজ করবে না।

আপনার Google Account-এ 2-Step Verification অন করুন।  
তারপর “App passwords” অপশন থেকে একটি ১৬-অক্ষরের নতুন পাসওয়ার্ড জেনারেট করুন।

এই পাসওয়ার্ডটি Gmail-এর “Send mail as” সেটআপে ব্যবহার করুন।

এতে করে নিরাপদভাবে আপনার কাস্টম ইমেইল Gmail-এর মাধ্যমে পাঠানো সম্ভব হবে।

## ধাপ ৬: SPF রেকর্ড না দিলে সমস্যা হবে

অনেকেই এই অংশটি বাদ দেয়। তারপর দেখে সব মেইল স্প্যামে যাচ্ছে।

Cloudflare DNS → Records এ গিয়ে একটি TXT রেকর্ড যোগ করুন:

Name: @  
Content:  
v=spf1 include:\_spf.google.com ~all

এটি প্রমাণ করে যে Gmail আপনার ডোমেইনের পক্ষ থেকে ইমেইল পাঠাতে অনুমোদিত। ফলে ইনবক্সে পৌঁছানোর সম্ভাবনা অনেক বেড়ে যায়।

## বাড়তি টিপ: আলাদা ব্র্যান্ড ইমেজ তৈরি করুন

আপনি চাইলে:

- info@yourdomain.com
- billing@yourdomain.com
- careers@yourdomain.com

এভাবে আলাদা আলাদা অ্যাড্রেস তৈরি করতে পারেন।

সবগুলোই একই Gmail-এ আসবে, কিন্তু ক্লায়েন্টের কাছে আপনার কাজ অনেক বেশি সংগঠিত এবং প্রফেশনাল মনে হবে।

একটি কাস্টম ইমেইল মানে শুধু নতুন ঠিকানা না। এটা আপনার ব্র্যান্ডের অংশ।
