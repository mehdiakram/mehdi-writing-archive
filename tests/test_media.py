"""Unit tests for media downloader, SSRF protection, and deduplication."""

from pathlib import Path
from unittest.mock import MagicMock, patch

from scripts.media import MediaArchiver, is_safe_url


def test_ssrf_protection_private_ips():
    policy = {"disallow_private_ips": True}
    
    # Disallow localhost / 127.0.0.1
    safe, reason = is_safe_url("http://127.0.0.1/malicious.png", policy)
    assert not safe
    assert "private IP" in reason or "disallowed" in reason

    # Disallow invalid scheme
    safe, reason = is_safe_url("file:///etc/passwd", policy)
    assert not safe
    assert "Unsupported scheme" in reason


def test_media_download_and_deduplication(tmp_path: Path):
    archiver = MediaArchiver(base_media_dir=tmp_path)
    
    mock_image_bytes = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4"
    
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.headers = {"Content-Type": "image/png"}
    mock_resp.iter_content.return_value = [mock_image_bytes]
    
    with patch.object(archiver.session, "get", return_value=mock_resp), \
         patch("scripts.media.is_safe_url", return_value=(True, "")):
        
        # First download
        res1 = archiver.download_image("https://example.com/logo.png", "royaltechbd")
        assert res1["status"] == "completed"
        assert res1["sha256_hash"] is not None
        assert res1["file_size"] == len(mock_image_bytes)
        
        # Second download of identical image
        res2 = archiver.download_image("https://example.com/logo.png", "royaltechbd")
        assert res2["status"] == "completed"
        assert res2["sha256_hash"] == res1["sha256_hash"]
