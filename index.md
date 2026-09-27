---
title: "SpaceCorps 2027 · Download"
description: "Download SpaceCorps 2027, a space MMO for macOS, Windows and Linux: fly for a corporation, hunt aliens with your clan and climb the season ranking."
canonical: "https://spacecorps.github.io/play/"
version: "0.2.0"
date: "2026-09-26"
server: "https://spacecorps-game.sliplane.app"
publisher: "SpaceCorps"
license: "Proprietary client, Free to play"
engine: "Space3d Engine"
platforms:
  - os: "macOS"
    arch: "universal (Apple Silicon & Intel)"
    format: "dmg"
    filename: "SpaceCorps2027-macos-universal.dmg"
    size: 81818270
    sha256: "fca611cd39fa8fdd0ac5fadec87471c68a91b408628fb233b775469139a8a61d"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-macos-universal.dmg"
  - os: "Windows"
    arch: "x86_64"
    format: "zip"
    filename: "SpaceCorps2027-windows-x86_64.zip"
    size: 77306033
    sha256: "d7aad21b4518ee299f2b91f05ecd5ffafca5bd51332bb93bca3e9cef399adb4f"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-windows-x86_64.zip"
  - os: "Linux"
    arch: "x86_64"
    format: "appimage"
    filename: "SpaceCorps2027-linux-x86_64.AppImage"
    size: 74058232
    sha256: "962206ce91663b9cddc4986e57b069a944554d1893e616e966dccb8be556fe23"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.AppImage"
  - os: "Linux"
    arch: "x86_64"
    format: "tar.gz"
    filename: "SpaceCorps2027-linux-x86_64.tar.gz"
    size: 77937083
    sha256: "0efe0b3ba5b5417f166ffbdc1a21e911846ca82f87c64a716d6e98f4ad3e2a3b"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.tar.gz"
---

# SpaceCorps 2027 · Downloads & System Guide

SpaceCorps 2027 is a multiplayer space action simulator built on the native Space3d engine for macOS, Windows, and Linux. Choose a corporation, customize your starship, coordinate tactical strikes with your clan, hunt alien incursions, and compete for seasonal leaderboards.

- Canonical URL: [https://spacecorps.github.io/play/](https://spacecorps.github.io/play/)
- Machine Interface: [llms.txt](https://spacecorps.github.io/play/llms.txt) | [llms-full.txt](https://spacecorps.github.io/play/llms-full.txt)
- Release Manifest: [release.json](https://spacecorps.github.io/play/release.json)
- Patch Notes: [patchnotes.md](https://spacecorps.github.io/play/patchnotes.md) | [patchnotes.json](https://spacecorps.github.io/play/patchnotes.json)
- GitHub Releases: [https://github.com/SpaceCorps/play/releases/latest](https://github.com/SpaceCorps/play/releases/latest)
- Discord Community: [https://discord.gg/VjW67tkrTb](https://discord.gg/VjW67tkrTb)

---

## Downloads (Version 0.2.0)

| Operating System | Architecture | Package Format | Download Link | SHA-256 Checksum |
| :--- | :--- | :--- | :--- | :--- |
| **macOS** | Universal (Apple Silicon & Intel) | `.dmg` (81.8 MB) | [SpaceCorps2027-macos-universal.dmg](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-macos-universal.dmg) | `fca611cd39fa8fdd0ac5fadec87471c68a91b408628fb233b775469139a8a61d` |
| **Windows** | x86_64 | `.zip` (77.3 MB) | [SpaceCorps2027-windows-x86_64.zip](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-windows-x86_64.zip) | `d7aad21b4518ee299f2b91f05ecd5ffafca5bd51332bb93bca3e9cef399adb4f` |
| **Linux** | x86_64 | `.AppImage` (74.1 MB) | [SpaceCorps2027-linux-x86_64.AppImage](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.AppImage) | `962206ce91663b9cddc4986e57b069a944554d1893e616e966dccb8be556fe23` |
| **Linux** | x86_64 | `.tar.gz` (77.9 MB) | [SpaceCorps2027-linux-x86_64.tar.gz](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.tar.gz) | `0efe0b3ba5b5417f166ffbdc1a21e911846ca82f87c64a716d6e98f4ad3e2a3b` |

---

## What's New

The latest release's patch notes (in English). Every release: [patchnotes.md](https://spacecorps.github.io/play/patchnotes.md) · [patchnotes.html](https://spacecorps.github.io/play/patchnotes.html)

<!-- patchnotes:latest -->
### 0.3.4 · 2026-09-27

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.3.4)

SpaceCorps 2027 0.3.4 gives every item a real 3D model, with its icon rendered from it. You can resize every window in flight from any side or corner, so the Game Log can grow as tall as you like, and the minimap shows the pilots of your own company in green.

#### What's new

**New item art**
- Every item now has a real 3D model, and its icon is a render of that model. The flat drawn icons are gone from the hangar, shop, fusion (Assembly), Galaxy Gates, cargo, hotbar, item tooltips and the wiki's item tables.
- Items of the same family share a look, and tiers read at a glance: higher tiers get more parts, more tick lights on the item and a darker, polished finish. Mark II boosters have twin chambers, fins and two lights.
- Laser ammo colours now match the lasers you see in flight: x1 red, x2 green, x3 blue, x4 magenta.
- Repair drones share one green repair colour; their tier shows in their arms and lights.
- The frame around an item still shows its rarity and fusion level exactly as before.

**Windows in flight**
- Drag any side or corner of a window to resize it, not only the bottom-right corner. The pointer shows the resize arrows over a window's edges.
- The Game Log grows vertically. Drag its top edge up to make it taller over the minimap, or its bottom edge down. Before, dragging it taller did nothing until enough lines had come in.
- The Game Log, Boosters and Active Quests hug their contents until you resize them. After that they keep the size you chose, also on your next flight, and longer contents scroll.
- Chat grows upward when you drag its top edge.

**Minimap**
- Pilots of your own company show as green squares. Before, every other pilot was red like the aliens. Aliens and pilots of other companies stay red.
<!-- /patchnotes:latest -->

---

## Checksum Verification

Verify the integrity of downloaded binaries prior to execution:

### macOS
```bash
shasum -a 256 SpaceCorps2027-macos-universal.dmg
# Expected: fca611cd39fa8fdd0ac5fadec87471c68a91b408628fb233b775469139a8a61d
```

### Windows (PowerShell)
```powershell
Get-FileHash SpaceCorps2027-windows-x86_64.zip -Algorithm SHA256
# Expected: d7aad21b4518ee299f2b91f05ecd5ffafca5bd51332bb93bca3e9cef399adb4f
```

### Linux
```bash
echo "962206ce91663b9cddc4986e57b069a944554d1893e616e966dccb8be556fe23  SpaceCorps2027-linux-x86_64.AppImage" | sha256sum -c -
```

---

## Installation & First Launch

Early alpha release binaries are unsigned; system security prompts will appear on first launch:

### macOS Installation
1. Open `SpaceCorps2027-macos-universal.dmg` and drag **SpaceCorps 2027** into `/Applications`.
2. **macOS 15 Sequoia and newer:** Launch the app once, click *Done*. Then open *System Settings > Privacy & Security*, scroll down to *"SpaceCorps 2027" was blocked*, and click **Open Anyway**.
3. **macOS 12 to 14:** Right-click (or Control-click) `SpaceCorps 2027.app`, choose **Open**, then confirm **Open**.
4. **Terminal Alternative:** Strip the quarantine attribute directly:
   ```bash
   xattr -dr com.apple.quarantine "/Applications/SpaceCorps 2027.app"
   ```

### Windows Installation
1. Right-click `SpaceCorps2027-windows-x86_64.zip` and select **Extract All**.
2. Keep the extracted `assets` folder adjacent to `spacecorps2027.exe`.
3. Launch `spacecorps2027.exe`. If Windows Defender SmartScreen displays a warning, click **More info** followed by **Run anyway**.

### Linux Installation
1. Make the AppImage executable and launch:
   ```bash
   chmod +x SpaceCorps2027-linux-x86_64.AppImage
   ./SpaceCorps2027-linux-x86_64.AppImage
   ```
2. If your distribution lacks FUSE (`libfuse2`), launch using the extract flag:
   ```bash
   ./SpaceCorps2027-linux-x86_64.AppImage --appimage-extract-and-run
   ```
   Or extract the `.tar.gz` archive:
   ```bash
   tar -xzf SpaceCorps2027-linux-x86_64.tar.gz
   ./SpaceCorps2027/spacecorps2027
   ```

---

## Server Connectivity & Game Data

- **Primary Server:** `https://spacecorps-game.sliplane.app`
- **Health Check Endpoint:** `https://spacecorps-game.sliplane.app/health`
- **Alternative Servers:** Switch game servers at runtime via the login screen (*Change server*) or in *Settings > Account > Server*.
- **Local Data Directory:**
  - macOS / Linux: `~/.spacecorps2027`
  - Windows: `%USERPROFILE%\.spacecorps2027`

---

## Supported Languages

SpaceCorps 2027 features complete localized UI, audio, and gameplay text for 10 languages:
- English (`en`)
- German (`de`)
- Spanish (`es`)
- French (`fr`)
- Portuguese - Brazil (`pt-BR`)
- Swedish (`sv`)
- Russian (`ru`)
- Japanese (`ja`)
- Korean (`ko`)
- Simplified Chinese (`zh-CN`)

---

## Technical Specifications & Requirements

- **Graphics Backend:** Native Vulkan, Metal, and DirectX 12 via Space3d Engine.
- **Minimum RAM:** 4 GB.
- **Recommended RAM:** 8 GB.
- **Storage:** 200 MB free disk space.
- **Network:** Broadband internet connection for real-time multiplayer state synchronization.
