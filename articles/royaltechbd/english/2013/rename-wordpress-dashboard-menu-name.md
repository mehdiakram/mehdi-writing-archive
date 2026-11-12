---
archive_id: royaltechbd-603
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 603
title: Rename WordPress Dashboard Menu Name
slug: rename-wordpress-dashboard-menu-name
language: en
status: publish
published_at: '2013-03-19T08:27:29'
published_at_gmt: '2013-03-19T02:27:29'
modified_at: '2026-09-28T09:03:49'
modified_at_gmt: '2026-09-28T03:03:49'
original_url: https://www.royaltechbd.com/rename-wordpress-dashboard-menu-name/
author: Mehdi Akram
categories:
- Wordpress
tags:
- Dashboard
- Menu
content_hash: c141c25326c18750455407e75cdc419d0c9a20e8daba36996c00dccc88842b3e
archived_at: '2026-11-12T08:31:05.460169+00:00'
---

**WordPress Dashboard Customize (Part 3)**  
Access the Active Theme of your website and open the functions.php file. Paste the snips below into the file then test.

[php]  
/\* Rename Dashboard Menu Name \*/  
function rename\_admin\_menu\_items( $menu ) {  
// $menu = str\_ireplace( ‘original name’, ‘new name’, $menu );  
$menu = str\_ireplace( ‘Dashboard’, ‘Home’, $menu );  
$menu = str\_ireplace( ‘Posts’, ‘Recipe’, $menu );  
$menu = str\_ireplace( ‘Comments’, ‘Visitor Feedback’, $menu );  
// return $menu array  
return $menu;  
}  
add\_filter(‘gettext’, ‘rename\_admin\_menu\_items’);  
add\_filter(‘ngettext’, ‘rename\_admin\_menu\_items’);  
[/php]

**After**  
![](http://farm9.staticflickr.com/8373/8571536104_5f348c6b64_z.jpg)
