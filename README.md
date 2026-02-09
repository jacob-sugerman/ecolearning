# EcoLearning VR Experience

An educational VR experience about the Hoh Rainforest, built with [A-Frame](https://aframe.io).

## About

This project is an interactive 3D/VR experience that teaches about the ecology of the Hoh Rainforest in Washington State. Users can explore a virtual environment featuring:
- 3D Earth visualization
- 360° video of forest streams
- Interactive hotspots with educational content about trees, moss, and streams
- Banana slug animations
- Nature sound effects

## ✅ Asset Recovery Available!

**Good News!** This project's assets are available on the Wayback Machine! The media files (3D models, videos, images, audio) can be recovered.

### Quick Start for Asset Recovery

**Method 1: Direct Download (Recommended)**
1. **Open [WAYBACK_URLS.md](WAYBACK_URLS.md)** - Contains direct Wayback Machine links
2. **Click each URL** - Access snapshots from July-August 2022
3. **Download files** - Save to the `assets/` directory
4. **Update HTML:**
   ```bash
   python3 update_asset_paths.py
   ```

**Method 2: Try Automatic Recovery**
   ```bash
   python3 recover_assets.py  # May have network issues
   python3 update_asset_paths.py
   ```

**Method 3: Use Alternatives**
   - See [ALTERNATIVE_ASSETS.md](ALTERNATIVE_ASSETS.md) for free replacement sources
   - See [ASSET_RECOVERY.md](ASSET_RECOVERY.md) for complete details

### Required Assets

The project needs 12 asset files:
- 1 3D model (Earth with clouds)
- 4 images (space background, textures, UI elements)
- 4 videos (slug animations, forest stream)
- 3 audio files (nature sounds)

See [assets/README.md](assets/README.md) for complete list and details.

## How to Use

Once assets are recovered:

1. **Desktop**: Open `index.html` in a modern web browser
   - Click and drag to look around
   - Click on colored spheres to activate interactions

2. **Mobile**: Open on a smartphone
   - Use device motion sensors to look around
   - Tap to interact

3. **VR Headset**: Use a [WebVR-compatible browser](https://aframe.io/docs/1.3.0/introduction/vr-headsets-and-webvr-browsers.html)

## Technology

Built with:
- [A-Frame 1.3.0](https://aframe.io) - WebVR framework
- A-Frame components for orbit controls, video handling, and interactions
- WebGL for 3D rendering

## Project Structure

```
ecolearning/
├── index.html              # Main VR experience
├── assets/                 # Media assets (models, images, videos, audio)
├── recover_assets.py       # Script to recover assets from web archives
├── update_asset_paths.py   # Script to update HTML with local asset paths
├── ASSET_RECOVERY.md       # Detailed asset recovery guide
├── ALTERNATIVE_ASSETS.md   # Guide to free replacement assets
└── README.md              # This file
```

## Development

This is an educational project focused on environmental awareness and rainforest ecology. The interactive elements help users learn about:
- The Hoh Rainforest ecosystem
- Western Hemlock trees
- Moss and its habitats  
- Forest streams and water flow
- Banana slugs

## License

See [LICENSE.md](LICENSE.md) for license information.

## Support A-Frame

If you find this project useful, consider supporting A-Frame:
- [Subscribe to the A-Frame newsletter](https://aframe.io/subscribe/)
- [Sponsor A-Frame development](https://github.com/sponsors/dmarcos)

Make WebVR with HTML and Entity-Component. Works on Vive, Rift, Quest, desktop, mobile platforms.