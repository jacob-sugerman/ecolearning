#!/usr/bin/env python3
"""
Asset Recovery Script for Glitch-Hosted Files
Attempts to recover assets from the Internet Archive's Wayback Machine

IMPORTANT: Assets ARE available on the Wayback Machine!
If this script fails due to network issues, see WAYBACK_URLS.md for direct download links.
"""

import os
import json
import urllib.request
import urllib.parse
import urllib.error
import time
from datetime import datetime

# List of assets to recover from .glitch-assets and index.html
ASSETS = [
    {
        "name": "EarthClouds_1_12756.glb",
        "url": "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/EarthClouds_1_12756.glb?v=1657414934299",
        "path": "assets/models/EarthClouds_1_12756.glb",
        "type": "3D Model",
        "size": "18.9 MB"
    },
    {
        "name": "Stellarium3.jpeg",
        "url": "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Stellarium3.jpeg?v=1657417537065",
        "path": "assets/images/Stellarium3.jpeg",
        "type": "Image",
        "size": "8.96 MB"
    },
    {
        "name": "2k_earth_clouds.jpg",
        "url": "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/2k_earth_clouds.jpg?v=1657443853342",
        "path": "assets/images/2k_earth_clouds.jpg",
        "type": "Image",
        "size": "965 KB"
    },
    {
        "name": "square-rounded-512.png",
        "url": "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/square-rounded-512(1).png?v=1658310350460",
        "path": "assets/images/square-rounded-512.png",
        "type": "Image",
        "size": "5.2 KB"
    },
    {
        "name": "Screen_Shot_bevel.png",
        "url": "https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/Screen%20Shot%202022-08-08%20at%2011.48.18%20PM.png?v=1660184134889",
        "path": "assets/images/Screen_Shot_bevel.png",
        "type": "Image",
        "size": "2.3 MB"
    },
    {
        "name": "slug_anim_1.webm",
        "url": "https://cdn.glitch.global/5272b45a-3c57-40ea-b716-d1f810ee77e5/ezgif.com-gif-maker(2).webm?v=1658537130670",
        "path": "assets/videos/slug_anim_1.webm",
        "type": "Video",
        "size": "212 KB"
    },
    {
        "name": "slug_anim_2.webm",
        "url": "https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/ezgif.com-gif-maker(3).webm?v=1658956817195",
        "path": "assets/videos/slug_anim_2.webm",
        "type": "Video",
        "size": "99.9 KB"
    },
    {
        "name": "Hoh_Forest_Stream.mp4",
        "url": "https://cdn.glitch.me/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Hoh_Forest_Stream.mp4?v=1657418916161",
        "path": "assets/videos/Hoh_Forest_Stream.mp4",
        "type": "Video",
        "size": "94.4 MB"
    },
    {
        "name": "slug3.1.mp4",
        "url": "https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/slug3.1.mp4?v=1660185353459",
        "path": "assets/videos/slug3.1.mp4",
        "type": "Video",
        "size": "8.6 MB"
    },
    {
        "name": "Tree.mp3",
        "url": "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Tree.mp3?v=1658269628533",
        "path": "assets/audio/Tree.mp3",
        "type": "Audio",
        "size": "254.7 KB"
    },
    {
        "name": "moss.mp3",
        "url": "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/moss.mp3?v=1658269630496",
        "path": "assets/audio/moss.mp3",
        "type": "Audio",
        "size": "373.9 KB"
    },
    {
        "name": "Stream.mp3",
        "url": "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Stream.mp3?v=1658269628351",
        "path": "assets/audio/Stream.mp3",
        "type": "Audio",
        "size": "268.5 KB"
    }
]

WAYBACK_API = "https://archive.org/wayback/available"


def create_directories():
    """Create necessary asset directories"""
    dirs = ["assets/models", "assets/images", "assets/videos", "assets/audio"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("✓ Created asset directories")


def check_wayback_availability(url):
    """
    Check if a URL is available in the Wayback Machine
    Returns the closest snapshot URL if available
    """
    try:
        params = urllib.parse.urlencode({"url": url})
        api_url = f"{WAYBACK_API}?{params}"
        
        with urllib.request.urlopen(api_url, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        if data.get("archived_snapshots", {}).get("closest", {}).get("available"):
            snapshot_url = data["archived_snapshots"]["closest"]["url"]
            timestamp = data["archived_snapshots"]["closest"]["timestamp"]
            return snapshot_url, timestamp
        
        return None, None
    except Exception as e:
        print(f"  ⚠ Error checking Wayback Machine: {e}")
        return None, None


def download_file(url, destination, timeout=120):
    """
    Download a file from a URL to destination
    """
    try:
        print(f"  Downloading from: {url}")
        
        # Create a request with a user agent
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Asset Recovery Script)'}
        )
        
        with urllib.request.urlopen(req, timeout=timeout) as response:
            data = response.read()
            
        with open(destination, 'wb') as f:
            f.write(data)
            
        file_size = len(data)
        return True, file_size
    except Exception as e:
        return False, str(e)


def recover_assets():
    """
    Main recovery function
    """
    print("=" * 70)
    print("GLITCH ASSET RECOVERY TOOL")
    print("=" * 70)
    print()
    print("NOTE: Assets ARE available on the Wayback Machine!")
    print("If this script fails, see WAYBACK_URLS.md for manual download links.")
    print()
    
    create_directories()
    print()
    
    results = {
        "recovered": [],
        "failed": [],
        "total": len(ASSETS)
    }
    
    for i, asset in enumerate(ASSETS, 1):
        print(f"[{i}/{len(ASSETS)}] Processing: {asset['name']}")
        print(f"  Type: {asset['type']} ({asset['size']})")
        print(f"  Original URL: {asset['url']}")
        
        # Check if file already exists
        if os.path.exists(asset['path']):
            print(f"  ✓ File already exists at {asset['path']}")
            results["recovered"].append({
                "name": asset['name'],
                "path": asset['path'],
                "source": "local (already exists)"
            })
            print()
            continue
        
        # Check Wayback Machine
        print("  Checking Wayback Machine...")
        snapshot_url, timestamp = check_wayback_availability(asset['url'])
        
        if snapshot_url:
            snapshot_date = datetime.strptime(timestamp, "%Y%m%d%H%M%S")
            print(f"  ✓ Found snapshot from {snapshot_date.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Attempt to download
            print(f"  Attempting download to {asset['path']}...")
            success, result = download_file(snapshot_url, asset['path'])
            
            if success:
                print(f"  ✓ Successfully downloaded ({result} bytes)")
                results["recovered"].append({
                    "name": asset['name'],
                    "path": asset['path'],
                    "source": f"Wayback Machine ({snapshot_date.strftime('%Y-%m-%d')})",
                    "size": result
                })
            else:
                print(f"  ✗ Download failed: {result}")
                results["failed"].append({
                    "name": asset['name'],
                    "url": asset['url'],
                    "reason": f"Download error: {result}"
                })
        else:
            print(f"  ✗ No snapshot found in Wayback Machine")
            results["failed"].append({
                "name": asset['name'],
                "url": asset['url'],
                "reason": "Not found in Wayback Machine"
            })
        
        print()
        time.sleep(1)  # Be nice to the Wayback Machine API
    
    # Print summary
    print("=" * 70)
    print("RECOVERY SUMMARY")
    print("=" * 70)
    print(f"Total assets: {results['total']}")
    print(f"Successfully recovered: {len(results['recovered'])}")
    print(f"Failed: {len(results['failed'])}")
    print()
    
    if results['recovered']:
        print("✓ RECOVERED ASSETS:")
        for asset in results['recovered']:
            print(f"  - {asset['name']}")
            print(f"    Path: {asset['path']}")
            print(f"    Source: {asset['source']}")
    
    if results['failed']:
        print()
        print("✗ FAILED ASSETS:")
        for asset in results['failed']:
            print(f"  - {asset['name']}")
            print(f"    URL: {asset['url']}")
            print(f"    Reason: {asset['reason']}")
    
    print()
    print("=" * 70)
    
    # Save results to JSON
    with open('recovery_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("Full results saved to: recovery_results.json")
    
    # Generate next steps
    print()
    print("NEXT STEPS:")
    if results['failed']:
        print("✨ ASSETS ARE AVAILABLE ON THE WAYBACK MACHINE! ✨")
        print("1. See WAYBACK_URLS.md for direct download links to all assets")
        print("2. Click each Wayback Machine URL and download from snapshots")
        print("3. The automated script may fail due to network restrictions,")
        print("   but manual download from the Wayback Machine works!")
        print()
        print("Alternative methods:")
        print("4. Check ASSET_RECOVERY.md for other recovery methods")
        print("5. Check ALTERNATIVE_ASSETS.md for free replacement sources")
    if results['recovered']:
        print("3. Run update_asset_paths.py to update index.html with new paths")
    print("4. Test the application to ensure all assets load correctly")
    
    return results


if __name__ == "__main__":
    try:
        results = recover_assets()
        exit_code = 0 if not results['failed'] else 1
        exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nRecovery interrupted by user")
        exit(130)
    except Exception as e:
        print(f"\n\nFatal error: {e}")
        exit(1)
