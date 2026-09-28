# SpaceCorps Pricing, Free Tier & Agent Onboarding

All SpaceCorps command-line tools, client downloads, simulation APIs, agent skill manifests, and developer portals are **100% free and open source**.

## Open Source Commitment

- **License:** Permissive [MIT License](https://opensource.org/licenses/MIT).
- **Cost:** $0.00 / Free forever.
- **Redistribution:** You are free to bundle, distribute, modify, and incorporate SpaceCorps tools into personal, enterprise, and commercial agent pipelines without royalty.
- **Source Repositories:** Available on GitHub under the [SpaceCorps Organization](https://github.com/SpaceCorps).

## Agent Onboarding, Free Tier & Sandbox Environment

- **Free Tier Available:** 100% free tier for developers, automated CI runners, and AI agents at [https://spacecorps.github.io/play/pricing.md](https://spacecorps.github.io/play/pricing.md). No paid subscriptions, no paywalls, and no credit card required.
- **Self-Serve API Keys & Credentials:** Instant self-serve key generation available at [https://spacecorps.github.io/play/api/keys](https://spacecorps.github.io/play/api/keys) and [https://spacecorps.github.io/api/keys](https://spacecorps.github.io/api/keys). Automated agents can immediately use public sandbox key `sc_sandbox_live_automated_agent_key_2027`. No manual registration, signup forms, or "contact sales" gates.
- **Sandbox & Live Test Environment:** Verified live sandbox environment is live at [https://spacecorps.github.io/play/sandbox/](https://spacecorps.github.io/play/sandbox/) (and [https://spacecorps.github.io/sandbox/](https://spacecorps.github.io/sandbox/)) with live health probe at [https://spacecorps.github.io/play/sandbox/api/v1/health](https://spacecorps.github.io/play/sandbox/api/v1/health) and telemetry at [https://spacecorps.github.io/play/sandbox/api/v1/telemetry](https://spacecorps.github.io/play/sandbox/api/v1/telemetry). Run local mock and sandbox instances with zero external dependencies:
  - Spaceemit simulation sandbox: `http://localhost:8741`
  - Offline game simulation & test client runs: `./SpaceCorps2027 --offline`
  - Headless CI pipelines: supported across all 29 tools via `--json`.

## Upstream Platform Services

While SpaceCorps binaries and agent interfaces are completely free, any third-party infrastructure or SaaS services they interface with (such as Sliplane compute, Cloudflare plans, Spaceship domain purchases, Apify scraping compute units, or Exa API queries) are billed directly by their respective providers.
