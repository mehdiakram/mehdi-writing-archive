---
archive_id: royaltechbd-3517
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 3517
title: Google Drive – List all files id inside a folder (no subfolders)
slug: google-drive-list-all-files-id-inside-a-folder-no-subfolders
language: en
status: publish
published_at: '2023-12-19T13:28:58'
published_at_gmt: '2023-12-19T07:28:58'
modified_at: '2026-09-28T09:03:13'
modified_at_gmt: '2026-09-28T03:03:13'
original_url: https://www.royaltechbd.com/google-drive-list-all-files-id-inside-a-folder-no-subfolders/
author: S M Mehdi Akram
categories:
- Google
- Tips
tags: []
content_hash: 25e3bebcf0a571cc763d3f633edff578dde64554f356f3ab00c7d7e87029529d
archived_at: '2026-11-12T08:38:56.497831+00:00'
---

If you want to list in a spreadsheet all files id that are located inside a folder (no subfolders).

```
function list_all_files_inside_a_folder(){
  var sh = SpreadsheetApp.getActiveSheet();
  var folder = DriveApp.getFolderById('1a1SkFgbMIr_8z1HnZvIpUPcOQ0NWp3HL'); //Change the folder ID here 
  var list = [];
  sh.clear();
  list.push(['File Name','File ID','Size(MB)']);
  var files = folder.getFiles();
  while (files.hasNext()){
    file = files.next();
    var row = []
    row.push(file.getName(),file.getId(),file.getSize()/1048576)
    list.push(row);
  }
   sh.getRange(1,1,list.length,list[0].length).setValues(list);
}
```
