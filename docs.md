# SpaceCorps Documentation

Technical documentation for SpaceCorps systems, APIs, simulation physics, and agent protocols.

## Core Services
- **SpaceCorps 2027**: Multiplayer 2D orbital space mechanics game with real-time Newtonian physics.
- **Space3d & Space3d-Molecular**: High-performance Rust game engine and atomistic simulation framework.
- **Native Rust CLIs**: Suite of 23 agentic tools providing autonomous task execution.

## Machine-Readable API
- OpenAPI 3.1.0 specification available at `/openapi.json` and `/openapi.yaml`.
- Authentication details documented in `/auth.md`.
- Pricing and quotas in `/pricing.md`.

## MCP Tools
SpaceCorps exposes standard Model Context Protocol tools:
- `get_game_telemetry`: Retrieve live player counts and cluster health.
- `verify_release_checksum`: Cryptographically verify client binary hashes.
- `query_codex_wiki`: Search game lore, mechanics, factions, and ship specs.
