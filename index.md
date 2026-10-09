---
title: "SpaceCorps 2027 · Download"
description: "Download SpaceCorps 2027, a space MMO for macOS, Windows and Linux: fly for a corporation, hunt aliens with your clan and climb the season ranking."
canonical: "https://spacecorps.github.io/play/"
publisher: "SpaceCorps"
license: "Proprietary client, Free to play"
engine: "Space3d Engine"
# release:front
version: "0.4.18"
date: "2026-10-09"
server: "https://spacecorps-game.sliplane.app"
platforms:
  - os: "macOS"
    arch: "universal (Apple Silicon & Intel)"
    format: "dmg"
    filename: "SpaceCorps2027-macos-universal.dmg"
    size: 147424883
    sha256: "7f9ff21b142ab1557ab9465de5559737b88f313da52a47b3567e7c8ddf6aa750"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-macos-universal.dmg"
  - os: "Windows"
    arch: "x86_64"
    format: "zip"
    filename: "SpaceCorps2027-windows-x86_64.zip"
    size: 142452926
    sha256: "61aae01930054590771e0b9f80bc583de454292de4ac9ad130fa70421c602c7a"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-windows-x86_64.zip"
  - os: "Linux"
    arch: "x86_64"
    format: "appimage"
    filename: "SpaceCorps2027-linux-x86_64.AppImage"
    size: 137566712
    sha256: "0ac978114174cbd26fa6d0e91ad6d553c3fe93a337a060efa00f5384494ec0ae"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.AppImage"
  - os: "Linux"
    arch: "x86_64"
    format: "tar.gz"
    filename: "SpaceCorps2027-linux-x86_64.tar.gz"
    size: 143295736
    sha256: "9eb8afc81d22ba2983b8d426e2e94049e7e223cfe2aace5b88934834fe17e822"
    url: "https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.tar.gz"
# /release:front
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

<!-- release:downloads -->
## Downloads (Version 0.4.18)

| Operating System | Architecture | Package Format | Download Link | SHA-256 Checksum |
| :--- | :--- | :--- | :--- | :--- |
| **macOS** | Universal (Apple Silicon & Intel) | `.dmg` (147.4 MB) | [SpaceCorps2027-macos-universal.dmg](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-macos-universal.dmg) | `7f9ff21b142ab1557ab9465de5559737b88f313da52a47b3567e7c8ddf6aa750` |
| **Windows** | x86_64 | `.zip` (142.5 MB) | [SpaceCorps2027-windows-x86_64.zip](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-windows-x86_64.zip) | `61aae01930054590771e0b9f80bc583de454292de4ac9ad130fa70421c602c7a` |
| **Linux** | x86_64 | `.AppImage` (137.6 MB) | [SpaceCorps2027-linux-x86_64.AppImage](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.AppImage) | `0ac978114174cbd26fa6d0e91ad6d553c3fe93a337a060efa00f5384494ec0ae` |
| **Linux** | x86_64 | `.tar.gz` (143.3 MB) | [SpaceCorps2027-linux-x86_64.tar.gz](https://github.com/SpaceCorps/play/releases/latest/download/SpaceCorps2027-linux-x86_64.tar.gz) | `9eb8afc81d22ba2983b8d426e2e94049e7e223cfe2aace5b88934834fe17e822` |
<!-- /release:downloads -->

---

## What's New

The latest release's patch notes (in English). Every release: [patchnotes.md](https://spacecorps.github.io/play/patchnotes.md) · [patchnotes.html](https://spacecorps.github.io/play/patchnotes.html)

<!-- patchnotes:latest -->
### 0.4.18 · 2026-10-09

[GitHub release](https://github.com/SpaceCorps/play/releases/tag/v0.4.18)

SpaceCorps 2027 0.4.18 fixes the Danger Sector update: the pulsars, the giant excavators and the Dormant Swamp now show when you fly into a Danger Sector through a gate. In 0.4.17 they showed only after you logged in again while standing on the map.

#### What's new

**Fixed**
- **The pulsar, the giant excavator and the Dormant Swamp appear when you jump in.** The server sent them to a pilot who logged in on the map or changed world, but not to one who came through a gate (a jump), so the minimap marks, the excavator's panel and the pictures were missing until the next login. A gate jump now sends them as a login does.

**If you already play**
- The fix is on the server: you need no new game. The server restarts for the update and every pilot who is in a Danger Sector then is sent the sector as before.
- A game of 0.4.16 or older still cannot see any of it; update the game.
- Nobody has played a full excavator run, a Void wave or the swamp for long yet, and the numbers come from a model. Please tell us what feels wrong.
<!-- /patchnotes:latest -->

---

<!-- release:checksums -->
## Checksum Verification

Verify the integrity of downloaded binaries prior to execution:

### macOS
```bash
shasum -a 256 SpaceCorps2027-macos-universal.dmg
# Expected: 7f9ff21b142ab1557ab9465de5559737b88f313da52a47b3567e7c8ddf6aa750
```

### Windows (PowerShell)
```powershell
Get-FileHash SpaceCorps2027-windows-x86_64.zip -Algorithm SHA256
# Expected: 61aae01930054590771e0b9f80bc583de454292de4ac9ad130fa70421c602c7a
```

### Linux
```bash
echo "0ac978114174cbd26fa6d0e91ad6d553c3fe93a337a060efa00f5384494ec0ae  SpaceCorps2027-linux-x86_64.AppImage" | sha256sum -c -
```
<!-- /release:checksums -->

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
2. The whole game is in `spacecorps2027.exe`: there is no `assets` folder to keep next to it.
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

<!-- release:languages -->
## Supported Languages

SpaceCorps 2027 is localized (every page, the HUD, help cards, quests and server messages) in 12 languages:
- English (`en`)
- German (`de`)
- Spanish (`es`)
- French (`fr`)
- Italian (`it`)
- Hungarian (`hu`)
- Portuguese (Brazil) (`pt-BR`)
- Swedish (`sv`)
- Russian (`ru`)
- Japanese (`ja`)
- Korean (`ko`)
- Chinese (Simplified) (`zh-CN`)

This download page (`?lang=<code>`) is translated into 10 of them: `en`, `de`, `es`, `fr`, `pt-BR`, `sv`, `ru`, `ja`, `ko`, `zh-CN`.
<!-- /release:languages -->

---

## Technical Specifications & Requirements

- **Graphics Backend:** Native Vulkan, Metal, and DirectX 12 via Space3d Engine.
- **Minimum RAM:** 4 GB.
- **Recommended RAM:** 8 GB.
- **Storage:** 200 MB free disk space.
- **Network:** Broadband internet connection for real-time multiplayer state synchronization.

---

## Pilot Codex & Game Wiki

Access detailed ship specifications, mechanics, alien encounter logs, and Skylab guides:
- Web: [SpaceCorps 2027 Wiki](https://spacecorps.github.io/play/wiki.html)
- JSON Feed: [wiki.json](https://spacecorps.github.io/play/wiki.json)
- Markdown Mirror: [wiki/](https://spacecorps.github.io/play/wiki/)

