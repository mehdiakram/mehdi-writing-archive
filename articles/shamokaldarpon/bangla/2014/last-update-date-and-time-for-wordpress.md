---
archive_id: shamokaldarpon-4112
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4112
title: ওয়ার্ডপ্রেসের সর্বশেষ আপডেটের তারিখ ও সময় দেখানো
slug: last-update-date-and-time-for-wordpress
language: bn
status: publish
published_at: '2014-07-22T10:23:46'
published_at_gmt: '2014-07-22T04:23:46'
modified_at: '2014-10-25T10:26:24'
modified_at_gmt: '2014-10-25T04:26:24'
original_url: https://www.shamokaldarpon.com/4112/last-update-date-and-time-for-wordpress
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- Date
- Date-Time
- Time
- Update
- WP
- ওয়ার্ডপ্রেস
- সর্বশেষ
content_hash: 53844815547ef5ebc357bfda0976c06c4892b3d6ada300c3cda56f578131cf36
archived_at: '2026-11-12T08:35:14.699352+00:00'
---

ওয়ার্ডপ্রেসের সর্বশেষ কোন লেখা কথন আপডেট বা প্রকাশ হয়েছে তা দেখানো জন্য [the\_modified\_date();](http://codex.wordpress.org/Function_Reference/the_modified_date) এবং [the\_modified\_time();](http://codex.wordpress.org/Function_Reference/the_modified_time) ব্যবহার করে প্রকাশ করা যায়। কিন্তু স্টিকি পোষ্ট বা কোন ক্যাটাগরি বা আর্কাইভ পেজের ক্ষেত্রে উক্ত পোষ্টে সময় এবং তারিখ প্রদর্শিত হয়।  
তবে আপনি যদি চান পুরো সাইটের সর্বশেষ আপডেট বা পোষ্ট করা পোষ্টের তারিখ এবং দেখাতে তাহলে ছোট দুটি ফাংশন তৈরী করে তা করতে পারেন।  
তারিখের জন্য ফাংশন

```

function royal_site_last_updated_date($d = '') {
	$recent = new WP_Query("showposts=1&orderby=modified&post_status=publish");
	if ( $recent->have_posts() ) {
		while ( $recent->have_posts() ) {
			$recent->the_post();
			$last_update_date = get_the_modified_date($d);
		}
		echo $last_update_date;
	}
	else
		echo 'No posts.';
}
```

ফাংশন প্রিন্ট করা

```
<?php royal_site_last_updated_date('F j, Y') ?>
```

সময়ের জন্য ফাংশন

```

function royal_site_last_updated_time($d = '') {
	$recent = new WP_Query("showposts=1&orderby=modified&post_status=publish");
	if ( $recent->have_posts() ) {
		while ( $recent->have_posts() ) {
			$recent->the_post();
			$last_update_time = get_the_modified_time($d);
		}
		echo $last_update_time;
	}
	else
		echo 'No posts.';
}
```

ফাংশন প্রিন্ট করা

```
<?php royal_site_last_updated_time('g:i a'); ?>
```
