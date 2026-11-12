---
archive_id: royaltechbd-521
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 521
title: Automatic WordPress backup with “BackWPup”
slug: automatic-wordpress-backup-with-backwpup
language: en
status: publish
published_at: '2013-02-10T11:27:12'
published_at_gmt: '2013-02-10T05:27:12'
modified_at: '2026-09-28T09:04:00'
modified_at_gmt: '2026-09-28T03:04:00'
original_url: https://www.royaltechbd.com/automatic-wordpress-backup-with-backwpup/
author: S M Mehdi Akram
categories:
- Wordpress
tags:
- BackPup
- BackWPup
content_hash: 2e1b942d35e1f0df058f307fcbe5f638a1d6c1d62acba658e42155d92e6fa98c
archived_at: '2026-11-12T08:38:58.511427+00:00'
---

BackWPup is a free WordPress plugin that automatically backsup WordPress database and files to web server, FTP, Dropbox, SugarSync, Amazon S3, Google Cloud Storage, Rackspace Cloud and other services. It’s easy to install and configure the plugin.

1. Install and activate the [BackWPup plugin](http://wordpress.org/extend/plugins/backwpup/ "BackWPup plugin") or www.backwpup.com
2. You will have a new BackWPup menu in your WordPress admin menu click **Settings**.
3. In the BackWPup menu, click **Add New**.
4. Set the title.
5. In the **Database Jobs** box, uncheck any tables that don’t need to be backed up.
6. In the **File Backup** box, uncheck any folders that don’t need to be backed up. Under **root.**
7. Configure your backup using one of the **Backup to** dropbox or any you want. You can configure multiple.
8. In the **Job Schedule** box, check **Activate scheduling** and set the schedule. I base the schedule on how frequently the site changes (daily, weekly, or monthly).
9. In the **Backup File** box, you may want to set the **File Format** to *Tar GZip*, which is faster and creates smaller compressed files than standard Zip. It also usually uses less memory, so Tar GZip may work on some hosts when Zip fails.
10. In the **Send log** box, review the settings.
11. In the **Job Type** box (top right), check **Optimize Database Tables** and **Check Database Tables**. Click **Save Changes**.

You should test your backup job after creating it. In the BackWPup menu, click **Jobs**. Below your job, click **Run Now**. The plugin generates logs to aid in troubleshooting.

Explore the rest of the BackWPup menu. **Working** shows the status of currently running backups, **Logs** shows logs, **Backups** lets you view and download backups, and **Tools** lets you restore.

Remember, you can always declutter screens in WordPress by using Screen Options or clicking the top right corner of a box to collapse it.
