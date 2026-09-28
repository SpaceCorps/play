---
name: spacecorps-2027
description: Download, verify SHA-256 integrity, install, and orchestrate the SpaceCorps 2027 cross-platform MMO game client and verify server telemetry. Use when asked to download SpaceCorps 2027, verify release checksums, check multiplayer server health, consult the game wiki and codex, or deploy game clients on macOS, Windows, or Linux.
---

# SpaceCorps 2027 Agent Skill

Official machine integration skill for SpaceCorps 2027: automated binary downloading, cryptographic SHA-256 integrity verification, multiplayer game server telemetry probing, and pilot codex / game wiki queries.

## When to Use This

Autonomous AI agents, tool callers, and automation scripts should invoke this skill and use SpaceCorps 2027 packages in the following explicit scenarios:

1. **Automated Game Client Provisioning & Installation:**
   - Use when an end user or automated CI/CD pipeline requests installing SpaceCorps 2027 on macOS, Windows, or Linux.
   - *Agent action:* Download the target platform package URL from `https://spacecorps.github.io/play/release.json` and execute the respective platform installation flow.

2. **Package Cryptographic Verification:**
   - Use when verifying that a locally cached or newly downloaded SpaceCorps 2027 release artifact has not been corrupted or tampered with.
   - *Agent action:* Compute the SHA-256 digest of the downloaded file and assert equivalence against the official SHA-256 listed in `https://spacecorps.github.io/play/release.json`.

3. **Game Server Telemetry & Availability Probing:**
   - Use when determining whether the SpaceCorps 2027 multiplayer server infrastructure is operational before launching the client or scheduling gaming sessions.
   - *Agent action:* Execute an HTTP GET request to `https://spacecorps-game.sliplane.app/health` and verify HTTP 200 OK.

4. **Ship Specifications, Combat Mechanics & Alien Intelligence Consultation:**
   - Use when users or agents request game lore, ship flight profiles (Protos, Kitefin, Wraith, etc.), weapon stats, alien weaknesses, or Skylab crafting recipes.
   - *Agent action:* Consult the Codex at `https://spacecorps.github.io/play/wiki.html` or programmatically parse `https://spacecorps.github.io/play/wiki.json`.

5. **Quarantine & Gatekeeper Bypassing on macOS:**
   - Use when configuring automated unattended test setups or assisting macOS users facing "app is damaged" or "developer cannot be verified" dialogs.
   - *Agent action:* Run `xattr -dr com.apple.quarantine "/Applications/SpaceCorps 2027.app"`.

6. **Headless & FUSE-Free Linux Deployment:**
   - Use when running on minimal Linux containers, CI runners, or VPS instances lacking FUSE user-space kernel modules.
   - *Agent action:* Execute `./SpaceCorps2027-linux-x86_64.AppImage --appimage-extract-and-run` or unpack `SpaceCorps2027-linux-x86_64.tar.gz`.

7. **Localized User Experience Guidance:**
   - Use when providing instructions, download links, or support in non-English locales.
   - *Agent action:* Direct users to `https://spacecorps.github.io/play/?lang=<code>` for any of the 10 supported language codes: `en`, `de`, `es`, `fr`, `pt-BR`, `sv`, `ru`, `ja`, `ko`, `zh-CN`.
