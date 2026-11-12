---
archive_id: shamokaldarpon-97
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 97
title: মাই কম্পিউটার থেকে শেয়ার ডকুমেন্ট বাদ দেওয়া
slug: remove-share-document-from-my-computer
language: bn
status: publish
published_at: '2007-08-09T18:16:38'
published_at_gmt: '2007-08-09T12:16:38'
modified_at: '2012-10-03T11:35:48'
modified_at_gmt: '2012-10-03T05:35:48'
original_url: https://www.shamokaldarpon.com/97/remove-share-document-from-my-computer
author: admin
categories:
- টিপস এন্ড ট্রিকস
tags:
- Shared Document
- Tips
- উইন্ডোজ
- টিপস
- শেয়ার ডকুমেন্ট
content_hash: d159b46533efc502dc88a94ef7bea22d3cb1946300f268dd8456e8f0d00403d0
archived_at: '2026-11-12T08:35:08.086979+00:00'
---

উইন্ডোজ এক্সপি বা ভিসতায় মাই কম্পিউটার খুললে শেয়ার ডকুমেন্ট দেখা যায়। উইন্ডোজের সাথে ডিফল্ট থাকা এই শেয়ার ডকুমেন্ট মুছে বাদ দেওয়া যায়।

এজন্য রেজিস্ট্রি এডিটর থেকে HKEY\_LOCAL\_MACHINE SOFTWARE Microsoft Windows CurrentVersion Explorer My Computer NameSpace DelegateFolders যান এবং নিচে সাব কী {59031a47-3f72-44a7-89c5-5595fe6b30ee} মুছে দিন। এবার মাই কম্পিউটারে খুললে শেয়ার ডকুমেন্ট দেখা যাবে না।
