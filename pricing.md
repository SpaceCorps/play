# SpaceCorps Pricing, Free Tier & Agent Onboarding

All SpaceCorps command-line tools, client downloads, simulation APIs, agent skill manifests, and developer portals are **100% free and open source**.

## Open Source Commitment

- **License:** Permissive [MIT License](https://opensource.org/licenses/MIT).
- **Cost:** $0.00 / Free forever.
- **Redistribution:** You are free to bundle, distribute, modify, and incorporate SpaceCorps tools into personal, enterprise, and commercial agent pipelines without royalty.
- **Source Repositories:** Available on GitHub under the [SpaceCorps Organization](https://github.com/SpaceCorps).

## Agent Onboarding, Free Tier & Sandbox Environment

- **Free Tier Available:** 100% free access for developers, automated CI runners, and AI agents. No paid subscriptions, no paywalls, and no credit card required.
- **Self-Serve API Keys & Credentials:** No manual registration or "contact sales" forms. All public APIs (spaceemit simulation, game release feed, server telemetry) require zero API keys. For authenticated tools, credentials are configured self-serve via platform CLI commands (`login`) or standard environment variables.
- **Sandbox & Local Test Environment:** Run local mock and sandbox instances with zero external dependencies:
  - Spaceemit simulation sandbox: `http://localhost:8741`
  - Offline game simulation & test client runs: `./SpaceCorps2027 --offline`
  - Headless CI pipelines: supported across all 29 tools via `--json`.

## Upstream Platform Services

While SpaceCorps binaries and agent interfaces are completely free, any third-party infrastructure or SaaS services they interface with (such as Sliplane compute, Cloudflare plans, Spaceship domain purchases, Apify scraping compute units, or Exa API queries) are billed directly by their respective providers.
