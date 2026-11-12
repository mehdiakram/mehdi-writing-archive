---
archive_id: shamokaldarpon-4236
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4236
title: ওয়ার্ডপ্রেসে পোষ্টের আর্কাইভকে উলম্ব বারে প্রর্দশন করা
slug: wordpress-post-archive-as-vertical-bar
language: bn
status: publish
published_at: '2015-01-03T11:04:49'
published_at_gmt: '2015-01-03T05:04:49'
modified_at: '2015-11-28T09:49:51'
modified_at_gmt: '2015-11-28T03:49:51'
original_url: https://www.shamokaldarpon.com/4236/wordpress-post-archive-as-vertical-bar
author: মেহেদী আকরাম
categories:
- ওয়ার্ডপ্রেস
tags:
- Archive
- WP
- আর্কাইভ
- ওয়ার্ডপ্রেস
content_hash: bb086f73276f4d5837f38ef3af4490a499083f630db4d3d1367cdb7236b24907
archived_at: '2026-11-12T08:35:21.952926+00:00'
---

ওয়ার্ডপ্রেসে ডিফল্ট আর্কাইভ উইজেটস এবং ক্যালেন্ডারের উইজেটস এর মাধ্যমে মাস হিসাবে আর্কাইভ দেখানো যায়। আমরা দেখাবো কিভাবে আর্কাইভ বছর/মাসের পোস্টের সংখ্যাকে উলম্ব বার আকারে প্রদর্শণ করা যায়। ফলে প্রতিটি বছর এক একটি রো হিসাবে দেখাবে এবং প্রতিটি রো তে ১২টি মাস থাকবে। যে মাসে কোন পোস্ট থাকেবে না যেই মাসের উলম্ব বার শুন্য থাকবে।  
যখন কোন বছরের রো এর উপরে মাউস রাখবেন তখন উক্ত বছরের মোট পোষ্টের সংখ্যা দেখাবে এবং যখন কোন মাসের উপরে মাউস রাখবেন তখন উক্ত মাসের পোষ্টের সংখ্যা দেখাবে।

নিচেন ফাংশনটি functions.php এ লিখুন।

```

function royal_bar_month_archives() {
    global $wpdb;
    $where = "WHERE post_type = 'post' AND post_status = 'publish'";
    $query = "SELECT YEAR(post_date) AS `year`, MONTH(post_date) AS `month`, count(ID) as posts FROM $wpdb->posts $where GROUP BY YEAR(post_date), MONTH(post_date) ORDER BY YEAR DESC, MONTH ASC";
    $_archive = $wpdb->get_results( $query );

    $last_year  = (int) $_archive[0]->year;
    $first_year = (int) $_archive[ count( $_archive ) - 1 ]->year;

    $archive    = array();
    $max        = 0;
    $year_total = array();
    
    foreach( $_archive as $data ) {
        if( !isset( $year_total[ $data->year ] ) ) {
            $year_total[ $data->year ] = 0;
        }
        $archive[ $data->year ][ $data->month ] = $data->posts;
        $year_total[ $data->year ] += $data->posts;
        $max = max( $max, $data->posts );
    }
    unset( $_archive );

    for ( $year = $last_year; $year >= $first_year; $year-- ) {
        echo '<div class="archive_year">';
        echo '<span class="archive_year_label">' . $year;
        if( isset( $year_total[$year] ) ) {
            echo '<span class="archive_year_count">' . $year_total[$year] . ' posts</span>';
        }
        echo '</span>';
        echo '<ol>';
        for ( $month = 1; $month <= 12; $month++ ) {
            $num = isset( $archive[ $year ][ $month ] ) ? $archive[ $year ][ $month ] : 0;
            $empty = $num ? 'not_empty' : 'empty';
            echo "<li class='$empty'>";
            $height = 100 - max( floor( $num / $max * 100 ), 20 );
            if( $num ) {
                $url = get_month_link( $year, $month );
                $m = str_pad( $month, 2, "0", STR_PAD_LEFT);
                echo "<a href='$url' title='$m/$year : $num posts'><span class='bar_wrap'><span class='bar' style='height:$height%'></span></span>";
                echo "<span class='label'>" . $m . "</span>";
                echo "</a>";
            }
            echo '</li>';
        }
        echo '</ol>';
        echo "</div>";
    }
}
```

নিচের সিএসএস লিখুন

```

/* Bar Archive */
#archives ol {
margin:-3px 0 5px;
padding:0;
list-style:none;
overflow:hidden;
width:100%;
}
#archives ol li {
display:inline-block;
float:left;
width:8%;
height:30px;
margin-left:.33333%;
background:#D6E685;
}
#archives ol li.empty {
background:rgba(246, 248, 231, 0.5);
}
#archives ol li a {
display:inline-block;
width:100%;
height:20px;
background:none;
padding:0;
}
#archives ol li a:hover {
border-radius:0;
background:inherit;
}
#archives span.bar_wrap {
width:100%;
height:100%;
zbackground:#F6F8E8;
display:block;
}
#archives span.bar {
width:100%;
background:#F6F8E8;
display:block;
}
#archives ol li.not_empty:hover {
background:#44A340;
}
#archives span.label {
display:block;
width:100%;
height:10px;
font-size:10px;
text-align:center;
line-height:2px;
color:transparent;
padding:2px 0px;
}
#archives ol li.not_empty:hover span.label {
color:white;
}
#archives .archive_year_label {
font-size:12px;
font-weight:bold;
color:#1E6823;
padding-left:2px;
}
#archives .archive_year:hover .archive_year_label {
color:#333;
}
#archives .archive_year_count {
display:none;
}
#archives .archive_year:hover .archive_year_count {
display:inline;
margin-left:30px;
color:#8CC665;
}

```

এবার যেখানে আর্কাইভ দেখাতে চান সেখানে নিচের ফংশনটি কল করুন

```

<div id='archives'>
    <?php royal_bar_month_archives(); ?>
</div>
```

ফলাফল নিচের স্ক্রিনশেটর মত দেখাবে  
![বার আর্কাইভ](https://c4.staticflickr.com/8/7440/16432955505_2173dd5525.jpg)
