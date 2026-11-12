---
archive_id: royaltechbd-1948
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 1948
title: Take Screenshot of Any Website in WordPress
slug: take-screenshot-of-any-website-in-wordpress
language: en
status: publish
published_at: '2022-01-28T17:06:21'
published_at_gmt: '2022-01-28T11:06:21'
modified_at: '2026-09-28T09:03:25'
modified_at_gmt: '2026-09-28T03:03:25'
original_url: https://www.royaltechbd.com/take-screenshot-of-any-website-in-wordpress/
author: Mehdi Akram
categories:
- Wordpress
tags:
- Screenshot
- Website
content_hash: cdbb77946e75144d9107b39efb32d0bf2a26295f84f42fae752060daa49353db
archived_at: '2026-11-12T08:31:02.659101+00:00'
---

Easily take a screenshot on any WordPress page or post using short code.

![](https://s.wordpress.com/mshots/v1/http%3A%2F%2Fwww.royaltechbd.com?w=800&h=600)

```
<?php
add_shortcode( 'snapshot', function ( $atts ) {
	$atts = shortcode_atts( array(
		'alt'    => '',
		'url'    => 'http://www.wordpress.org',
		'width'  => '400',
		'height' => '300'
	), $atts );
	$params = array(
		'w' => $atts['width'],
		'h' => $atts['height'],
	);
	$url = urlencode( $atts['url'] );
	$src = 'http://s.wordpress.com/mshots/v1/' . $url . '?' . http_build_query( $params, null, '&' );

	$cache_key = 'snapshot_' . md5( $src );
	$data_uri = get_transient( $cache_key );
	if ( ! $data_uri ) {
		$response = wp_remote_get( $src );
		if ( 200 === wp_remote_retrieve_response_code( $response ) ) {
			$image_data = wp_remote_retrieve_body( $response );
			if ( $image_data && is_string( $image_data ) ) {
				$src = $data_uri = 'data:image/jpeg;base64,' . base64_encode( $image_data );
				set_transient( $cache_key, $data_uri, DAY_IN_SECONDS );
			}
		}
	}
	return '<img src="' . esc_attr( $src ) . '" alt="' . esc_attr( $atts['alt'] ) . '"/>';
} );
?>
```

Uses

```
[snapshot url="http://www.royaltechbd.com" alt="Royal Technologies" width="800" height="600"]
```
