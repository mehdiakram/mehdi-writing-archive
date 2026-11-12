---
archive_id: royaltechbd-591
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 591
title: Remove menu items from WordPress Admin bar
slug: remove-menu-items-from-wordpress-admin-bar
language: en
status: publish
published_at: '2013-03-18T04:45:54'
published_at_gmt: '2013-03-17T22:45:54'
modified_at: '2026-09-28T09:03:51'
modified_at_gmt: '2026-09-28T03:03:51'
original_url: https://www.royaltechbd.com/remove-menu-items-from-wordpress-admin-bar/
author: Mehdi Akram
categories:
- Wordpress
tags:
- Admin
- Menu
content_hash: c3959e7643c478b349d275e0ce7c4da3af6d4b8b39d27c00cb60377b9d631d4a
archived_at: '2026-11-12T08:31:05.501515+00:00'
---

**WordPress Dashboard Customize (Part 1)**  
Access the Active Theme of your website and open the functions.php file. Paste the snips below into the file then test.  
**Before**  
![](http://farm9.staticflickr.com/8235/8567967960_47c632bfb9_z.jpg)  
[php]  
/\* Remove menu items from WordPress admin bar \*/  
function wps\_admin\_bar() {  
global $wp\_admin\_bar;  
$wp\_admin\_bar->remove\_menu(‘wp-logo’);  
$wp\_admin\_bar->remove\_menu(‘about’);  
$wp\_admin\_bar->remove\_menu(‘wporg’);  
$wp\_admin\_bar->remove\_menu(‘documentation’);  
$wp\_admin\_bar->remove\_menu(‘support-forums’);  
$wp\_admin\_bar->remove\_menu(‘feedback’);  
$wp\_admin\_bar->remove\_menu(‘view-site’);  
}  
add\_action( ‘wp\_before\_admin\_bar\_render’, ‘wps\_admin\_bar’ );  
[/php]

![](http://farm9.staticflickr.com/8378/8566869883_ce7cefaba8_z.jpg)
