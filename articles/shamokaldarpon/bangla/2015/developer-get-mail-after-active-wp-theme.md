---
archive_id: shamokaldarpon-4279
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4279
title: ‌ওয়ার্ডপ্রেসে থিম সক্রিয় হলেই ডেভেলপার মেইল পাবে
slug: developer-get-mail-after-active-wp-theme
language: bn
status: publish
published_at: '2015-05-02T15:30:22'
published_at_gmt: '2015-05-02T09:30:22'
modified_at: '2015-11-28T09:52:27'
modified_at_gmt: '2015-11-28T03:52:27'
original_url: https://www.shamokaldarpon.com/4279/developer-get-mail-after-active-wp-theme
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- developers
- WP
- ওয়ার্ডপ্রেস
content_hash: a8c315db9db19eb2c4c68daa065c17ca05b26f8b09b31b64dc96ffb0fc6b50c8
archived_at: '2026-11-12T08:35:21.967972+00:00'
---

আপনি যদি চান আপনার ডেভেলপ করা থিম কোন ‌ওয়েবসাইটে সক্রিয় হবার সাথে সাথে আপনার কাছে উক্ত সাইটের মেইল আসবে তাহলে কেমন হয়! সাখে ‌উক্ত ওয়েবসাইটের ঠিকানা, থিমের নাম এবং অ্যাডমিনের মেইল ঠিকানা। আপনি চাইলে আরো কিছু তথ্য যুক্ত করতে পারেন যা আপনি মেইলের মাধ্যমে পেতে চান।  
এজন্য নিচের কোড থিমের functions.php ফাইলে কপি/পেস্ট করে সেভ করুন।

```

/* Send Mail After Setup Theme*/
function set_mail_html_content_type() {
return 'text/html';
}

add_action('after_switch_theme', 'royal_mail_me');

function royal_mail_me (){
$to = 'email@yourdomain.com';
$subject = 'Your theme ('.$theme_name.') activated';
$site = site_url();
$theme_name = get_current_theme();
$admin_email = get_option( 'admin_email' );
$message = '
Dear Developer,  

('.$site.') website has been activated your theme ('.$theme_name.').  

Admin mail : '.$admin_email'.
';

add_filter( 'wp_mail_content_type', 'set_mail_html_content_type' );
wp_mail( $to, $subject, $message );
remove_filter( 'wp_mail_content_type', 'set_mail_html_content_type' ); 
}
```

ব্যাস এবার থিমটি সক্রিয় করে (লোকালহোস্টে হলে মেইল আসবে না) দেখেন আপনার মেইলে মেইল এসেছে।
