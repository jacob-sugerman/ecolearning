# EcoLearning VR Experience

An educational VR experience about the Hoh Rainforest, built with [A-Frame](https://aframe.io).

## About

This project is an interactive 3D/VR experience that teaches about the ecology of the Hoh Rainforest in Washington State. Users can explore a virtual environment featuring:
- 3D Earth visualization
- 360° video of forest streams
- Interactive hotspots with educational content about trees, moss, and streams
- Banana slug animations
- Nature sound effects

## ⚠️ Asset Recovery Required

**Important**: This project previously hosted assets on Glitch.com. Since Glitch no longer exists, the media assets (3D models, videos, images, audio) need to be recovered or replaced before the project will work.

### Quick Start for Asset Recovery

1. **Attempt automatic recovery from web archives:**
   ```bash
   python3 recover_assets.py
   ```

2. **Check what assets are still needed:**
   ```bash
   python3 update_asset_paths.py --dry-run
   ```

3. **Find replacement assets:**
   - See [ALTERNATIVE_ASSETS.md](ALTERNATIVE_ASSETS.md) for free sources
   - See [ASSET_RECOVERY.md](ASSET_RECOVERY.md) for detailed info

4. **Update HTML once assets are in place:**
   ```bash
   python3 update_asset_paths.py
   ```

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