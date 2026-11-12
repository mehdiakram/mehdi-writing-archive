---
archive_id: shamokaldarpon-3647
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 3647
title: ওয়ার্ডপ্রেসে নিজের পছন্দের ডাটাবেজ এরর পেজ তৈরী করা
slug: custom-database-error-page-in-wordpress
language: bn
status: publish
published_at: '2013-05-25T16:09:19'
published_at_gmt: '2013-05-25T10:09:19'
modified_at: '2015-11-28T09:45:15'
modified_at_gmt: '2015-11-28T03:45:15'
original_url: https://www.shamokaldarpon.com/3647/custom-database-error-page-in-wordpress
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- Database
- Error
- ওয়ার্ডপ্রেস
- ডাটাবেজ
content_hash: 8e2dc344116f4300753a2134bb5936deb08982f7e8fd2105a5fb886838942f69
archived_at: '2026-11-12T08:35:15.833524+00:00'
---

যারা ওয়ার্ডপ্রেস নিয়ে কাজ করেন তারা জানেন বেশ কিছু কারণে ডাটাবেস এরর পেজ আসে। কিন্তু ভিজিটরা যদি Error Establishing a Database Connection ম্যাসেজ না দেখে নিজের ডিজাইন করা একটি পেজ দেখে তাহলে কেমন হয়।![](http://farm9.staticflickr.com/8379/8589181820_186863c56b_z.jpg)  
এজন্য নিজে একটি পেজ ডিজাইন করুন এবং উক্ত পেজের সোর্স কোডের উপরে নিচের কোড লিখে db-error.php নামে সেভ করুন এবং ফাইলটি কনটেন্ট (wp-content) ফোল্ডারে রাখুন।

```

<?php
header('HTTP/1.1 503 Service Temporarily Unavailable');
header('Status: 503 Service Temporarily Unavailable');
header('Retry-After: 600');
mail("mehdi@shamokaldarpon.com", "Database Error", "There is a problem with the database!", "From: DB Error Found");
?>
```

এরপরে কোন কারণে ডাটাবেজ এরর হলে Error Establishing a Database Connection ম্যাসেজ না এসে সদ্য ডিজাইন করা পেজটি দেখাবে।

চাইলে নিচের সম্পূর্ণ কোড db-error.php নামে সেভ করে ব্যবহার করতে পারেন।

```

<?php
header('HTTP/1.1 503 Service Temporarily Unavailable');
header('Status: 503 Service Temporarily Unavailable');
header('Retry-After: 600');
mail("mehdi@shamokaldarpon.com", "Database Error", "There is a problem with the database!", "From: DB Error Found");
?>

<!DOCTYPE HTML>
<html>
<head>
<title>We are working in Backend</title>
<style>
@import url(http://fonts.googleapis.com/css?family=Open+Sans:300);
body {font-family: 'Open Sans', sans-serif;background:#01A0DB}
* {margin:0;padding:0}
.column, .column h1, .column h2, .social_profiles a {transition: all 0.9s ease 0s;-moz-transition: all 0.9s ease 0s;-webkit-transition: all 0.9s ease 0s;-o-transition: all 0.9s ease 0s;}
.column {color:#fff;text-align:center}
.column h1{font-size: 50px; font-weight: normal; line-height: 50px; margin-bottom: 50px; margin-top: 138px;}
.column h1:hover{font-size: 60px; line-height: 60px;}
.column h2{font-size: 30px; font-weight: normal; line-height: 35px; margin-bottom: 40px;}
.column h2:hover{font-size: 50px; line-height: 50px; }
.column h2 span {background: none repeat scroll 0 0 #FFFFFF; color: #01A0DB; padding: 0 10px; font-weight: bold;}
.social_profiles {}
.social_profiles a{color: #FFFFFF; display: inline-block; font-size: 18px; margin-right: 15px; margin-top: 9px; padding: 10px 15px; text-decoration: none;}
.social_profiles a:hover{font-size: 25px; padding: 10px 15px; text-decoration: none;}
.facebook {background:#4166BB}
.facebook:hover {background:#22438E}
.twitter {background:#32CEFF}
.twitter:hover {background:#0C86AC}
.gplus {background:#EA0000}
.gplus:hover {background:#A70303}

</style>
</head>

    <body>
        <div class="column">
            <h1>We are working in our site!</h1>
            <h2>Our Site will be launch <span>very sort time.</span></h2>
            <div class="social_profiles">
                <a href="https://www.facebook.com/mehdiakram" target="_blank" class="facebook">Facebook</a>
                <a href="https://twitter.com/mehdiakramt" target="_blank" class="twitter">Twitter</a>
                <a href="https://plus.google.com/u/0/111670173570585456902" target="_blank" class="gplus">Google Plus</a>
            </div>
        </div>
    </body>

</html>
```
