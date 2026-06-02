#!/usr/bin/env python3
"""
IPInfo CLI - A modern command-line tool for IP address information lookup
Copyright (c) 2026 gitstq
MIT License
"""

import argparse
import json
import sys
import requests
from typing import Optional, Dict, Any
from dataclasses import dataclass
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint

__version__ = "1.0.0"
__author__ = "gitstq"

console = Console()

# API endpoints
IPINFO_API = "https://ipinfo.io/json"
IPINFO_LOOKUP_API = "https://ipinfo.io/{ip}/json"
IPAPI_API = "http://ip-api.com/json/{ip}"
IPAPI_SELF_API = "http://ip-api.com/json/"

@dataclass
class IPInfo:
    """Data class for IP information"""
    ip: str
    hostname: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    loc: Optional[str] = None
    org: Optional[str] = None
    postal: Optional[str] = None
    timezone: Optional[str] = None
    asn: Optional[str] = None
    isp: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "ip": self.ip,
            "hostname": self.hostname,
            "city": self.city,
            "region": self.region,
            "country": self.country,
            "country_code": self.country_code,
            "location": self.loc,
            "organization": self.org,
            "postal": self.postal,
            "timezone": self.timezone,
            "asn": self.asn,
            "isp": self.isp
        }


def get_my_ip() -> IPInfo:
    """Get information about your public IP address"""
    try:
        # Try ipinfo.io first
        response = requests.get(IPINFO_API, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return IPInfo(
                ip=data.get("ip", "N/A"),
                hostname=data.get("hostname"),
                city=data.get("city"),
                region=data.get("region"),
                country=data.get("country"),
                loc=data.get("loc"),
                org=data.get("org"),
                postal=data.get("postal"),
                timezone=data.get("timezone")
            )
        
        # Fallback to ip-api.com
        response = requests.get(IPAPI_SELF_API, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return IPInfo(
                ip=data.get("query", "N/A"),
                city=data.get("city"),
                region=data.get("regionName"),
                country=data.get("country"),
                country_code=data.get("countryCode"),
                loc=f"{data.get('lat')},{data.get('lon')}" if data.get('lat') else None,
                isp=data.get("isp"),
                org=data.get("org"),
                timezone=data.get("timezone")
            )
    except requests.RequestException as e:
        console.print(f"[red]Error fetching IP information: {e}[/red]")
        sys.exit(1)
    
    return IPInfo(ip="N/A")


def lookup_ip(ip_address: str) -> IPInfo:
    """Look up information for a specific IP address"""
    try:
        # Try ipinfo.io first
        url = IPINFO_LOOKUP_API.format(ip=ip_address)
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if "bogon" in data and data["bogon"]:
                console.print(f"[yellow]Warning: {ip_address} is a bogon (private/reserved) IP address[/yellow]")
                return IPInfo(ip=ip_address)
            
            return IPInfo(
                ip=data.get("ip", ip_address),
                hostname=data.get("hostname"),
                city=data.get("city"),
                region=data.get("region"),
                country=data.get("country"),
                loc=data.get("loc"),
                org=data.get("org"),
                postal=data.get("postal"),
                timezone=data.get("timezone")
            )
        
        # Fallback to ip-api.com
        url = IPAPI_API.format(ip=ip_address)
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "fail":
                console.print(f"[red]Error: {data.get('message', 'Unknown error')}[/red]")
                return IPInfo(ip=ip_address)
            
            return IPInfo(
                ip=data.get("query", ip_address),
                city=data.get("city"),
                region=data.get("regionName"),
                country=data.get("country"),
                country_code=data.get("countryCode"),
                loc=f"{data.get('lat')},{data.get('lon')}" if data.get('lat') else None,
                isp=data.get("isp"),
                org=data.get("org"),
                timezone=data.get("timezone")
            )
            
    except requests.RequestException as e:
        console.print(f"[red]Error looking up IP: {e}[/red]")
        sys.exit(1)
    
    return IPInfo(ip=ip_address)


def display_table(info: IPInfo) -> None:
    """Display IP information in a formatted table"""
    table = Table(title=f"🔍 IP Information: {info.ip}", show_header=False, box=None)
    table.add_column("Field", style="cyan bold")
    table.add_column("Value", style="green")
    
    fields = [
        ("🌐 IP Address", info.ip),
        ("🖥️  Hostname", info.hostname or "N/A"),
        ("🏙️  City", info.city or "N/A"),
        ("📍 Region", info.region or "N/A"),
        ("🌍 Country", info.country or "N/A"),
        ("🔤 Country Code", info.country_code or "N/A"),
        ("📌 Location", info.loc or "N/A"),
        ("🏢 Organization", info.org or "N/A"),
        ("📧 Postal Code", info.postal or "N/A"),
        ("⏰ Timezone", info.timezone or "N/A"),
        ("🔌 ISP", info.isp or "N/A"),
        ("📊 ASN", info.asn or "N/A"),
    ]
    
    for field, value in fields:
        if value and value != "N/A":
            table.add_row(field, str(value))
    
    console.print()
    console.print(table)
    console.print()


def display_json(info: IPInfo) -> None:
    """Display IP information in JSON format"""
    console.print_json(json.dumps(info.to_dict(), indent=2))


def display_compact(info: IPInfo) -> None:
    """Display IP information in compact format"""
    console.print(Panel(
        f"[bold cyan]IP:[/bold cyan] {info.ip}\n"
        f"[bold cyan]Location:[/bold cyan] {info.city or 'N/A'}, {info.region or 'N/A'}, {info.country or 'N/A'}\n"
        f"[bold cyan]ISP:[/bold cyan] {info.org or info.isp or 'N/A'}\n"
        f"[bold cyan]Timezone:[/bold cyan] {info.timezone or 'N/A'}",
        title="IPInfo",
        border_style="blue"
    ))


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        prog="ipinfo",
        description="🔍 A modern CLI tool for IP address information lookup",
        epilog="Examples:\n"
               "  ipinfo                    # Show your public IP info\n"
               "  ipinfo 8.8.8.8            # Look up specific IP\n"
               "  ipinfo 1.1.1.1 -j         # Output as JSON\n"
               "  ipinfo -c                 # Compact output",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "ip",
        nargs="?",
        help="IP address to look up (default: your public IP)"
    )
    
    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Output in JSON format"
    )
    
    parser.add_argument(
        "-c", "--compact",
        action="store_true",
        help="Output in compact format"
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    
    args = parser.parse_args()
    
    # Get IP information
    if args.ip:
        info = lookup_ip(args.ip)
    else:
        info = get_my_ip()
    
    # Display result
    if args.json:
        display_json(info)
    elif args.compact:
        display_compact(info)
    else:
        display_table(info)


if __name__ == "__main__":
    main()
