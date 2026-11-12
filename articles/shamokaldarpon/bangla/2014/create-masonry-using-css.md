---
archive_id: shamokaldarpon-4228
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4228
title: সিএসএস দ্বারা মেসনরি (Masonry) তৈরী করা
slug: create-masonry-using-css
language: bn
status: publish
published_at: '2014-12-23T13:21:45'
published_at_gmt: '2014-12-23T07:21:45'
modified_at: '2014-12-23T13:21:45'
modified_at_gmt: '2014-12-23T07:21:45'
original_url: https://www.shamokaldarpon.com/4228/create-masonry-using-css
author: মেহেদী আকরাম
categories:
- ওয়েব ডিজাইন এবং ডেভেলপমেন্ট
tags:
- column
- column-count
- CSS
- Masonry
- responsive
- মেসনরি
- রেসপনসিভ
- সিএসএস
content_hash: 1bac73b3e66664ca52cf5c81af852e7076185685030e26483569f4a750173aaa
archived_at: '2026-11-12T08:35:14.721404+00:00'
---

[জাভাস্ক্রিপ্ট দ্বারা সুন্দর মেসনরি](http://masonry.desandro.com/) তৈরী করা যায়, তবে শুধুমাত্র সিএসএস দ্বারাও মেসনরি তৈরী করা যায়, তবে এটা মূলত [CSS3 এর column-count](http://www.w3schools.com/cssref/css3_pr_column-count.asp) পোপার্টির ব্যবহার, যা দেখতে মেসনরি’র মতই মনে হবে। চাইলে এটাকে রেসপনসিভ করা যাবে column-count কম বেশী করে।  
HTML কোড

```

<div class="wrapper">
	<div class="masonry">
		<div class="item">1 Lorem ipsum dolor sit amet, consectetur adipisicing elit.  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum? </div>
		<div class="item">2 Lorem ipsum dolor sit amet, consectetur adipisicing elit.  Incidunt sit unde minima in nostrum? </div>
		<div class="item">3 Lorem ipsum dolor sit amet, consectetur adipisicing elit.  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum? </div>
		<div class="item">4 Lorem ipsum dolor sit amet, consectetur adipisicing elit. Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum? </div>
		<div class="item">5 Neque, vitae, fugiat, libero corrupti officiis sint facilis tempora quidem repudiandae praesentium odit similique adipisci aut.</div>
		<div class="item">6 Incidunt sit unde minima in nostrum? Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?  Incidunt sit unde minima in nostrum?   </div>
		<div class="item">7 Ducimus, voluptates, modi, delectus animi maiores consequuntur repellat quisquam fugiat eum possimus enim culpa totam praesentium magni quae!</div>
		<div class="item">8 Lorem ipsum dolor sit amet, dicta dolore adipisci hic ipsam velit deleniti possimus cumque accusantium rerum quibusdam.</div>
		<div class="item">9 Lorem ipsum dolor sit amet, dicta dolore adipisci hic ipsam velit deleniti possimus cumque accusantium rerum quibusdam.</div>
		<div class="item">10 Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae, praesentium consequatur ducimus commodi quam ex illo omnis dicta reiciendis vel nesciunt deserunt aut sequi nam mollitia perferendis ipsam possimus temporibus!</div>
		<div class="item">11 Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae, praesentium consequatur ducimus commodi quam ex illo omnis dicta reiciendis vel nesciunt deserunt aut sequi nam mollitia perferendis ipsam possimus temporibus!</div>
		<div class="item">12 Ab, adipisci, temporibus eaque quis harum perferendis incidunt cupiditate doloribus dolor numquam voluptates ipsum dolore aspernatur et voluptate ipsam beatae animi culpa.</div>
	</div>
</div>
```

কলাম কাউন্ট এর জন্য CSS কোড

```

body {
    font: 1em/1.67 'Open Sans', Arial, Sans-serif;
    margin: 0;
    background: #e9e9e9;
}

.wrapper {
    max-width: 95%;
    margin: 3em auto;
	width: 1260px;
}

.masonry {
/* Masonry basic */
    margin: 1.5em 0;
    padding: 0;
    -moz-column-gap: 1.5em;
    -webkit-column-gap: 1.5em;
    column-gap: 1.5em;
    font-size: .85em;
/* Masonry column */	
	-moz-column-count: 5;
	-webkit-column-count: 5;
	column-count: 5;	
	
	
}

.item {
/* Masonry bricks or child elements */
    background-color: #fff;
    width: 100%;	
    display: inline-block;
    padding: 1em;
    margin: 0 0 1.5em;
    box-sizing: border-box;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    box-shadow: 2px 2px 4px 0 #ccc;
}
```

রেসপসসিভ করার জন্য নিচের CSS কোড ব্যবহার করতে পারেন

```

@media only screen and (max-width: 1100px) {
    .masonry {
        -moz-column-count: 4;
        -webkit-column-count: 4;
        column-count: 4;
    }
}

@media only screen and (max-width: 900px) {
    .masonry {
        -moz-column-count: 3;
        -webkit-column-count: 3;
        column-count: 3;
    }
}


@media only screen and (max-width: 700px) {
    .masonry {
        -moz-column-count: 2;
        -webkit-column-count: 2;
        column-count: 2;
    }
}

@media only screen and (max-width: 400px) {
    .masonry {
        -moz-column-count: 1;
        -webkit-column-count: 1;
        column-count: 1;
    }
}
```

[ডেমো](http://codepen.io/mehdiakam/pen/gbYqQX)
