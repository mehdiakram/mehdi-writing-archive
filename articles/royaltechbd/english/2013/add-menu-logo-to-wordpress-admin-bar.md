---
archive_id: royaltechbd-596
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 596
title: Add Menu & Logo to WordPress Admin bar
slug: add-menu-logo-to-wordpress-admin-bar
language: en
status: publish
published_at: '2013-03-18T05:06:22'
published_at_gmt: '2013-03-17T23:06:22'
modified_at: '2026-09-28T09:03:50'
modified_at_gmt: '2026-09-28T03:03:50'
original_url: https://www.royaltechbd.com/add-menu-logo-to-wordpress-admin-bar/
author: S M Mehdi Akram
categories:
- Wordpress
tags:
- Admin
- Admin bar
content_hash: 94d13578a4d70ef906f0ba85345cacc6cdbebd7ecfa253b15faee2e050b11754
archived_at: '2026-11-12T08:38:58.459836+00:00'
---

**WordPress Dashboard Customize (Part 2)**  
Access the Active Theme of your website and open the functions.php file. Paste the snips below into the file then test.

[php]  
/\*  
\* Add a simple menu & link that opens in a new window  
\* Change the Menu ‘title’ name and ‘href’ link.  
\*/  
function rt\_admin\_bar() {  
global $wp\_admin\_bar;  
//Add a link called ‘RT\_Menu’  
$wp\_admin\_bar->add\_menu( array(  
‘id’ => ‘RT\_Menu’,  
‘title’ => ‘<img src="’.get\_template\_directory\_uri(\_\_FILE\_\_).’/images/rt\_logo.png"/>’,  
‘href’ => ‘http://www.royaltechbd.com/’,  
‘meta’ => array( target => ‘\_blank’ )  
));

//THEN add a sub-link called ‘RoyalTechnologies’  
$wp\_admin\_bar->add\_menu( array(  
‘id’ => ‘RoyalTechnologies’,  
‘title’ => ‘Royal Technologies’,  
‘href’ => ‘http://www.royaltechbd.com’,  
‘meta’ => array( target => ‘\_blank’ ),  
‘parent’=>’RT\_Menu’  
));

//THEN add a sub-link called ‘twitter’  
$wp\_admin\_bar->add\_menu( array(  
‘id’ => ‘blog’,  
‘title’ => ‘Shamokal Darpon’,  
‘href’ => ‘http://www.shamokaldarpon.com’,  
‘meta’ => array( target => ‘\_blank’ ),  
‘parent’=>’RT\_Menu’  
));

//THEN add a sub-link called ‘facebook’  
$wp\_admin\_bar->add\_menu( array(  
‘id’ => ‘facebook’,  
‘title’ => ‘Mehdi Akram – Facebook’,  
‘href’ => ‘https://www.facebook.com/mehediakram’,  
‘meta’ => array( target => ‘\_blank’ ),  
‘parent’=>’RT\_Menu’  
));

//THEN add a sub-link called ‘twitter’  
$wp\_admin\_bar->add\_menu( array(  
‘id’ => ‘twitter’,  
‘title’ => ‘Mehdi Akram – Twitter’,  
‘href’ => ‘https://www.twitter.com/mehdiakram’,  
‘meta’ => array( target => ‘\_blank’ ),  
‘parent’=>’RT\_Menu’  
));

//THEN add a sub-link called ‘googleplus’  
$wp\_admin\_bar->add\_menu( array(  
‘id’ => ‘googleplus’,  
‘title’ => ‘Mehdi Akram – Google Plus’,  
‘href’ => ‘https://plus.google.com/u/0/111670173570585456902’,  
‘meta’ => array( target => ‘\_blank’ ),  
‘parent’=>’RT\_Menu’  
));  
}  
add\_action( ‘admin\_bar\_menu’, ‘rt\_admin\_bar’, 10 );  
[/php]  
The add\_action you can set the menu position:  
10 = Before the WP Logo  
15 = Between the logo and My Sites  
25 = After the My Sites menu  
100 = End of menu

**After**  
![](http://farm9.staticflickr.com/8386/8567989080_94f719c916_z.jpg)
