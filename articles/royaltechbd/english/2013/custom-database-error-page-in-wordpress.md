---
archive_id: royaltechbd-613
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 613
title: Custom “Database Error” Page in WordPress
slug: custom-database-error-page-in-wordpress
language: en
status: publish
published_at: '2013-03-24T11:32:31'
published_at_gmt: '2013-03-24T05:32:31'
modified_at: '2026-09-28T09:03:47'
modified_at_gmt: '2026-09-28T03:03:47'
original_url: https://www.royaltechbd.com/custom-database-error-page-in-wordpress/
author: S M Mehdi Akram
categories:
- Wordpress
tags:
- Database
- WP
content_hash: 14416e1041a5db9a887590735dc7c7cb9c9a211643cb6274070212e6191e5b16
archived_at: '2026-11-12T08:38:58.434747+00:00'
---

Some times you seeing a screen like **Error Establishing a Database Connection** or **Error Database** on your site. This can happen for various reasons, but often users don’t know that their site is down. Also that page itself looks pretty ugly in itself. In this article, we will show you how to customize your database error page in WordPress with CSS3. We will also show you how to setup a notification for every time your website goes down due to a database error.

Open a new file and save it as “**db-error.php**“. Paste the following content inside that. Then upload the file in your **wp-content/** directory.

[php]  
<?php // custom WordPress database error page

header(‘HTTP/1.1 503 Service Temporarily Unavailable’);  
header(‘Status: 503 Service Temporarily Unavailable’);  
header(‘Retry-After: 600’); // 1 hour = 3600 seconds

// If you wish to email yourself upon an error  
// mail("your@email.com", "Database Error", "There is a problem with the database!", "From: Db Error Watching");

?>

<!DOCTYPE HTML>  
<html>  
<head>  
<title>We are working in Backend</title>  
<style>  
@import url(http://fonts.googleapis.com/css?family=Open+Sans:300);  
body {font-family: ‘Open Sans’, sans-serif;background:#01A0DB}  
\* {margin:0;padding:0}  
.column, .column h1, .column h2, .social\_profiles a {transition: all 0.9s ease 0s;-moz-transition: all 0.9s ease 0s;-webkit-transition: all 0.9s ease 0s;-o-transition: all 0.9s ease 0s;}  
.column {color:#fff;text-align:center}  
.column h1{font-size: 50px; font-weight: normal; line-height: 50px; margin-bottom: 50px; margin-top: 138px;}  
.column h1:hover{font-size: 60px; line-height: 60px;}  
.column h2{font-size: 30px; font-weight: normal; line-height: 35px; margin-bottom: 40px;}  
.column h2:hover{font-size: 50px; line-height: 50px; }  
.column h2 span {background: none repeat scroll 0 0 #FFFFFF; color: #01A0DB; padding: 0 10px; font-weight: bold;}  
.social\_profiles {}  
.social\_profiles a{color: #FFFFFF; display: inline-block; font-size: 18px; margin-right: 15px; margin-top: 9px; padding: 10px 15px; text-decoration: none;}  
.social\_profiles a:hover{font-size: 25px; padding: 10px 15px; text-decoration: none;}  
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
<div class="social\_profiles">  
<a href="https://www.facebook.com/mehdiakram" target="\_blank" class="facebook">Facebook</a>  
<a href="https://twitter.com/mehdiakramt" target="\_blank" class="twitter">Twitter</a>  
<a href="https://plus.google.com/u/0/111670173570585456902" target="\_blank" class="gplus">Google Plus</a>  
</div>  
</div>  
</body>

</html>  
[/php]
