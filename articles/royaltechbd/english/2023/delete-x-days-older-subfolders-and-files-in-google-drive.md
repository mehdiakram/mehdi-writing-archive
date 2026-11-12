---
archive_id: royaltechbd-3331
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 3331
title: Delete X days older subfolders and files in Google Drive
slug: delete-x-days-older-subfolders-and-files-in-google-drive
language: en
status: publish
published_at: '2023-10-22T18:59:37'
published_at_gmt: '2023-10-22T12:59:37'
modified_at: '2026-09-28T09:03:19'
modified_at_gmt: '2026-09-28T03:03:19'
original_url: https://www.royaltechbd.com/delete-x-days-older-subfolders-and-files-in-google-drive/
author: Mehdi Akram
categories:
- Google
tags:
- Google
- Google Drive
- Tips
content_hash: f5041c372ab8c678f6a5288fe6fd7b9e9251594d069dd99831bad15e7e25bbc7
archived_at: '2026-11-12T08:31:00.816634+00:00'
---

I created a little script to delete subfolders & files in specific folders older than 30 days on Google Drive.It doesn’t permanently delete them, it just puts them in the Trash folder. It works quite well to delete subfolders & files from Google Drive.

[![](https://www.royaltechbd.com/wp-content/uploads/2023/10/SubFoldersInGoogleDrive.png)](https://www.royaltechbd.com/wp-content/uploads/2023/10/SubFoldersInGoogleDrive.png)

```
function DeleteOldFiles() {
  var ManySubFolders = new Array(
    'FOLDER_ID_HERE',
    'FOLDER_ID_HERE',
    'FOLDER_ID_HERE'
  );

  var OldDays = 30 * 24 * 60 * 60 * 1000; // 30 Days

  for (var key in ManySubFolders) {
    var folder = DriveApp.getFolderById(ManySubFolders[key])
    const files = folder.getFiles();
      while (files.hasNext()){
      var file = files.next();

      if (new Date() - file.getLastUpdated() > OldDays) {
        file.setTrashed(true); // Places the file in the Trash folder
      }
    }
    const folders = folder.getFolders();
    while (folders.hasNext()){
      var folder = folders.next();
      if (new Date() - folder.getLastUpdated() > OldDays) {
        folder.setTrashed(true); // Places the file in the Trash folder
      }
    }

  }

}
```

To complete the script, and delete subfolder & files from Google Drive:  
Change **FOLDER\_ID\_HERE** with the folder ID’s you see in Google Drive. You can get them by double-clicking the folder and the URL structure will be something like this: https://drive.google.com/drive/folders/**dfgfdsdfdfghf78ghjn3hbgddfgHyTdfgfdgyz**  
If you have more folders, just keep adding the ID’s to the Array.

The last part is quite easy and it requires you to make the script run once a day. While the Apps Script editor is open, in the menu click **Edit -> All your triggers** and then set a specific time.

[![](https://www.royaltechbd.com/wp-content/uploads/2023/10/googledrivetriggers.png)](https://www.royaltechbd.com/wp-content/uploads/2023/10/googledrivetriggers.png)
