#!/usr/bin/env python3
"""
Unit tests for IPInfo CLI
"""

import json
import pytest
from unittest.mock import patch, MagicMock
from ipinfo import (
    IPInfo,
    get_my_ip,
    lookup_ip,
    display_table,
    display_json,
    display_compact
)


class TestIPInfo:
    """Tests for IPInfo dataclass"""
    
    def test_ipinfo_creation(self):
        """Test IPInfo object creation"""
        info = IPInfo(
            ip="8.8.8.8",
            hostname="dns.google",
            city="Mountain View",
            region="California",
            country="United States",
            loc="37.3860,-122.0838",
            org="Google LLC"
        )
        
        assert info.ip == "8.8.8.8"
        assert info.hostname == "dns.google"
        assert info.city == "Mountain View"
        assert info.region == "California"
        assert info.country == "United States"
    
    def test_ipinfo_to_dict(self):
        """Test IPInfo to_dict method"""
        info = IPInfo(
            ip="1.1.1.1",
            city="Sydney",
            country="Australia"
        )
        
        result = info.to_dict()
        
        assert result["ip"] == "1.1.1.1"
        assert result["city"] == "Sydney"
        assert result["country"] == "Australia"
        assert result["hostname"] is None


class TestGetMyIP:
    """Tests for get_my_ip function"""
    
    @patch('ipinfo.requests.get')
    def test_get_my_ip_success(self, mock_get):
        """Test successful IP retrieval"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "ip": "1.2.3.4",
            "city": "New York",
            "region": "New York",
            "country": "US",
            "loc": "40.7128,-74.0060",
            "org": "Example ISP",
            "timezone": "America/New_York"
        }
        mock_get.return_value = mock_response
        
        result = get_my_ip()
        
        assert result.ip == "1.2.3.4"
        assert result.city == "New York"
        assert result.country == "US"


class TestLookupIP:
    """Tests for lookup_ip function"""
    
    @patch('ipinfo.requests.get')
    def test_lookup_ip_success(self, mock_get):
        """Test successful IP lookup"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "ip": "8.8.8.8",
            "hostname": "dns.google",
            "city": "Mountain View",
            "region": "California",
            "country": "US",
            "loc": "37.3860,-122.0838",
            "org": "Google LLC"
        }
        mock_get.return_value = mock_response
        
        result = lookup_ip("8.8.8.8")
        
        assert result.ip == "8.8.8.8"
        assert result.hostname == "dns.google"
        assert result.org == "Google LLC"
    
    @patch('ipinfo.requests.get')
    def test_lookup_bogon_ip(self, mock_get):
        """Test bogon IP handling"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "ip": "192.168.1.1",
            "bogon": True
        }
        mock_get.return_value = mock_response
        
        result = lookup_ip("192.168.1.1")
        
        assert result.ip == "192.168.1.1"


class TestDisplayFunctions:
    """Tests for display functions"""
    
    def test_display_json(self, capsys):
        """Test JSON output"""
        info = IPInfo(
            ip="1.1.1.1",
            city="Sydney",
            country="Australia"
        )
        
        display_json(info)
        captured = capsys.readouterr()
        
        # Verify JSON is valid
        output = json.loads(captured.out)
        assert output["ip"] == "1.1.1.1"
        assert output["city"] == "Sydney"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
