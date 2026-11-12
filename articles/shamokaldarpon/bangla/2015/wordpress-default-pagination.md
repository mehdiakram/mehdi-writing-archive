---
archive_id: shamokaldarpon-4342
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4342
title: ‌ওয়ার্ডপ্রেসের বিল্টইন পেজিনেশন
slug: wordpress-default-pagination
language: bn
status: publish
published_at: '2015-11-04T11:49:02'
published_at_gmt: '2015-11-04T05:49:02'
modified_at: '2015-11-04T11:49:02'
modified_at_gmt: '2015-11-04T05:49:02'
original_url: https://www.shamokaldarpon.com/4342/wordpress-default-pagination
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- codex
- comments
- comments pagination
- links
- Pagination
- WP
- ওয়ার্ডপ্রেস
- কমেন্ট পেজিনেশন
- পেজ পেজিনেশন
- পেজিনেশন
content_hash: d253bd0c1dcff99f3cf56a5aefb876197802ade706fa39d58a6fbe3bcacacec2
archived_at: '2026-11-12T08:35:15.476419+00:00'
---

‌ওয়ার্ডপ্রেসে দ্বারা যারা ওয়েবসাইট তৈরী করেন তাদের পেজ পেজিনেশন বা কমেন্ট পেজিনেশন করার দরকার হয়। বেশীরভাগ ডেভেলপাররা কাস্টম ফাংশন তৈরী করে পেজ পেজিনেশন বা কমেন্ট পেজিনেশন ব্যবহার করে থাকে। তবে কাস্টম ফাংশন ছাড়াও খুব সহজে ‌ওয়ার্ডপ্রেসের বিল্টইন পেজিনেশন ফাংশন ব্যবহার করা যায়। ফাংশন দুটি হচ্ছে paginate\_links এবং paginate\_comments\_links।  
ফাংশন দুটি সম্পর্কে আরো বিস্তারিত পাবেন ফাংশন দুটির কোডেক্স থেকে।

পেজ পেজিনেশন কোড

```
<div class="pagination">
<?php
global $wp_query;
$big = 999999999; // need an unlikely integer
echo paginate_links( array(
'base' 		=> str_replace( $big, '%#%', esc_url( get_pagenum_link( $big ))),
'format' 	=> '?paged=%#%',
'current' 	=> max(1, get_query_var('paged') ),
'total' 	=> $wp_query->max_num_pages,
'prev_next' 	=> True,
'prev_text'	=> __('« Previous'),
'next_text' 	=> __('Next »'),						
'before_page_number'=> ''
) );
?>
</div>
```

বিস্তারিত কোডেক্সে: <https://codex.wordpress.org/Function_Reference/paginate_links>

কমেন্ট পেজিনেশন কোড

```
<div class="pagination">
<?php paginate_comments_links( array('prev_text' => '&laquo;', 'next_text' => '&raquo;') )  ?>
</div>
```

বিস্তারিত কোডেক্সে: <https://codex.wordpress.org/Function_Reference/paginate_comments_links>

পেজ পেজিনেশন এবং কমেন্ট পেজিনেশন উভয়ের জন্য CSS কোড

```
/* For Pagination CSS */
.pagination{
clear:both;
font-size:14px;
line-height:14px;
padding:20px 0; 
overflow: hidden;
text-align: center;
}
.pagination span, .pagination a{
margin:2px 2px 2px 0;
padding:6px 9px 5px 9px;
text-decoration:none;
width:auto;
color:#fff;
background:#555;
line-height: 30px;
}
.pagination a:hover{
color:#fff;
background:#3279BB;
}
.pagination .current{
padding:6px 9px 5px 9px;
background:#3279BB;
color:#fff;
} 
```
