"""WordPress REST API Client for Mehdi's Digital Legacy.

Resilient client with exponential backoff, rate-limiting throttle,
pagination header parsing, and strict error handling.
"""

from __future__ import annotations

import logging
import time
from typing import Any, Dict, Generator, List, Optional, Tuple
import requests

logger = logging.getLogger("archive.wordpress")


class WordPressClientError(Exception):
    """Base exception for WordPress API interactions."""
    pass


class WordPressAPIClient:
    """Robust client for fetching public data from WordPress REST API endpoints."""

    def __init__(
        self,
        base_url: str,
        api_url: str,
        source_key: str,
        timeout: int = 30,
        max_retries: int = 3,
        retry_backoff: float = 1.5,
        delay_ms: int = 250,
        user_agent: Optional[str] = None
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_url = api_url.rstrip("/")
        self.source_key = source_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_backoff = retry_backoff
        self.delay_seconds = max(0.0, delay_ms / 1000.0)
        
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": user_agent or (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36 MehdiArchive/1.0"
            ),
            "Accept": "application/json",
        })

    def _request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Executes HTTP request with exponential backoff retry and throttling."""
        url = endpoint if endpoint.startswith("http") else f"{self.api_url}/{endpoint.lstrip('/')}"
        params = params or {}
        
        if self.delay_seconds > 0:
            time.sleep(self.delay_seconds)
            
        last_exception = None
        current_delay = 1.0
        
        for attempt in range(1, self.max_retries + 1):
            try:
                logger.debug(f"[{self.source_key}] GET {url} (Attempt {attempt}/{self.max_retries}) params={params}")
                resp = self.session.get(url, params=params, timeout=self.timeout)
                
                # Handle rate-limiting (429) or transient server errors (500, 502, 503, 504)
                if resp.status_code in (429, 500, 502, 503, 504):
                    logger.warning(
                        f"[{self.source_key}] Server returned HTTP {resp.status_code} for {url}. "
                        f"Retrying in {current_delay:.1f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= self.retry_backoff
                    continue
                    
                resp.raise_for_status()
                return resp
                
            except (requests.RequestException, ConnectionError, TimeoutError) as e:
                last_exception = e
                logger.warning(
                    f"[{self.source_key}] Request error ({type(e).__name__}: {e}) for {url}. "
                    f"Retrying in {current_delay:.1f}s... (Attempt {attempt}/{self.max_retries})"
                )
                if attempt == self.max_retries:
                    break
                time.sleep(current_delay)
                current_delay *= self.retry_backoff
                
        raise WordPressClientError(
            f"Failed to fetch {url} after {self.max_retries} attempts: {last_exception}"
        ) from last_exception

    def get_site_info(self) -> Dict[str, Any]:
        """Fetches root site information from /wp-json."""
        root_url = f"{self.base_url}/wp-json"
        resp = self._request(root_url)
        return resp.json()

    def get_users(self) -> List[Dict[str, Any]]:
        """Fetches all public users / authors."""
        try:
            resp = self._request("users", params={"per_page": 100})
            return resp.json()
        except Exception as e:
            logger.warning(f"[{self.source_key}] Could not fetch users: {e}")
            return []

    def get_categories(self) -> List[Dict[str, Any]]:
        """Fetches all categories handling pagination."""
        categories: List[Dict[str, Any]] = []
        page = 1
        while True:
            try:
                resp = self._request("categories", params={"per_page": 100, "page": page})
                data = resp.json()
                if not data or not isinstance(data, list):
                    break
                categories.extend(data)
                
                total_pages = int(resp.headers.get("X-WP-TotalPages", 1))
                if page >= total_pages:
                    break
                page += 1
            except Exception as e:
                logger.warning(f"[{self.source_key}] End of categories or error at page {page}: {e}")
                break
        return categories

    def get_tags(self) -> List[Dict[str, Any]]:
        """Fetches all tags handling pagination."""
        tags: List[Dict[str, Any]] = []
        page = 1
        while True:
            try:
                resp = self._request("tags", params={"per_page": 100, "page": page})
                data = resp.json()
                if not data or not isinstance(data, list):
                    break
                tags.extend(data)
                
                total_pages = int(resp.headers.get("X-WP-TotalPages", 1))
                if page >= total_pages:
                    break
                page += 1
            except Exception as e:
                logger.warning(f"[{self.source_key}] End of tags or error at page {page}: {e}")
                break
        return tags

    def get_posts_page(
        self,
        page: int = 1,
        per_page: int = 50,
        modified_after: Optional[str] = None,
        order: str = "asc",
        orderby: str = "modified"
    ) -> Tuple[List[Dict[str, Any]], int, int]:
        """Fetches a single page of published posts with pagination metadata.
        
        Returns:
            Tuple of (posts_list, total_posts, total_pages)
        """
        params: Dict[str, Any] = {
            "status": "publish",
            "per_page": per_page,
            "page": page,
            "orderby": orderby,
            "order": order,
            "_embed": 1,
        }
        if modified_after:
            params["modified_after"] = modified_after
            
        resp = self._request("posts", params=params)
        posts_data = resp.json()
        
        total_posts = int(resp.headers.get("X-WP-Total", len(posts_data)))
        total_pages = int(resp.headers.get("X-WP-TotalPages", 1))
        
        return posts_data, total_posts, total_pages

    def iterate_all_posts(
        self,
        per_page: int = 50,
        modified_after: Optional[str] = None,
        order: str = "asc",
        orderby: str = "modified"
    ) -> Generator[Dict[str, Any], None, None]:
        """Generator that streams all published posts across all pages."""
        page = 1
        total_pages = 1
        
        while page <= total_pages:
            posts, total_count, total_pages = self.get_posts_page(
                page=page,
                per_page=per_page,
                modified_after=modified_after,
                order=order,
                orderby=orderby
            )
            for post in posts:
                yield post
            page += 1

    def get_media_item(self, media_id: int) -> Optional[Dict[str, Any]]:
        """Fetches details for a specific media item by ID."""
        try:
            resp = self._request(f"media/{media_id}")
            return resp.json()
        except Exception as e:
            logger.warning(f"[{self.source_key}] Could not fetch media ID {media_id}: {e}")
            return None
