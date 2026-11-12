---
archive_id: shamokaldarpon-6434
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 6434
title: 'Activepieces ফ্রি: No-Code Automation দিয়ে কাজ অটোমেট করুন'
slug: activepieces-no-code-automation-guide
language: bn
status: publish
published_at: '2026-10-04T10:21:00'
published_at_gmt: '2026-10-04T04:21:00'
modified_at: '2026-10-04T12:22:19'
modified_at_gmt: '2026-10-04T06:22:19'
original_url: https://www.shamokaldarpon.com/6434/activepieces-no-code-automation-guide
author: মেহেদী আকরাম
categories:
- অটোমেশন
- AI
tags:
- Activepieces
- Activepieces Free
- Activepieces Tutorial
- AI Automation
- Automation Tools
- No-Code Automation
- Self Hosted Automation
- workflow automation
- অটোমেশন
- ফ্রি Automation
content_hash: 9a6c7f89b0d1e8d472db4253fdb78c6632deb3bec24ad766a128433b0802085f
archived_at: '2026-11-12T08:36:54.075048+00:00'
---

প্রতিদিন একই ধরনের কাজ বারবার করতে হচ্ছে? Email থেকে তথ্য কপি করা, Google Sheets আপডেট করা, নতুন Form submission থেকে notification পাঠানো, CRM-এ customer যোগ করা কিংবা AI দিয়ে কোনো content process করা, এসব কাজ অনেক সময় স্বয়ংক্রিয়ভাবে করা সম্ভব।

এই কাজের জন্য জনপ্রিয় automation platform যেমন Zapier বা Make-এর পাশাপাশি **Activepieces** একটি শক্তিশালী বিকল্প। বিশেষ করে যারা কম খরচে automation করতে চান এবং প্রয়োজনে নিজের server-এ software চালাতে চান, তাদের জন্য Activepieces বেশ আকর্ষণীয়।

[Activepieces-এর অফিসিয়াল ওয়েবসাইট](https://www.activepieces.com)

![Activepieces No-Code Automation](https://www.shamokaldarpon.com/wp-content/uploads/2026/10/Activepieces-No-Code-Automation-1024x512.png)

## Activepieces কী?

Activepieces হলো একটি open-source automation platform, যার মাধ্যমে বিভিন্ন application, API, webhook এবং AI service-এর মধ্যে workflow তৈরি করা যায়।

সহজভাবে বললে:

**একটি ঘটনা ঘটবে → Activepieces সেটি ধরবে → কয়েকটি কাজ স্বয়ংক্রিয়ভাবে সম্পন্ন করবে।**

যেমন:

**Website Form → Activepieces → Google Sheets → Email Notification**

অথবা:

**New Order → Activepieces → Customer Data → CRM → WhatsApp/SMS Notification**

Activepieces-এর মূল ধারণা হলো Flow। একটি Flow-তে সাধারণত একটি Trigger থাকে এবং এরপর এক বা একাধিক Action চালানো হয়। বর্তমানে Activepieces তাদের platform-এ 760+ app integration এবং হাজার হাজার action থাকার কথা জানিয়েছে।

# Activepieces কি সত্যিই ফ্রি?

হ্যাঁ। তবে এখানে একটি গুরুত্বপূর্ণ বিষয় বুঝতে হবে।

Activepieces ব্যবহারের মূলত দুইটি free পথ আছে:

### ১. Free Cloud Plan

Activepieces-এর cloud version ব্যবহার করতে চাইলে Free plan দিয়ে শুরু করা যায়। বর্তমানে Free plan-এ কোনো credit card প্রয়োজন হয় না এবং এটি $0 মূল্যে দেওয়া হচ্ছে। এতে প্রতিদিন 100 credits, unlimited flows, Flows, Agents, Tables, MCP এবং API access রয়েছে।

তবে cloud free plan-এ daily credit limit আছে। Credit শেষ হয়ে গেলে পরবর্তী refresh পর্যন্ত নতুন run সম্পন্ন হবে না।

### ২. Self-hosted Community Edition

এটাই Activepieces-এর সবচেয়ে আকর্ষণীয় দিকগুলোর একটি।

Activepieces-এর core MIT license-এর অধীনে open source এবং Community Edition নিজের server-এ চালানো যায়। তাদের official documentation অনুযায়ী Community Edition-এ run বা user-এর ওপর credit-based cap নেই।

অর্থাৎ নিজের VPS বা server থাকলে Activepieces নিজেই host করে automation চালানো সম্ভব।

# Self-hosted Activepieces কেন গুরুত্বপূর্ণ?

ধরা যাক আপনার একটি VPS আছে।

আপনি সেখানে Activepieces install করলেন এবং Docker-এর মাধ্যমে চালালেন। তখন automation-এর infrastructure আপনার নিজের server-এ থাকবে।

এর সুবিধা:

- নিজের server ব্যবহার করা যায়
- নিজের data নিজের infrastructure-এ রাখা যায়
- Community Edition-এ runs-এর ওপর credit system নেই
- Open-source code ব্যবহার করা যায়
- প্রয়োজন অনুযায়ী configuration করা যায়
- API ও webhook ব্যবহার করা যায়
- বিভিন্ন application connect করা যায়

Activepieces বর্তমানে Docker Compose এবং Kubernetes সহ একাধিক self-hosting option দেয়। তাদের recommended self-hosting setup Docker Compose-এর সঙ্গে PostgreSQL এবং Redis ব্যবহার করে।

# Activepieces দিয়ে কী কী করা যায়?

Activepieces শুধু সাধারণ app-to-app automation-এর জন্য নয়। এর মাধ্যমে business automation, AI workflow এবং data processing-এর মতো কাজও করা যায়।

## ১. Email Automation

নতুন email আসলে automatically:

- Email থেকে তথ্য বের করা
- Google Sheets-এ save করা
- অন্য কাউকে notification পাঠানো
- AI দিয়ে email summarize করা
- Customer data CRM-এ পাঠানো

এগুলো করা যায়।

## ২. Form Automation

ধরুন আপনার website-এ একটি contact form আছে।

কেউ form submit করলে:

**Form → Activepieces → Database → Email → Notification**

এই পুরো workflow automatically চালানো সম্ভব।

## ৩. Google Sheets Automation

Google Sheets-এর data ব্যবহার করে বিভিন্ন ধরনের automation তৈরি করা যায়।

যেমন:

**New Row → Check Data → AI Processing → Email**

অথবা:

**New Customer → Google Sheets → CRM → Notification**

## ৪. AI Automation

Activepieces-এর AI integration-এর মাধ্যমে AI workflow তৈরি করা যায়। তাদের AI integration-এ structured data extraction এবং agent-based multi-step task-এর মতো capability রয়েছে।

উদাহরণ:

**Customer Email → AI → বুঝবে Customer কী চেয়েছে → Category নির্ধারণ → CRM Update → Reply**

এ ধরনের workflow business-এর repetitive কাজ অনেকটাই কমিয়ে দিতে পারে।

# ৫. API এবং Webhook Automation

Developerদের জন্য Activepieces-এর সবচেয়ে গুরুত্বপূর্ণ সুবিধাগুলোর একটি হলো API এবং webhook support।

আপনার নিজের software যদি webhook পাঠাতে পারে, তাহলে সেই data Activepieces-এর workflow-এ ব্যবহার করা যায়।

যেমন:

**Laravel Application → Webhook → Activepieces → Email + Database + CRM**

অথবা:

**WordPress Plugin → Webhook → Activepieces → Google Sheets**

ফলে আলাদা আলাদা software-এর মধ্যে bridge হিসেবে Activepieces ব্যবহার করা সম্ভব।

# ৬. 760+ Integrations

Activepieces-এর official integration directory অনুযায়ী বর্তমানে 760+ pieces রয়েছে। এগুলোর মাধ্যমে বিভিন্ন application ও service-এর সঙ্গে automation তৈরি করা যায়।

Activepieces-এর ভাষায় একটি Piece হলো একটি application integration, যেখানে সেই application-এর trigger এবং action থাকে।

আর গুরুত্বপূর্ণ বিষয় হলো, integration-এর জন্য আলাদা করে connector কিনতে হয় না। Activepieces তাদের pricing page-এ জানিয়েছে যে integrations প্রতিটি plan-এ অন্তর্ভুক্ত।

# Activepieces-এর Free Cloud বনাম Self-hosted

| বিষয় | Free Cloud | Self-hosted Community |
| --- | --- | --- |
| মূল্য | $0 | Software free |
| Server | Activepieces-এর | নিজের server |
| Credit limit | 100 credits/day | Community Edition-এ run cap নেই |
| Unlimited Flow | হ্যাঁ | হ্যাঁ |
| Open Source | Core | Core |
| Server Management | প্রয়োজন নেই | নিজেকে করতে হবে |
| Data Location | Cloud | নিজের infrastructure |
| Docker | প্রয়োজন নেই | ব্যবহার করা যায় |
| PostgreSQL/Redis | Managed | নিজের setup |
| Customization | সীমিত | বেশি |

Cloud version শুরু করার জন্য সহজ। অন্যদিকে নিজের VPS থাকলে self-hosting বেশি control দেয়।

# Activepieces কি Zapier-এর বিকল্প?

অনেক ক্ষেত্রে Activepieces Zapier-এর বিকল্প হিসেবে ব্যবহার করা যায়।

Zapier-এর মূল সুবিধা হলো cloud-based এবং setup খুব সহজ। Activepieces-এর বড় আকর্ষণ হলো open-source core এবং self-hosting।

একটি সাধারণ তুলনা:

| বিষয় | Activepieces | Zapier |
| --- | --- | --- |
| Free option | আছে | আছে |
| Open-source core | আছে | নেই |
| Self-hosting | আছে | নেই |
| No-code workflow | আছে | আছে |
| API/Webhook | আছে | আছে |
| AI automation | আছে | আছে |
| নিজের server-এ চালানো | সম্ভব | নয় |

আপনার যদি শুধু সহজ automation দরকার হয়, cloud solution যথেষ্ট হতে পারে। কিন্তু নিজের infrastructure-এ automation চালানো, data control এবং customization গুরুত্বপূর্ণ হলে Activepieces-এর self-hosted option বিশেষভাবে কাজে আসতে পারে।

# Activepieces Self-host করতে কী লাগে?

সাধারণভাবে একটি VPS/server, Docker এবং প্রয়োজনীয় database/cache infrastructure দরকার।

Activepieces-এর official installation documentation অনুযায়ী Docker Compose recommended self-hosting method। PostgreSQL এবং Redis ব্যবহার করার setup দেওয়া আছে।

একটি সাধারণ architecture হতে পারে:

**Domain  
↓  
Reverse Proxy  
↓  
Activepieces  
↓  
PostgreSQL + Redis**

আপনি চাইলে Cloudflare এবং SSL ব্যবহার করে এটিকে একটি subdomain-এর মাধ্যমে চালাতে পারেন।

উদাহরণ:

`automation.yourdomain.com`

# Activepieces দিয়ে Business Automation-এর কিছু বাস্তব উদাহরণ

ধরুন আপনার একটি IT company আছে।

একজন নতুন client website-এর contact form পূরণ করল।

তখন automation হতে পারে:

**Contact Form**  
↓  
**Activepieces**  
↓  
**Customer Information Extract**  
↓  
**Google Sheets**  
↓  
**CRM**  
↓  
**Email Notification**  
↓  
**Sales Team Notification**

অর্থাৎ একজন employee-কে manually প্রতিটি ধাপ করতে হচ্ছে না।

আরেকটি উদাহরণ:

**New Order**  
↓  
Activepieces  
↓  
Order Information  
↓  
Invoice System  
↓  
Customer Email  
↓  
Admin Notification

এভাবে repetitive কাজগুলো workflow-এর মাধ্যমে পরিচালনা করা যায়।

# Activepieces এবং AI Agent

Activepieces এখন শুধু traditional automation-এর মধ্যে সীমাবদ্ধ নয়। AI Agent এবং MCP-এর মতো AI-related capability-ও platform-এর অংশ।

Activepieces-এর MCP functionality ব্যবহার করে connected tools-কে AI client-এর কাছে tool হিসেবে expose করা যায়। তাদের documentation অনুযায়ী Claude, Cursor এবং অন্যান্য MCP client-এর সঙ্গে এই ধরনের integration করা যায়।

এর ফলে ভবিষ্যতে workflow এমন হতে পারে:

**AI Agent → Activepieces → CRM → Email → Database → Reporting**

অর্থাৎ AI শুধু উত্তর দেবে না, প্রয়োজন অনুযায়ী connected application-এর ওপর action-ও নিতে পারবে।

# Activepieces-এর সবচেয়ে বড় সুবিধা

Activepieces-এর কয়েকটি বিষয় বিশেষভাবে উল্লেখ করার মতো।

### Open Source

Core MIT license-এর অধীনে open source। চাইলে code দেখা, পরিবর্তন করা এবং নিজের version চালানো যায়।

### Self-hosting

নিজের VPS বা infrastructure-এ চালানো যায়।

### No-code Automation

বেশিরভাগ workflow drag-and-drop interface দিয়ে তৈরি করা যায়।

### AI Support

AI এবং agent-based automation তৈরি করা যায়।

### API ও Webhook

নিজের application-এর সঙ্গে Activepieces connect করা যায়।

### অনেক Integration

760+ integration থাকার কারণে বিভিন্ন service-এর সঙ্গে workflow তৈরি করা যায়।

# Activepieces কার জন্য ভালো?

Activepieces বিশেষভাবে কাজে লাগতে পারে:

- Web Developer
- WordPress Developer
- SaaS Developer
- Digital Marketing Agency
- IT Company
- Freelancer
- Small Business
- Startup
- Automation Specialist
- AI Automation Developer
- যারা নিজের VPS ব্যবহার করেন

বিশেষ করে যারা Docker, VPS, API এবং webhook সম্পর্কে কিছুটা জানেন, তাদের জন্য self-hosted Activepieces বেশ শক্তিশালী একটি option হতে পারে।

# Activepieces কি সম্পূর্ণ ফ্রি?

এখানে বিষয়টি পরিষ্কারভাবে বলা দরকার।

**Activepieces Cloud Free plan সম্পূর্ণ ফ্রি, কিন্তু সেখানে daily credit limit রয়েছে।**

অন্যদিকে **Self-hosted Community Edition-এর MIT-licensed core নিজের infrastructure-এ বিনামূল্যে চালানো যায় এবং Community Edition-এ run/user-এর credit cap নেই।** তবে enterprise features আলাদা commercial license-এর আওতায় পড়ে।

তাই আপনি যদি শুধু শুরু করতে চান, Free Cloud যথেষ্ট।

আর যদি আপনার নিজের VPS থাকে এবং বেশি control চান, তাহলে Self-hosted Community Edition বিবেচনা করা যায়।

# মোট কথা

Automation-এর জন্য সবসময় বড় budget প্রয়োজন হয় না। Activepieces-এর মতো platform ব্যবহার করে ছোট business থেকে শুরু করে বড় ধরনের workflow automation পর্যন্ত তৈরি করা সম্ভব।

বিশেষ করে **open-source + self-hosting + AI + API + 760+ integrations** একসঙ্গে পাওয়ায় Activepieces developers এবং businesses-এর জন্য একটি উল্লেখযোগ্য automation platform হয়ে উঠেছে।

আপনি যদি automation শেখা শুরু করতে চান, তাহলে প্রথমে Free Cloud দিয়ে কয়েকটি simple workflow তৈরি করে দেখা যেতে পারে। পরে প্রয়োজন হলে নিজের VPS-এ Activepieces self-host করা যায়।

**Activepieces-এর সবচেয়ে বড় শক্তি হলো: আপনি চাইলে cloud ব্যবহার করবেন, আবার চাইলে নিজের server-এ automation stack নিজের নিয়ন্ত্রণে চালাবেন।**
