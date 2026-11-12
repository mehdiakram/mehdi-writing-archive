---
archive_id: shamokaldarpon-2931
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 2931
title: ওয়েবসাইটে উড়ন্ত টুইটার
slug: animated-flying-twitter-bird-for-website
language: bn
status: publish
published_at: '2011-12-07T16:09:38'
published_at_gmt: '2011-12-07T10:09:38'
modified_at: '2023-12-07T17:07:45'
modified_at_gmt: '2023-12-07T11:07:45'
original_url: https://www.shamokaldarpon.com/2931/animated-flying-twitter-bird-for-website
author: মেহেদী আকরাম
categories:
- সামাজিক নেটওয়ার্ক
tags:
- Bird
- Flying Bird
- Internet
- উড়ন্ত
- টুইটার
content_hash: a747f168e2d7e107668678b794b36d1b973a19c7876bfa11f4ce4545a2038372
archived_at: '2026-11-12T08:36:38.811989+00:00'
---

নিজের ওয়েবসাইট আছে অথচ জনপ্রিয় মাইক্রো ব্লগিং টুইটার -এ অ্যাকাউন্ট নেই এমন কাউকে বোধ হয় পাওয়া যাবে না। প্রায় সকল ওয়েবসাইটের টুইটারের অ্যাকাউন্টের লিংক দেওয়া তাকে। তবে চাইলে সহজেই উড়ন্ত টুইটার যুক্ত করা যায়।

এজন্য নিচের কোডটি পেজের ফুটারে/হেডারে যুক্ত করে নিজের অ্যাকাউন্টের জন্য <http://twitter.com/mehdiakram> এর পরিবর্তে নিজের টুইটার অ্যাকাউন্টের লিংক দিতে হবে।

```
<script src="https://mehdiakram.github.io/FlyingTwitbird/js/tripleflap.js"></script>
<a id="theBird" href="http://twitter.com/mehdiakram" target="_blank" style="display: block; position: absolute; width: 64px; height: 64px; background-image: url(https://mehdiakram.github.io/FlyingTwitbird/images/birdsprite.png); background-attachment: initial; background-origin: initial; background-clip: initial; background-color: transparent; z-index: 947; left: 0px; top: 587px; background-position: 0px 0px; background-repeat: no-repeat no-repeat; "></a>
<a id="theBirdLtweet" href="http://twitter.com/home?status=Twitter%20-%20MehdiAkram%20http%3A//www.shamokaldarpon.com/" target="_blank" title="tweet this" style="position: absolute; background-image: url(https://mehdiakram.github.io/FlyingTwitbird/images/birdsprite.png); background-attachment: initial; background-origin: initial; background-clip: initial; background-color: transparent; width: 58px; height: 30px; z-index: 951; left: 49px; top: 583px; display: none; opacity: 0; background-position: -64px 0px; background-repeat: no-repeat no-repeat; "></a>
<a id="theBirdLfollow" href="http://twitter.com/mehdiakram" target="_blank" title="follow me" style="position: absolute; background-image: url(https://mehdiakram.github.io/FlyingTwitbird/images/birdsprite.png); background-attachment: initial; background-origin: initial; background-clip: initial; background-color: transparent; width: 58px; height: 20px; z-index: 952; left: 54px; top: 613px; display: none; opacity: 0; background-position: -64px -30px; background-repeat: no-repeat no-repeat; "></a>


<p>What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
</p>
<p>
Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
</p>
<p>
Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
</p>
<p>
The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
</p>
<p>
Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.</p>   
<script>
var birdSprite="https://mehdiakram.github.io/FlyingTwitbird/images/birdsprite.png";
var targetElems=new Array("img","hr","table","td","div","input","textarea","button","select","ul","ol","li","h1","h2","h3","h4","p","code","object","a","b","strong","span");
var twitterAccount = "http://twitter.com/mehdiakram";var tweetThisText = "Twitter - Mehdi Akram http://www.shamokaldarpon.com/";
tripleflapInit();    
</script>
```

লাইভ দেখুন **[গিটহাব](https://mehdiakram.github.io/FlyingTwitbird/)**, **[কোডপেন](https://codepen.io/mehdiakram/full/RwvvxNV)**

এছাড়াও ওয়ার্ডপ্রেসের জন্য নিচের প্লাগইনটি ব্যাবহার করতে পারেন।  
<http://wordpress.org/extend/plugins/anmiated-twitter-bird/>  
<http://wordpress.org/extend/plugins/fly-twitter-on-blog/>
