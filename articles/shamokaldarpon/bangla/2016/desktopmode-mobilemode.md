---
archive_id: shamokaldarpon-4522
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4522
title: ‌ওয়েবসাইট ভিজিেটর সময় ডেক্সটপ/মোবাইল ভিউ দেখানো
slug: desktopmode-mobilemode
language: bn
status: publish
published_at: '2016-04-04T10:34:53'
published_at_gmt: '2016-04-04T04:34:53'
modified_at: '2016-06-15T15:28:44'
modified_at_gmt: '2016-06-15T09:28:44'
original_url: https://www.shamokaldarpon.com/4522/desktopmode-mobilemode
author: মেহেদী আকরাম
categories:
- ওয়েব ডিজাইন এবং ডেভেলপমেন্ট
tags: []
content_hash: aa8f14a24a4b746b92ade4dac8392eacb18d019f9505daff60102271ecc173b4
archived_at: '2026-11-12T08:35:24.653027+00:00'
---

বর্তমানে ‌ওয়েবসাইট ডিজাইন করলে প্রায় সকলই রেসপনসিভ ডিজাইন করে। স্মার্ট ডিভাইসে ওয়েবসাইটের দেখে অনেক বেশী বেড়ে গেছে। মিডিয়া কুয়েরির মাধ্যমে রেসপনসিভ করলে মোবাইল বা ছোট ডিভাইসে সয়ংক্রিয়ভাবে রেসপনসিভ ভিউ আসে। এক্ষেত্রে ভিউয়াররা চাইলেই ডেক্সটপের মত ভিউ মোবাইলে দেখতে পারে না। তবে অনেক সাইটেই Switch To Desktop View এবং Switch To Mobile View লিংক থাকে যার সাহায্যে স্মার্ট ডিভাইসের ব্যবহারকারীরা প্রয়োজনে ডেক্সটপ ভিউ (নন রেসপনসিভ ভিউ) দেখতে পারেন।  
![responsive-web-design-icon](http://www.shamokaldarpon.com/wp-content/uploads/responsive-web-design-icon-300x199.png)  
আপনি যদি চান তাহলে আপনার ‌ওয়েবসাইটের ভিউয়ারদের এমন সুযোগ দিতে পারেন। এজন্য সামান্য কিছু কোড যুক্ত করতে হবে।

নিচের কোড <head>ট্যাগ শুরু হবার পরে লিখুন

```
<?php session_start(); ?>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<?php
if($_GET['show_desktop_mode'] == 'true') {
$_SESSION['desktopmode'] = 'true';
}
else if($_GET['show_desktop_mode'] == 'false') {
$_SESSION['desktopmode'] = 'false';
}
if($_SESSION['desktopmode'] == 'true') {
/* DESKTOP MODE */
?>
<meta name="viewport" content="width=1170">
<?php
} 
else {
/* DEFAULT*/
?>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="<?php bloginfo('template_url'); ?>/responsive.css" rel="stylesheet">
<?php
}
?>
Which 
```

\*এখানে রেসপনসিভ সিএসএসগুলো responsive.css ফাইলে আলাদা করা হয়েছে।  
এবার ফুটারের যেখানে ডেক্সটপ/মোবাইল সুইচ করার লিংক দিতে চান সেখানে নিচের কোড লিখুন।

```
<p>
<?php if($_SESSION['desktopmode'] == 'false') { ?>
<p id="desktopmode"><a href="?show_desktop_mode=true">Switch To Desktop View</a></p>
<?php } elseif($_SESSION['desktopmode'] == 'true') { ?>
<p id="mobilemode"><a href="?show_desktop_mode=false">Switch To Mobile View</a></p>
<?php } else { ?>
<p id="mobilemode"><a href="?show_desktop_mode=true">Switch To Desktop View</a></p>
<?php } ?>
</p>
```

এর পরে ডিফল্ট সিএসএস-এ নিচের কোড লিখুন।

```
#mobilemode, #desktopmode{text-align:center; display:none;}
#footer a, #mobilemode a, #desktopmode a{color:#fff;}

@media(max-width:1199px ){
#mobilemode, #desktopmode {display:block;}
}
```

উপরোক্ত সিএসএস কোডের কালার বা এ্যলাইনমেন্ট ইচ্ছামত দিন।  
এবার দেখুন কাজ করছে কি না।  
\*উপরোক্ত কোডে কিছু ‌ওয়ার্ডপ্রেসের কোড যুক্ত আছে। ‌ওয়ার্ডপ্রেস ছাড়া ব্যবহার করতে চাইলে পরিবর্তন করে নিতে হবে।
