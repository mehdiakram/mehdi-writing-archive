---
archive_id: shamokaldarpon-4212
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4212
title: কোন প্লাগইন ছাড়ায় ওয়েবসাইটে কোড প্রদর্শন করা
slug: show-code-using-css-without-plugin
language: bn
status: publish
published_at: '2014-10-26T11:14:41'
published_at_gmt: '2014-10-26T05:14:41'
modified_at: '2014-10-25T11:24:16'
modified_at_gmt: '2014-10-25T05:24:16'
original_url: https://www.shamokaldarpon.com/4212/show-code-using-css-without-plugin
author: মেহেদী আকরাম
categories:
- ওয়েব ডিজাইন এবং ডেভেলপমেন্ট
tags:
- code
- CSS
- pre
- pre tag
- ওয়েবসাইট
- কোড
- সিএসএস
content_hash: 08228902cb885deca4c507c72b68e5b166e4b17511d20f3008b42542ba255111
archived_at: '2026-11-12T08:35:14.713548+00:00'
---

ওয়েব সাইটে php, html বা অনান্য ল্যাঙ্গুয়েজের কোড প্রদর্শনের জন্য আমরা বিভিন্ন প্লাগইন ব্যবহার করে থাকি। যেমন ওয়ার্ডপ্রেসের জন্য SyntaxHighlighter বেশ জনপ্রিয়। তবে চাইলে কোন প্লাগইন ছাড়ায় শুধুমাত্র CSS দ্বারা কোড হাইলাইটার বানানো যায়।  
এজন্য নিচের CSS কোড ব্যবহার করুন এবং কোডে pre ট্যাগ ব্যবহার করুন।  
[pre ট্যাগের ব্যবহার](http://www.w3schools.com/tags/tag_pre.asp)  
নিচের মত pre ট্যাগ ব্যবহার করুন  
![Pre Tag](https://mehdiakram.files.wordpress.com/2014/10/pre-tag.png)

ওয়েবসাইটের নিচের মত কোড দেখাবে  
![Show code using css](https://mehdiakram.files.wordpress.com/2014/10/show-code-using-css.png)

সিএসএস কোড

```

/* Show Code using CSS */
pre:before {
  background-image: url("images/code.png");
  content: " ";
  height: 100%;
  left: 0;
  padding-left: 20px;
  position: absolute;
  top: 0;
  width: 16px;
}

code, pre {
  color: #c63;
  font-family: "Courier New",Courier,monospace;
  font-size: 1em;
  padding-left: 35px;
}

pre {
  border: 1px solid #ddd;
  font-style: normal;
  font-weight: 400;
  margin-bottom: 22px;
  max-height: 1740px;
  overflow: auto;
  padding: 5px 10px 4px 40px;
  width: calc(100% - 52px);
  display: block;
  position: relative;
}
```

[code.png ডাউনলোড করুন](https://mehdiakram.files.wordpress.com/2014/10/code.png)
