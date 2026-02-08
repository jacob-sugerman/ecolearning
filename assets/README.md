# Assets Directory

This directory contains the media assets for the EcoLearning VR experience.

## Directory Structure

```
assets/
├── models/          # 3D models (.glb, .gltf)
├── images/          # Textures and UI images (.jpg, .jpeg, .png)
├── videos/          # Video files (.mp4, .webm)
└── audio/           # Sound effects and audio (.mp3)
```

## Required Assets

The application needs the following files to function properly:

### Models (assets/models/)
- `EarthClouds_1_12756.glb` - 3D Earth model with clouds

### Images (assets/images/)
- `Stellarium3.jpeg` - Space/stars background (8192x4096)
- `2k_earth_clouds.jpg` - Earth cloud texture (2048x1024)
- `square-rounded-512.png` - UI bevel element (512x512)
- `Screen_Shot_bevel.png` - UI border element

### Videos (assets/videos/)
- `slug_anim_1.webm` - Banana slug animation video
- `slug_anim_2.webm` - Secondary slug animation
- `Hoh_Forest_Stream.mp4` - 360° forest stream video
- `slug3.1.mp4` - Main slug video content

### Audio (assets/audio/)
- `Tree.mp3` - Tree/forest ambient sound
- `moss.mp3` - Moss ambient sound
- `Stream.mp3` - Stream water sound effect

## Obtaining Assets

These assets were originally hosted on Glitch.com and are no longer accessible. See the repository root for:

- **ASSET_RECOVERY.md** - Detailed information about each asset and recovery methods
- **ALTERNATIVE_ASSETS.md** - Guide to finding free replacement assets
- **recover_assets.py** - Script to attempt recovery from web archives

## Asset Guidelines

When adding or replacing assets:

1. **File Naming**: Use the exact filenames listed above
2. **Format**: Keep the original formats for compatibility
3. **Quality**: Try to match or exceed original quality
4. **Size**: Be mindful of file sizes for web performance
5. **Licenses**: Ensure you have rights to use the assets
6. **Attribution**: Document sources in ATTRIBUTIONS.md if required

## Testing

After adding assets, test by:
1. Opening `index.html` in a web browser
2. Checking the browser console for errors
3. Verifying all 3D models, textures, videos, and sounds load
4. Testing interactivity (clicking on elements)

## Current Status

Run this command from the repository root to check which assets are present:

```bash
python3 update_asset_paths.py --dry-run
```

## Need Help?

See:
- [ASSET_RECOVERY.md](../ASSET_RECOVERY.md) for detailed recovery instructions
- [ALTERNATIVE_ASSETS.md](../ALTERNATIVE_ASSETS.md) for free replacement sources
- [README.md](../README.md) for project information
