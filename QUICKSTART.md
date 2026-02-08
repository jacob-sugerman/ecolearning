# Quick Start Guide: Recovering Your Glitch Assets

This guide will help you get your EcoLearning VR project working again after the Glitch shutdown.

## What Happened?

Your project used Glitch.com to host media files (videos, images, 3D models, audio). Glitch is no longer available, so these assets need to be recovered or replaced.

## Three Simple Options

### Option 1: Check for Original Files (Fastest if you have them)

**Look in these places:**
1. Your computer's Downloads folder from July-August 2022
2. Your Documents or Desktop folders
3. Google Drive, Dropbox, or other cloud storage
4. Your phone (if you recorded the audio/video)
5. Email attachments from summer 2022

**If you find them:**
```bash
# 1. Copy files to the right folders (see "File Locations" below)
# 2. Run this command:
python3 update_asset_paths.py
# 3. Open index.html in your browser - done!
```

### Option 2: Try Automatic Recovery (Worth a shot)

```bash
# Run this script - it checks web archives automatically:
python3 recover_assets.py

# Then update your HTML:
python3 update_asset_paths.py

# Test it:
# Open index.html in a browser
```

### Option 3: Use Free Replacements (Most reliable)

If you can't find the originals, use free alternatives:

**Quick replacement checklist:**
- [ ] Earth 3D model → Get from [NASA 3D Resources](https://nasa3d.arc.nasa.gov/models)
- [ ] Space background → Get from [NASA Images](https://images.nasa.gov/)
- [ ] Earth cloud texture → Get from [NASA Visible Earth](https://visibleearth.nasa.gov/)
- [ ] Forest video → Get from [Pexels](https://www.pexels.com/search/videos/forest%20stream/)
- [ ] Slug images/videos → Get from [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Banana_slugs)
- [ ] Nature sounds → Get from [Freesound](https://freesound.org/)
- [ ] UI images → Can skip these or create simple ones

See [ALTERNATIVE_ASSETS.md](ALTERNATIVE_ASSETS.md) for detailed links and instructions.

## File Locations

Put your assets in these exact locations:

```
assets/
├── models/
│   └── EarthClouds_1_12756.glb       ← 3D Earth model
├── images/
│   ├── Stellarium3.jpeg              ← Space background
│   ├── 2k_earth_clouds.jpg           ← Cloud texture
│   ├── square-rounded-512.png        ← UI element (optional)
│   └── Screen_Shot_bevel.png         ← UI border (optional)
├── videos/
│   ├── slug_anim_1.webm              ← Slug animation
│   ├── slug_anim_2.webm              ← Slug animation 2
│   ├── Hoh_Forest_Stream.mp4         ← Forest 360 video
│   └── slug3.1.mp4                   ← Main slug video
└── audio/
    ├── Tree.mp3                      ← Tree sound
    ├── moss.mp3                      ← Moss sound
    └── Stream.mp3                    ← Stream sound
```

## Step-by-Step Process

### Step 1: Choose Your Approach
- Have originals? → Use Option 1
- Not sure? → Try Option 2 first
- Can't find anything? → Use Option 3

### Step 2: Get the Files
- Either find your originals
- OR download replacements from free sources

### Step 3: Organize Files
```bash
# Copy/move files to the correct locations shown above
# Make sure filenames match exactly!
```

### Step 4: Update the HTML
```bash
# This replaces Glitch URLs with local paths:
python3 update_asset_paths.py
```

### Step 5: Test
```bash
# Open index.html in a web browser
# Check the browser console (F12) for errors
# Click around to test interactions
```

## Checking Your Progress

At any time, run this to see what's missing:
```bash
python3 update_asset_paths.py --dry-run
```

This shows:
- ✓ Which files you have
- ✗ Which files are still missing
- No files are changed (just a preview)

## Priority Assets (Start Here)

If you want to get something working quickly, focus on these first:

**Must Have (Project won't work without these):**
1. EarthClouds_1_12756.glb - The 3D Earth model
2. Stellarium3.jpeg - Space background
3. slug3.1.mp4 - Main slug video

**Nice to Have:**
4. Hoh_Forest_Stream.mp4 - The 360° forest video
5. Audio files (Tree.mp3, moss.mp3, Stream.mp3)

**Optional:**
6. Other videos and UI images

## Troubleshooting

**"Script says assets are missing"**
- Double-check filenames match exactly (case-sensitive!)
- Make sure files are in the correct subdirectories
- Run: `ls -R assets/` to see what you have

**"Website shows broken images/videos"**
- Open browser console (F12) to see errors
- Check if update_asset_paths.py was run
- Verify asset files are not corrupted

**"Can't find originals anywhere"**
- That's okay! Use Option 3 (free replacements)
- See ALTERNATIVE_ASSETS.md for direct links

## Need More Help?

See detailed documentation:
- [ASSET_RECOVERY.md](ASSET_RECOVERY.md) - Complete asset details
- [ALTERNATIVE_ASSETS.md](ALTERNATIVE_ASSETS.md) - Where to find replacements
- [assets/README.md](assets/README.md) - Asset directory info

## Contact

If you have questions:
1. Check the GitHub Issues for this repo
2. Ask in the A-Frame community
3. Review the documentation files above

---

**Remember**: The project is still yours and still works! It just needs the media files to be put back in place. You've got this! 🌲🐌
