# Asset Recovery Guide for Glitch-Hosted Files

## Problem
This project previously hosted assets on Glitch.com CDN. Since Glitch no longer exists, these assets are inaccessible and need to be recovered and re-hosted.

## Assets Needed

The following assets were identified from `.glitch-assets` and `index.html`:

### 3D Models
1. **EarthClouds_1_12756.glb** (18.9 MB)
   - Original URL: `https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/EarthClouds_1_12756.glb`
   - UUID: `AjXYc0o4XhaajEZR`
   - Purpose: 3D Earth model for the scene

### Images
2. **Stellarium3.jpeg** (8.96 MB, 8192x4096)
   - Original URL: `https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Stellarium3.jpeg`
   - UUID: `PebFs1BIburbF75Z`
   - Purpose: Space/stars background skybox

3. **2k_earth_clouds.jpg** (965 KB, 2048x1024)
   - Original URL: `https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/2k_earth_clouds.jpg`
   - UUID: `lQHZHaz6vlJevngq`
   - Purpose: Cloud texture for Earth

4. **square-rounded-512(1).png** (5.2 KB, 512x512)
   - Original URL: `https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/square-rounded-512(1).png`
   - UUID: `RAsUTYNsLD0Wufab`
   - Purpose: UI element/button bevel

5. **Screen Shot 2022-08-08 at 11.48.18 PM.png** (2.3 MB, 14400x9000)
   - Original URL: `https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/Screen%20Shot%202022-08-08%20at%2011.48.18%20PM.png`
   - UUID: `irfX2uF6r2wk2ekA`
   - Purpose: UI element/border

6. **pngwing.com.png** (10.9 KB, 1600x1600)
   - Original URL: `https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/pngwing.com.png`
   - UUID: `dyC0tZVpoQywa88A`
   - Purpose: Additional UI element (not currently in index.html)

### Videos
7. **ezgif.com-gif-maker(2).webm** (212 KB)
   - Original URL: `https://cdn.glitch.global/5272b45a-3c57-40ea-b716-d1f810ee77e5/ezgif.com-gif-maker(2).webm`
   - UUID: `AKK7Hhgr0edDvoJg`
   - Purpose: Slug animation video (slug material)

8. **ezgif.com-gif-maker(3).webm** (99.9 KB)
   - Original URL: `https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/ezgif.com-gif-maker(3).webm`
   - UUID: `c2wakjecdXxru5K2`
   - Purpose: Slug animation video 2 (slug2 material)

9. **Hoh_Forest_Stream.mp4** (94.4 MB)
   - Original URL: `https://cdn.glitch.me/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Hoh_Forest_Stream.mp4`
   - UUID: `xSNIkLYdHDciprYy`
   - Purpose: 360° video of forest stream (streamvid videosphere)

10. **slug3.1.mp4** (8.6 MB)
    - Original URL: `https://cdn.glitch.global/769659af-e334-4469-8ae9-89981faea934/slug3.1.mp4`
    - UUID: `LYeO8DWOI5k47Ip0`
    - Purpose: Slug video (colors material, main video)

### Audio Files
11. **Tree.mp3** (254.7 KB)
    - Original URL: `https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Tree.mp3`
    - UUID: `VjgXiQVdTe3yhDOc`
    - Purpose: Tree/forest sound effect (sound1)

12. **moss.mp3** (373.9 KB)
    - Original URL: `https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/moss.mp3`
    - UUID: `9ckebHgQxUfomx8n`
    - Purpose: Moss sound effect (sound2)

13. **Stream.mp3** (268.5 KB)
    - Original URL: `https://cdn.glitch.global/57a2561b-bbb0-4ad1-85a3-ecb8c6f6011a/Stream.mp3`
    - UUID: `6bFZznLOfSFyFRWp`
    - Purpose: Stream water sound effect (sound3)

## Recovery Methods

### ✅ Method 1: Wayback Machine (CONFIRMED AVAILABLE!)

**The assets ARE available on the Wayback Machine!**

See **[WAYBACK_URLS.md](WAYBACK_URLS.md)** for direct Wayback Machine URLs to all 12 assets.

**Steps:**
1. Open WAYBACK_URLS.md
2. Click the Wayback Machine URL for each asset
3. Select a snapshot from July-August 2022
4. Download the file and save it to the specified path
5. Repeat for all 12 assets

**Automated approach:**
```bash
python3 recover_assets.py
```

This script will attempt to find and download assets from the Wayback Machine automatically. Note: May encounter network restrictions in some environments, so manual download from WAYBACK_URLS.md is recommended.

### Method 2: Manual Web Archive Search
Visit the Wayback Machine manually:
- Go to https://web.archive.org/
- Enter each Glitch URL
- Look for snapshots from 2022 (July-August when assets were uploaded)
- Download manually if found

### Method 3: Original Source Files
If you have the original project files or backups:
1. Check local computer downloads/documents
2. Check email attachments from 2022
3. Check cloud storage (Google Drive, Dropbox, etc.)
4. Check other devices used during development

### Method 4: Alternative Assets
For some assets, you may be able to find alternatives:
- **Stellarium3.jpeg**: Space/stars skybox - can use free alternatives from NASA or generate with Stellarium software
- **2k_earth_clouds.jpg**: Earth texture - available from various free texture sites
- **Tree.mp3, moss.mp3, Stream.mp3**: Nature sound effects - available from freesound.org or similar sites
- **EarthClouds_1_12756.glb**: 3D Earth model - available from Sketchfab or other 3D model sites

## Next Steps

1. Run the recovery script
2. Check which assets were successfully recovered
3. For missing assets:
   - Search for original files locally
   - Find suitable replacements
   - Consider creating new assets
4. Update `index.html` to point to new asset locations
5. Test the application with recovered/replacement assets

## Asset Directory Structure

Once recovered, assets should be organized as:
```
assets/
├── models/
│   └── EarthClouds_1_12756.glb
├── images/
│   ├── Stellarium3.jpeg
│   ├── 2k_earth_clouds.jpg
│   ├── square-rounded-512.png
│   ├── Screen_Shot_bevel.png
│   └── pngwing.com.png
├── videos/
│   ├── slug_anim_1.webm
│   ├── slug_anim_2.webm
│   ├── Hoh_Forest_Stream.mp4
│   └── slug3.1.mp4
└── audio/
    ├── Tree.mp3
    ├── moss.mp3
    └── Stream.mp3
```

## Hosting Options After Recovery

1. **GitHub (Recommended for this repo)**
   - Store assets in the repository
   - Use GitHub Pages for hosting
   - Free and integrated with your code

2. **GitHub Releases**
   - Upload large files as release assets
   - Good for files over 50MB

3. **Cloudflare R2 or AWS S3**
   - Cloud storage with CDN
   - Pay-as-you-go pricing

4. **Netlify or Vercel**
   - Automatic deployment
   - Free tier available

## Important Notes

- Original upload dates: July-August 2022
- Total asset size: ~135 MB
- Largest file: Hoh_Forest_Stream.mp4 (94.4 MB)
- Project appears to be an educational VR experience about the Hoh Rainforest
