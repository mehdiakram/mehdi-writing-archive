---
archive_id: royaltechbd-988
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 988
title: Limit the number of words in excerpt without plugins
slug: limit-the-number-of-words-in-excerpt-without-plugins
language: en
status: publish
published_at: '2013-08-28T16:54:55'
published_at_gmt: '2013-08-28T10:54:55'
modified_at: '2026-09-28T09:03:40'
modified_at_gmt: '2026-09-28T03:03:40'
original_url: https://www.royaltechbd.com/limit-the-number-of-words-in-excerpt-without-plugins/
author: Mehdi Akram
categories:
- Wordpress
tags:
- Tips
content_hash: 86b2210a42c0d4e641bfdae457b7d9c26546beaef7e8f9cc8b8b62c88801aed8
archived_at: '2026-11-12T08:31:05.361449+00:00'
---

Excerpt by default display a numbers of characters so some times brake a word, No you can set limit the number of words displayed in the excerpt without any plugin.  
  
Put the following code in your templates functions.php file.  
[code]  
function royal\_string\_limit\_words($string, $word\_limit)  
{  
$words = explode(‘ ‘, $string, ($word\_limit + 1));  
if(count($words) > $word\_limit)  
array\_pop($words);  
return implode(‘ ‘, $words);  
}  
[/code]

Now put the following code in your template where you want to display the excerpt.  
[code]  
<?php  
$excerpt = get\_the\_excerpt();  
echo royal\_string\_limit\_words($excerpt,55);  
?>  
[/code]  
Where 55 is the number of words (not character) to display.
