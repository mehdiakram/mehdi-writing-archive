---
archive_id: royaltechbd-1961
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 1961
title: Remove Facebook for WooCommerce from WordPress Database
slug: remove-facebook-for-woocommerce-from-wordpress-database
language: en
status: publish
published_at: '2022-02-20T19:16:57'
published_at_gmt: '2022-02-20T13:16:57'
modified_at: '2026-09-28T09:03:25'
modified_at_gmt: '2026-09-28T03:03:25'
original_url: https://www.royaltechbd.com/remove-facebook-for-woocommerce-from-wordpress-database/
author: Mehdi Akram
categories:
- Wordpress
tags:
- Database
- Facebook for WooCommerce
- Remove
- Wordpress
content_hash: 253b22e978434c7266523069dc33568b4fef9558cc399edfba7937f4fb21ae07
archived_at: '2026-11-12T08:31:03.255697+00:00'
---

Want to Remove Facebook for WooCommerce from WooCommerce data stored in your WordPress database?
[![](https://www.royaltechbd.com/wp-content/uploads/2022/02/facebook-for-woocommerce.png)](https://www.royaltechbd.com/wp-content/uploads/2022/02/facebook-for-woocommerce.png)
– First of all, please backup your database [It is important for security]
– Deactivate Facebook for WooCommerce plugin
– Open your phpMyAdmin page [you might want to ask your host if you’re not sure]
– Then navigate to the SQL section and paste the code below into the white box, lastly please click Go
`` DELETE FROM `wp_options` WHERE option_name LIKE '%wc_facebook_%'; ``
[![](https://www.royaltechbd.com/wp-content/uploads/2022/02/phpadmin-1024x647.png)](https://www.royaltechbd.com/wp-content/uploads/2022/02/phpadmin.png)
**Note:** Sometimes some wordPress database has a unique table prefix, the most common prefix is `wp`, so the table will start like `wp_options`, but if your database has a different prefix, please ensure to adjust accordingly the above code.
Once, the above data removal is completed, please reactivate Facebook for WooCommerce and then go back to `Marketing > Facebook`, and click **Get Started**.
