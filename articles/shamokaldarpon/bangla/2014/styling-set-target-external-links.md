---
archive_id: shamokaldarpon-4133
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4133
title: ওয়েব সাইটে এক্সটারনাল লিংককে স্টাইল করা এবং target যুক্ত করা
slug: styling-set-target-external-links
language: bn
status: publish
published_at: '2014-02-12T11:05:59'
published_at_gmt: '2014-02-12T05:05:59'
modified_at: '2015-11-28T09:47:28'
modified_at_gmt: '2015-11-28T03:47:28'
original_url: https://www.shamokaldarpon.com/4133/styling-set-target-external-links
author: মেহেদী আকরাম
categories:
- ওয়েব ডিজাইন এবং ডেভেলপমেন্ট
tags:
- jquery
- no conflict
- জেকুয়েরী
content_hash: 01c2e84927bee727352081df3209c6c35172beb391f1470977864d9d7b84614a
archived_at: '2026-11-12T08:35:21.930328+00:00'
---

ওয়েব সাইটে এক্সটারনাল লিংককে CSS এর মাধ্যমে স্টাইল করা, লিংকের শেষে শব্দ বা [ছবি যুক্ত](http://en.wikipedia.org/wiki/Bangladesh) করা যায়। এছাড়াও চাইলে এক্সটারনাল লিংকের ক্ষেত্রে target=”\_blank” সেট করা যায় জেকুয়েরীর সাহায্যে। নিচের উদাহারণে shamokaldarpon.com ছাড়া বাকী সব লিংক এক্সটারনাল লিংক হিসাবে ব্যবহার করেছি। আপনার প্রয়োজনমত সাইটের ইআরএল পরিবর্তন করে নিবেন।

```

<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>Styling External Links</title>

<style type="text/css">
/* Styling External Links */
a[href^="http://"]:not([href*="shamokaldarpon.com"]):after,
a[href^="https://"]:not([href*="shamokaldarpon.com"]):after{
padding-left:2px;
content: "" url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAVklEQVR4Xn3PgQkAMQhDUXfqTu7kTtkpd5RA8AInfArtQ2iRXFWT2QedAfttj2FsPIOE1eCOlEuoWWjgzYaB/IkeGOrxXhqB+uA9Bfcm0lAZuh+YIeAD+cAqSz4kCMUAAAAASUVORK5CYII=);
}		
</style>
		
<script src="http://code.jquery.com/jquery-latest.min.js"  type="text/javascript"></script>	
<script type="text/javascript">
jQuery.noConflict();
(function( $ ) {
$(document).ready(function(){
	$("a[href^='http://']:not([href*='shamokaldarpon.com'])").attr("target","_blank");
	$("a[href^='https://']:not([href*='shamokaldarpon.com'])").attr("target","_blank");
});
})(jQuery);
</script>		
		
		
		
		
</head>
<body>
<div> 
<h4>Internal Links</h4>
<a href="http://shamokaldarpon.com">Shamokal Darpon</a>
<a href="http://demo.shamokaldarpon.com">Demo</a>
<a href="http://www.shamokaldarpon.com/4120/sylhet-tour-2014">Sylhet Tour 2014</a>
<a href="http://www.shamokaldarpon.com/4127/khoiyachora-waterfalls">Khoiyachora Waterfalls</a>
</div>


<div> <h4>External Links</h4>
<a href="https://www.facebook.com">Facebook</a>
<a href="https://www.google.com">Google</a>
<a href="https://wikipedia.org">Wikipedia</a>
<a href="http://royaltechbd.com">Royal Technologies</a>
</div>
</body>
</html>
```

এখানে CSS পার্টটুক shamokaldarpon.com ছাড়া বাকী লিংকগুলোর শেষে একটি ছবি যুক্ত করা হয়েছে এবং জেকুয়েরী কল করা এবং স্ক্রিপ্টটুক shamokaldarpon.com ছাড়া বাকী সব লিংকে target=”\_blank” করা হয়েছে।

[কোডপেন লিংক](http://codepen.io/mehdiakam/pen/HeEpt)
