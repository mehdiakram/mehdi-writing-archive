---
archive_id: royaltechbd-1655
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 1655
title: Display numbers in lack and crore
slug: display-numbers-in-lack-and-crore
language: en
status: publish
published_at: '2020-11-16T17:32:34'
published_at_gmt: '2020-11-16T11:32:34'
modified_at: '2026-09-28T09:03:26'
modified_at_gmt: '2026-09-28T03:03:26'
original_url: https://www.royaltechbd.com/display-numbers-in-lack-and-crore/
author: Mehdi Akram
categories:
- MS Office
tags:
- Excel
content_hash: 31817dca86e9f64152e38ead73ef7b1bc5914d6e73ffdf19e5822041d958f21b
archived_at: '2026-11-12T08:31:03.261673+00:00'
---

If your country’s currency system is in Lakhs and Crores, and not in Millions and Billions, this is what you need to do.

Select all the cells where you want the numbers to then display in Lakhs and Crores (let’s say entire D column).  
Right-click and go to ‘Format cells’ (shortcut to go to format cells is Ctrl + 1).  
Format Cells  
Select ‘Custom’ and in the ‘Type’ box, type this  
[>=10000000]##\,##\,##\,##0;[>=100000] ##\,##\,##0;##,##0

Press Ok.  
Write 1 Crore (1 with 7 zero’s) and check the output.
