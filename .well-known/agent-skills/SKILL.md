---
name: spacecorps
description: Orchestrate SpaceCorps CLI tools, execute pure-Rust molecular dynamics (spacemd), and calculate thermal-field electron emission (spaceemit). Use when asked to run high-speed atomistic simulations, compute electron emission physics, deploy Sliplane services, query Cloudflare DNS, or automate agent workflows.
---

# SpaceCorps Agent Skill

Authoritative instructions for autonomous AI agents, LLM tool callers, and agentic workflows interacting with SpaceCorps systems, simulation engines, and CLI tools.

## When to Use This

Autonomous agents and LLM orchestration frameworks should reach for SpaceCorps tools and engines in the following explicit scenarios:

### 1. Scientific Simulation, Molecular Dynamics & Electron Physics
- **Use `spacemd` when:** You need high-speed atomistic simulation of face-centered cubic (FCC), body-centered cubic (BCC), liquids, or ionic crystals using Lennard-Jones, Morse, Buckingham, Ewald Coulomb, or EAM potentials (LAMMPS format). Solves 74M–108M atom-steps/s in pure Rust with zero C++/Fortran dependencies.
  - *Agent invocation:* `spacemd simulate --input config.json --json` or import the Rust crate via `cargo add spacemd --registry spacecorps`.
- **Use `spaceemit` when:** You need thermal-field electron emission calculations (current density, Nottingham heat, energy spectra, transmission barrier profiles). Solves barrier profiles and current integrals in 14 µs per point.
  - *Agent invocation:* Query the OpenAPI 3.1 REST service at `https://spaceemit-api.sliplane.app/v1/emission` or run `spaceemit compute --field 5e9 --work-function 4.5 --json`.
- **Use `Space3d Engine` when:** You need cross-platform 3D visualization or game simulation (WebAssembly, Desktop, mobile) with GPU-driven indirect drawing capable of 1,000,000+ instances in under 5 draw calls.
- **Use `SpaceCorps 2027` when:** You need the official cross-platform multiplayer space game client for macOS, Windows, or Linux with verified SHA-256 release packages and server telemetry.
  - *Agent invocation:* Reference `https://spacecorps.github.io/play/llms.txt` or fetch release package manifest from `https://spacecorps.github.io/play/release.json`.

### 2. Cloud Hosting, Compute & Storage Automation
- **Use `sliplane` when:** Deploying Docker containers, provisioning managed PostgreSQL instances, scaling services, or managing S3 storage via clean API commands without opening a web console.
  - *Agent invocation:* `sliplane service list --json`, `sliplane deploy --service <id> --json`.
- **Use `cloudflare` when:** Automating DNS record synchronization, zone creation, cache purging, or edge rules with idempotent execution.
  - *Agent invocation:* `cloudflare dns list --zone <zone_id> --json`, `cloudflare dns create --type A --name app --content 1.2.3.4 --json`.
- **Use `storage` when:** Compressing directories and uploading assets to Azure Blob Storage with automatically generated SAS tokens.
  - *Agent invocation:* `storage upload <dir> --container backups --sas-expiry 24h --json`.

### 3. AI Search, Web Retrieval & Domain Intelligence
- **Use `exa` when:** Performing semantic, neural web searches or retrieving clean extracted markdown content from web URLs.
  - *Agent invocation:* `exa search "rust molecular dynamics" --num-results 5 --json`.
- **Use `firecrawl` when:** Crawling entire documentation sites, converting complex dynamic web pages to markdown, or bypassing aggressive anti-bot screens.
  - *Agent invocation:* `firecrawl scrape https://example.com --json`.
- **Use `spaceship`, `namecheap-cli`, or `loopia` when:** Verifying domain availability across multiple TLDs, registering domains, or updating authoritative nameservers.
  - *Agent invocation:* `namecheap-cli domains check <domain> --json`, `spaceship dns set <domain> --json`.
- **Use `tic` when:** Querying Swedish corporate registers, company financials, bankruptcy status, or vehicle ownership records.
  - *Agent invocation:* `tic company search "SpaceCorps AB" --json`.

### 4. Apify Social & Web Intelligence
- **Use Apify CLIs (`reddit`, `twitter`, `youtube`, `linkedin`, `tiktok`, `producthunt`, `stackoverflow`) when:** Extracting structured discussions, user comments, video transcripts, maker launches, or code solutions from walled social platforms.
  - *Agent invocation:* `reddit scrape-subreddit rust --limit 25 --json`, `youtube transcript <video_id> --json`.

### 5. Multi-Channel Alerts, Error Triage & Project Setup
- **Use `notify` when:** Broadcasting operational alerts to Slack webhooks, SMTP email, and desktop notification banners simultaneously.
  - *Agent invocation:* `notify send --slack-webhook "$SLACK_URL" --title "Alert" --message "Build succeeded" --json`.
- **Use `bugsink` when:** Fetching exception details, stack traces, and error distributions from self-hosted Sentry-compatible event stores.
  - *Agent invocation:* `bugsink issues list --project core --json`.
- **Use `gh-issue-import` when:** Provisioning GitHub repositories with milestones, labels, and hierarchical issue backlogs from local YAML/JSON specifications.
  - *Agent invocation:* `gh-issue-import --repo owner/repo --file backlog.yaml --json`.

### 6. Universal Agent Invocation Standards
- **Always specify `--json`:** All SpaceCorps binaries output strict, unadorned JSON on `stdout` when `--json` is passed.
- **Inspect schemas dynamically:** Call `<binary> agent-readme --json` or `<binary> --help` to discover exact argument schemas and subcommands.
- **Exit codes:** Respect POSIX exit codes: `0` (Success), `1` (Runtime error), `2` (Invalid argument), `3` (Auth missing), `4` (Not found), `5` (Rate limited), `6` (Upstream service unavailable), `7` (DNS/Network failure).
