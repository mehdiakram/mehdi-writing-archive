---
archive_id: royaltechbd-3465
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 3465
title: Contact Form 7 – Dynamically populate dropdown list
slug: contact-form-7-dynamically-populate-dropdown-list
language: en
status: publish
published_at: '2023-11-30T19:11:08'
published_at_gmt: '2023-11-30T13:11:08'
modified_at: '2026-09-28T09:03:16'
modified_at_gmt: '2026-09-28T03:03:16'
original_url: https://www.royaltechbd.com/contact-form-7-dynamically-populate-dropdown-list/
author: S M Mehdi Akram
categories:
- Tips
tags:
- CF7
- Contact Form 7
- dropdown
- Dynamically
- list
- populate
content_hash: 8651291ec6bd9811da67f0bd1b4c8f8076ecc70946ce0b4c0019d52a5bd0b9fc
archived_at: '2026-11-12T08:38:57.794749+00:00'
---

## Populate Select List

We can achieve the result with some really simple PHP, using the `wpcf7_form_tag_data_option` action hook. I failed to find any good documentation about this powerful feature. That’s why I wrote this post.

```
add_filter( 'wpcf7_form_tag_data_option', 'dynamic_select_list', 10, 3);
function dynamic_select_list($n, $options, $args) {
	if (in_array('division', $options)){
	  $division= array(
		"MAY 07 - NEW ORLEANS, LA",
		"MAY 09 - AUSTIN, TX",
		"MAY 12 - HOUSTON, TX"
	  );
	  return $division;
	}
	return $n;
}
```

Used

```
[select divisionname data:division]
```

[![](https://www.royaltechbd.com/wp-content/uploads/2023/11/Contact-Form-7-1024x512.png)](https://www.royaltechbd.com/wp-content/uploads/2023/11/Contact-Form-7.png)

## Populate Select List With Taxonomy

The following is a more up to date way to dynamically populate the built-in select with options and could easily be extended to support more.

```
add_filter( 'wpcf7_form_tag', 'dynamic_select_taxonomy', 10 );
function dynamic_select_taxonomy( $tag ) {

    // Only run on select lists
    if( 'select' !== $tag['type'] && ('select*' !== $tag['type']) ) {
        return $tag;
    } else if ( empty( $tag['options'] ) ) {
        return $tag;
    }

    $term_args = array();

    // Loop thorugh options to look for our custom options
    foreach( $tag['options'] as $option ) {

        $matches = explode( ':', $option );

        if( ! empty( $matches ) ) {

            switch( $matches[0] ) {

                case 'taxonomy':
                    $term_args['taxonomy'] = $matches[1];
                    break;

                case 'parent':
                    $term_args['parent'] = intval( $matches[1] );
                    break;

            }
        }

    }

    // Ensure we have a term arguments to work with
    if( empty( $term_args ) ) {
        return $tag;
    }

    // Merge dynamic arguments with static arguments
    $term_args = array_merge( $term_args, array(
        'hide_empty' => false,
    ) );

    $terms = get_terms( $term_args );

    // Add terms to values
    if( ! empty( $terms ) && ! is_wp_error( $term_args ) ) {

        foreach( $terms as $term ) {

            $tag['values'][] = $term->name;

        }

    }

    return $tag;

}
```

Uses

```
[select mytaxname taxonomy:category]
```
