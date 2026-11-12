---
archive_id: shamokaldarpon-4289
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4289
title: ‌ওয়ার্ডপ্রেসে ইউজার লুকিয়া রাখা
slug: hide-wordpress-user
language: bn
status: publish
published_at: '2015-08-08T15:27:26'
published_at_gmt: '2015-08-08T09:27:26'
modified_at: '2015-11-28T09:53:20'
modified_at_gmt: '2015-11-28T03:53:20'
original_url: https://www.shamokaldarpon.com/4289/hide-wordpress-user
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- developers
- WP
- ওয়ার্ডপ্রেস
content_hash: 4fa1b5bd8ae68aa232ffe3431bde5d2ec84a5df58bbe3bfeda4c8df2289ff36c
archived_at: '2026-11-12T08:35:21.973193+00:00'
---

আপনি যদি চান আপনার ‌ওয়ার্ডপ্রেসে সাইটে আপনার অ্যাডমিনিস্ট্রেটর ইউজারটি অন্য ইউজার (এমনকি অন্য অ্যাডমিনিস্ট্রেটর) থেকে লুকিয়ে রাখতে, তাহলে সহজেই functions.php দ্বারা তা করতে পারবেন। এজন্য নিচের কোড থিমের functions.php ফাইলে কপি/পেস্ট করে সেভ করুন।

```

add_action('pre_user_query','royal_hide_user_query');
function royal_hide_user_query($user_search) {
  global $current_user;
  $username = $current_user->user_login;

  if ($username !== 'smmehdiakram') { 
    global $wpdb;
    $user_search->query_where = str_replace('WHERE 1=1',
      "WHERE 1=1 AND {$wpdb->users}.user_login != 'smmehdiakram'",$user_search->query_where);
  }
}	

add_action('admin_head','hide_user_count');
function hide_user_count(){
?>
<style>
.wp-admin.users-php span.count {display: none;}
</style>
<?php
}
```

ব্যাস এবার ড্যাশবোর্ডের ইউজার্সে গিয়ে দেখুন smmehdiakram নামের ইউজারটি দেখা যাচ্ছে না।  
এখানে ইউজারের নাম হিসাবে smmehdiakram ব্যবহার করা হয়েছে।
