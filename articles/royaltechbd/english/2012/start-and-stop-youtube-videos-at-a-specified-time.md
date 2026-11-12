---
archive_id: royaltechbd-473
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 473
title: Start and Stop YouTube Videos at a Specified Time
slug: start-and-stop-youtube-videos-at-a-specified-time
language: en
status: publish
published_at: '2012-07-02T00:55:25'
published_at_gmt: '2012-07-01T18:55:25'
modified_at: '2026-09-28T09:04:32'
modified_at_gmt: '2026-09-28T03:04:32'
original_url: https://www.royaltechbd.com/start-and-stop-youtube-videos-at-a-specified-time/
author: Mehdi Akram
categories:
- Online
- Tips
tags:
- YouTube
content_hash: a3f5adbdfcbd20c05324b38e58b22fe34773460ff592e7f143469e8e86353d82
archived_at: '2026-11-12T08:31:11.939848+00:00'
---

YouTube gives users the automatic start video at a specific time and stop another specific time. Google added a [new youtube parameter](http://apiblog.youtube.com/2012/06/all-good-things-must-come-to-end.html) that allows users to stop video playback at a specific time.

The end parameter is a positive integer value specifies the time in seconds from the start of the video, when the player should stop playing the video. Note that the time is measured from the beginning of the video and not from either the value of the start player parameter or the start Seconds parameter.

Example:  
[code]  
<iframe width="420" height="315" src="http://www.youtube.com/embed/Nc9xq-TVyHI?start=60<strong>&end=119</strong>" frameborder="0" allowfullscreen></iframe>  
[/code]  
Here Start from 60 (**?start=60**) second and stop 119 second (**&end=119**).
