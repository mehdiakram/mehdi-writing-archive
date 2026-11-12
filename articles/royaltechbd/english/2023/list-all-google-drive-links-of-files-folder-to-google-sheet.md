---
archive_id: royaltechbd-3482
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 3482
title: List all Google Drive links of Files / folder to Google Sheet
slug: list-all-google-drive-links-of-files-folder-to-google-sheet
language: en
status: publish
published_at: '2023-12-05T15:53:08'
published_at_gmt: '2023-12-05T09:53:08'
modified_at: '2026-09-28T09:03:15'
modified_at_gmt: '2026-09-28T03:03:15'
original_url: https://www.royaltechbd.com/list-all-google-drive-links-of-files-folder-to-google-sheet/
author: Mehdi Akram
categories:
- Google
tags:
- Drive
- File
- folder
content_hash: 10fe35ad4e81fb04f21ce04e96df3026c7563ec93d160234468611aa3fdc80cc
archived_at: '2026-11-12T08:30:59.043875+00:00'
---

Google Drive is a powerful cloud storage service provided by Google which has a powerful tool called Google Apps Script and it is free. So, we can easily add, modify, delete files present in Google Drive. We can find docs, sheets, and slides by searching File Title, File Contents, etc. Using Google Drive for a while, you find useful of getting a list with URL of all those files and folder in Google Sheet so that you can track content of google drive.

We can easily create a list from Google Drive or export a Google Drive folder structure. So without wasting time let start.

Google Apps Script allows you to create a script that can add, modify and find files and folders present in google drives. We can list all Google Drive links of Files /Folders to Google Sheets with the help of these Google Apps Script.

Step 1 : Create new Google Sheets  
Step 2 : In a sheet title bar ,select “Tools” >> “Script Editor”.  
Step 3 : In the Script Editor, delete everything from the textbox and paste the following script.

```
function onOpen() {
  var SS = SpreadsheetApp.getActiveSpreadsheet();
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Royal')
    .addItem('List All Files and Folders', 'listFilesAndFolders')
    .addToUi();
};


function listFilesAndFolders(){
  var folderId = Browser.inputBox('Enter folder ID', Browser.Buttons.OK_CANCEL);
  if (folderId === "") {
    Browser.msgBox('Folder ID is invalid');
    return;
  }
  getFolderTree(folderId, true); 
};


// Get Folder Tree
function getFolderTree(folderId, listAll) {
  try {
    // Get folder by id
    var parentFolder = DriveApp.getFolderById(folderId);
    
    // Initialise the sheet
    var file, data, sheet = SpreadsheetApp.getActiveSheet();
    sheet.clear();
    sheet.appendRow(["Full Path", "Name","Type" ,"Date", "URL", "Last Updated", "Description", "Size (MB)", "Owner Email"]);
    
    // Get files and folders

    getChildFolders(parentFolder.getName(), parentFolder, data, sheet, listAll);
  } catch (e) {
    Logger.log(e.toString());
  }
};

// Get the list of files and folders and their metadata in recursive mode
function getChildFolders(parentName, parent, data, sheet, listAll) {
  var childFolders = parent.getFolders();
 
  // List folders inside the folder
  while (childFolders.hasNext()) {
    var childFolder = childFolders.next();
    var folderId = childFolder.getId();

    data = [ 
      parentName + "/" + childFolder.getName(),
      childFolder.getName(),
      "Folder",
      childFolder.getDateCreated(),
      childFolder.getUrl(),
      childFolder.getLastUpdated(),
      childFolder.getDescription(),
      childFolder.getSize()/1024,
      childFolder.getOwner().getEmail()
    ];
    // Write
    sheet.appendRow(data);
    
    // List files inside the folder
    var files = childFolder.getFiles();
    while (listAll & files.hasNext()) {
      var childFile = files.next();
      data = [ 
        parentName + "/" + childFolder.getName() + "/" + childFile.getName(),

        childFile.getName(),
        "Files",
        childFile.getDateCreated(),
        childFile.getUrl(),
        childFile.getLastUpdated(),
        childFile.getDescription(),
        childFile.getSize()/1024/1024,
        childFile.getOwner().getEmail(),
      ];
      // Write
      sheet.appendRow(data);
    }
    // Recursive call of the subfolder
    getChildFolders(parentName + "/" + childFolder.getName(), childFolder, data, sheet, listAll);  
  }
};
```

Step 4 : Click on the Edit icon.  
Step 5 : Goto the same Google Sheets File and refresh the page.  
Step 6 : Then you will get the “List Files/Folders” menu, click on it, and select the “List All Files and Folders” item.  
Step 7 : Popup will appear and there type folder Id.  
Step 8 : Press the Ok button in the popup.  
Then all your folders, files links are listed in google docs one by one. Depending on the number of files and folders of Google Drive, it may take some time to display all the files.

**How to get FolderId?**  
To get folderId, first, go to the desired folder in google drive whose files/folders you want to list and then copy the random character just after ‘https://drive.google.com/drive/folders/’ as shown below and then paste it in the above popup.
