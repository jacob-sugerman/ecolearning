#!/usr/bin/env python3
"""
Update Asset Paths in index.html
Replaces Glitch CDN URLs with local asset paths
"""

import re
import os
import sys

# Mapping of Glitch URLs to local paths
URL_MAPPINGS = {
    "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/EarthClouds_1_12756.glb?v=1657414934299": "assets/models/EarthClouds_1_12756.glb",
    "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Stellarium3.jpeg?v=1657417537065": "assets/images/Stellarium3.jpeg",
    "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/2k_earth_clouds.jpg?v=1657443853342": "assets/images/2k_earth_clouds.jpg",
    "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/square-rounded-512(1).png?v=1658310350460": "assets/images/square-rounded-512.png",
    "https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/Screen%20Shot%202022-08-08%20at%2011.48.18%20PM.png?v=1660184134889": "assets/images/Screen_Shot_bevel.png",
    "https://cdn.glitch.global/5272b45a-3c57-40ea-b716-d1f810ee77e5/ezgif.com-gif-maker(2).webm?v=1658537130670": "assets/videos/slug_anim_1.webm",
    "https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/ezgif.com-gif-maker(3).webm?v=1658956817195": "assets/videos/slug_anim_2.webm",
    "https://cdn.glitch.me/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Hoh_Forest_Stream.mp4?v=1657418916161": "assets/videos/Hoh_Forest_Stream.mp4",
    "https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/slug3.1.mp4?v=1660185353459": "assets/videos/slug3.1.mp4",
    "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Tree.mp3?v=1658269628533": "assets/audio/Tree.mp3",
    "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/moss.mp3?v=1658269630496": "assets/audio/moss.mp3",
    "https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Stream.mp3?v=1658269628351": "assets/audio/Stream.mp3",
}


def check_assets_exist():
    """Check which assets actually exist"""
    existing = []
    missing = []
    
    for url, path in URL_MAPPINGS.items():
        if os.path.exists(path):
            existing.append((url, path))
        else:
            missing.append((url, path))
    
    return existing, missing


def update_html_file(input_file="index.html", output_file=None, dry_run=False):
    """
    Update HTML file with new asset paths
    If output_file is None, updates in place (after creating backup)
    If dry_run is True, only shows what would be changed
    """
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found")
        return False
    
    # Read the original file
    with open(input_file, 'r') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Replace each URL
    for old_url, new_path in URL_MAPPINGS.items():
        if old_url in content:
            content = content.replace(old_url, new_path)
            changes.append((old_url, new_path))
    
    # Report changes
    if not changes:
        print("No Glitch URLs found in the file - nothing to update")
        return False
    
    print(f"Found {len(changes)} URL(s) to update:")
    for old_url, new_path in changes:
        asset_name = new_path.split('/')[-1]
        exists = "✓ EXISTS" if os.path.exists(new_path) else "✗ MISSING"
        print(f"  - {asset_name} [{exists}]")
        print(f"    From: {old_url}")
        print(f"    To:   {new_path}")
    
    if dry_run:
        print("\n[DRY RUN] No files were modified")
        return True
    
    # Create backup
    if output_file is None:
        backup_file = f"{input_file}.backup"
        with open(backup_file, 'w') as f:
            f.write(original_content)
        print(f"\n✓ Created backup: {backup_file}")
        output_file = input_file
    
    # Write updated content
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"✓ Updated: {output_file}")
    
    # Check for missing assets
    _, missing = check_assets_exist()
    if missing:
        print(f"\n⚠ WARNING: {len(missing)} asset(s) are still missing:")
        for url, path in missing:
            print(f"  - {path}")
        print("\nThe HTML has been updated, but these files need to be recovered.")
        print("Run recover_assets.py or see ASSET_RECOVERY.md for help.")
    
    return True


def main():
    """Main function"""
    print("=" * 70)
    print("ASSET PATH UPDATER")
    print("=" * 70)
    print()
    
    # Parse arguments
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    
    if dry_run:
        print("[DRY RUN MODE - No files will be modified]")
        print()
    
    # Check asset status
    existing, missing = check_assets_exist()
    
    print("Asset Status:")
    print(f"  ✓ Found: {len(existing)}/{len(URL_MAPPINGS)}")
    print(f"  ✗ Missing: {len(missing)}/{len(URL_MAPPINGS)}")
    print()
    
    if missing:
        print("Missing assets:")
        for url, path in missing:
            print(f"  - {path}")
        print()
        print("⚠ Some assets are missing. The HTML will be updated anyway,")
        print("  but you'll need to recover or replace these assets.")
        print()
    
    # Update the HTML file
    success = update_html_file(dry_run=dry_run)
    
    if success and not dry_run:
        print()
        print("=" * 70)
        print("✓ Update complete!")
        print()
        print("Next steps:")
        print("1. Review the changes in index.html")
        print("2. If any assets are missing, recover them using recover_assets.py")
        print("3. Test the application by opening index.html in a browser")
        print("4. If everything works, you can delete index.html.backup")
    elif success and dry_run:
        print()
        print("Run without --dry-run to apply changes")
    
    return 0 if success else 1


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        exit(130)
    except Exception as e:
        print(f"\n\nError: {e}")
        exit(1)
