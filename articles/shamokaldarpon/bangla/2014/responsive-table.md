---
archive_id: shamokaldarpon-4095
source: shamokaldarpon
source_name: সমকাল দর্পণ
wordpress_id: 4095
title: রেসপনসিভ টেবিল
slug: responsive-table
language: bn
status: publish
published_at: '2014-06-03T15:35:58'
published_at_gmt: '2014-06-03T09:35:58'
modified_at: '2015-11-28T09:40:13'
modified_at_gmt: '2015-11-28T03:40:13'
original_url: https://www.shamokaldarpon.com/4095/responsive-table
author: মেহেদী আকরাম
categories:
- ওয়েব ডিজাইন এবং ডেভেলপমেন্ট
tags:
- responsive
- table
- টেবিল
- রেসপনসিভ
content_hash: 23ed3288da54766a5ef402fc5e376a95d93560c785517487505e0eadc94d6782
archived_at: '2026-11-12T08:35:15.801811+00:00'
---

ওয়েবসাইট ডিজাইন করতে অনেকই টেবিল ব্যবহার করে থাকে কিন্তু টেবিলকে রেসপনসিভ করতে পারে না অনেকেই, এখানে একটি টেবিলকে রেসপনসিভ করে দেখানো হয়েছে।

```

<!DOCTYPE html>
<html>
<head>
	<meta charset='UTF-8'>
	<title>Responsive Table</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style type="text/css">
	table.members_details { width: 100%; 	border-collapse: collapse; 	}
	.members_details tr:nth-of-type(odd) { background: #eee; }
	.members_details th { 
		background: #333; 
		color: white; 
		font-weight: bold; 
	}
	.members_details td, .members_details th { 
		padding: 6px; 
		border: 1px solid #ccc; 
		text-align: left; 
	}		
@media only screen and (max-width: 768px)  {
		.members_details > thead { display: none !important;}	
		.text_align_center {text-align: left;}

		.members_details table, .members_details thead, .members_details tbody, .members_details th, .members_details td, .members_details tr { 
			display: block; 
		}
			
		.members_details tr { border: 1px solid #ccc; margin-bottom: 10px;}
		.members_details tr:last-child {margin-bottom: 0;}
		
		.members_details td { 
			position: relative;
			padding: 0 0 0 40%; 
			width: 60%;
			min-height: 18px;
		}
		
		.members_details td:before { 
			position: absolute;
			left: 6px;
			padding-right: 10px; 
			white-space: nowrap;
		}
		
		.members_details td:nth-of-type(1):before { content: "Member ID"; }
		.members_details td:nth-of-type(2):before { content: "Member Name"; }
		.members_details td:nth-of-type(3):before { content: "Profession"}
		.members_details td:nth-of-type(4):before { content: "Blood Group"; }
		.members_details td:nth-of-type(5):before { content: "Mailing Address"; }
		.members_details td:nth-of-type(6):before { content: "Contact"}
	
	}	
	</style>
</head>

<body>

	<div id="page-wrap">
		<h1>Responsive Table</h1>
		<table class="members_details">
			<thead>
				<tr>
					<th class="members_id text_align_center"><b>Member ID</b></th>
					<th class="members_name text_align_center"><b>Name</b></th>
					<th class="members_position text_align_center"><b>Profession</b></th>
					<th class="members_blood_group text_align_center"><b>Blood Group</b></th>
					<th class="members_address text_align_center"><b>Mailing Address</b></th>
					<th class="members_contact text_align_center"><b>Contact</b></th>		
				</tr>
			</thead>
			<tbody>

			<tr>
				<td class="members_id text_align_center">12213</td>
				<td class="members_name">Md. Mahmudul Hasan
				</td><td class="members_position">Head of Procurement &amp; Commercial Navana Furniture Ltd.</td>
				<td class="members_blood_group text_align_center">B+</td>
				<td class="members_address">167/15, 5B, Corner View RA, East Kafrul, Dhaka Cantonment, Dhaka-1206</td>
				<td class="members_contact">01111111111, email@gmail.com</td>		
			</tr>
		
			<tr>

				<td class="members_id text_align_center">231</td>
				<td class="members_name">Rabindra Nath Das
				</td><td class="members_position">Manager-Project, Corporate IT,Navana Group</td>
				<td class="members_blood_group text_align_center">N/A</td>
				<td class="members_address">Dhaka</td>
				<td class="members_contact">01111111111, emailadress@gmail.com</td>		
			</tr>
		
				</tbody>
		</table>
	
	</div>	
</body>
</html>
```
