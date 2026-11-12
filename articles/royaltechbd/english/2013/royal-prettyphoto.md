---
archive_id: royaltechbd-978
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 978
title: Royal PrettyPhoto
slug: royal-prettyphoto
language: en
status: publish
published_at: '2013-08-02T14:34:37'
published_at_gmt: '2013-08-02T08:34:37'
modified_at: '2026-09-28T09:03:41'
modified_at_gmt: '2026-09-28T03:03:41'
original_url: https://www.royaltechbd.com/royal-prettyphoto/
author: Mehdi Akram
categories:
- Our Plugins
- Wordpress
tags: []
content_hash: f32ee1d2eda31bef6d1ae2c1a404f5bac0d891b2da3c3437cbedf9a870599065
archived_at: '2026-11-12T08:31:05.374292+00:00'
---

Royal PrettyPhoto is a ismple cool plugin to add automatic lightbox in wordpress post/page using added images.  
  
![prettyphoto](https://ps.w.org/rt-prettyphoto/assets/banner-772x250.png?rev=1153442)

**Examples:**  
To add a Single Video

[code]  
<a href="Full Video Link" rel="prettyPhoto"><img alt="" src="Full Thumbnial Path" /></a>  
[/code]

To add video with default image gallery

[code]  
<a href="Full Video Link" rel="prettyPhoto[Your\_Post\_ID]" ><img src="Full Thumbnial Path" alt=""/></a>  
[/code]

If you post ID is 708 rel should rel=”prettyPhoto[708]”.  
Aditional Gallery with Image, Youtube Video, Vimeo Video or DIV

[code]  
<div id="complexgallery">  
<a href="Internal or External Full Image Link" rel="prettyPhoto[galleryname]"><img src="Full Thumbnial Path" alt=""/></a>  
<a href="Youtube Full Video Link" rel="prettyPhoto[galleryname]"><img src="Full Thumbnial Path" alt=""/></a>  
<a href="Vimeo Full Video Link" rel="prettyPhoto[galleryname]"><img src="Full Thumbnial Path" alt=""/></a>  
<a href="#DIV\_ID\_NAME" rel="prettyPhoto[galleryname]"><img src="Full Thumbnial Path" alt=""/></a>  
<a href="#DIV\_ID\_NAME" rel="prettyPhoto[galleryname]">Text for Link</a>  
</div>  
[/code]

For DIV you should add a div like below.

[code]  
<div id="DIV\_ID\_NAME" style="display:none">  
<p>This is inline DEV content for prettyPhoto.</p>  
<p>Your DIV full conent here.</p><p>Your DIV full conent here.</p><p>Your DIV full conent here.</p><p>Your DIV full conent here.</p></div>  
</div>  
[/code]

Download from <https://wordpress.org/plugins/rt-prettyphoto/>
