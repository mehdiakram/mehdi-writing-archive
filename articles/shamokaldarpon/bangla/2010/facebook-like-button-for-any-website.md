---
archive_id: shamokaldarpon-2156
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 2156
title: যেকোন সাইটের জন্য ফেসবুকের লাইক বাটন
slug: facebook-like-button-for-any-website
language: bn
status: publish
published_at: '2010-04-26T15:28:10'
published_at_gmt: '2010-04-26T09:28:10'
modified_at: '2023-11-01T09:59:08'
modified_at_gmt: '2023-11-01T03:59:08'
original_url: https://www.shamokaldarpon.com/2156/facebook-like-button-for-any-website
author: মেহেদী আকরাম
categories:
- ব্রাউজার
tags:
- Google Crome
- Internet
- Like
- Like Button
- plugins
- ফেসবুক
- লাইক
content_hash: 742b91bf5cc49aec499ff996c9a1fc50fadc28292da6f3cde5f570147e03cd70
archived_at: '2026-11-12T08:35:42.436427+00:00'
---

জনপ্রিয় সামাজিক নেটওয়ার্কি সাইট ফেসবুক সমপ্রতি লাইক বাটন অবমুক্ত করেছে। এই বাটনে সাহায্যে যেকোন ওয়েবসাইটকে লাইক করা যাবে। ফেসবুকের প্লাগইনের মাধ্যমে ওয়েবসাইটে থেকে এবং সরাসরি গুগল ক্রোমে থেকে লাইক করা যাবে।   
গুগল ক্রোমে লাইক বাটন: ক্রোমের এক্সটেনশনটি <https://chrome.google.com/extensions/detail/ocfhgijcimpoffgcapmbnheggfgfiime> থেকে ইনস্টল করুন তাহলে গুগল ক্রোমের এড্রেসাবরের ডানে Facebook Likes বাটন আসবে। এখন এখানে লাইক বাটনে ক্লিক করলে বর্তমান সাইটটি লাইক হিসাবে গৃহীত হবে এবং ফেসবুকের ওয়ালে তা প্রদর্শন করবে। ফেসবুকে যদি লগইন করা না থাকে তাহলে লাইক বাটনে ক্লিক করার পরে লগইন করার উইন্ডো থেকে লগইন করতে হবে।  
কোন নির্দিষ্ট সাইটে ফেসবুক লাইক বাটন ব্যবহার করতে চাইলে <http://developers.facebook.com/docs/reference/plugins/like> সাইটে গিয়ে সাইটের নাম লিখে প্রয়োজনীয় পরিবর্তন করে Get Code বাটনে ক্লিক করলে iframe এবং XFBML দুই ধরনের প্রোগ্রামিং কোড আসবে। আর ওয়ার্ডপ্রেসের জন্য নিচের কোড ব্যবহার করতে পারেন।

```

<iframe src="http://www.facebook.com/plugins/like.php?href=<?php echo urlencode(get_permalink()); ?>&amp;layout=standard&amp;show-faces=true&amp;width=530&amp;height=60&amp;action=like&amp;colorscheme=light" scrolling="no" frameborder="0" allowTransparency="true" style="border:none; overflow:hidden; width:530px; height:60px"></iframe>
```
