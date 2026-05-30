# Awesome VecTrade [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![CI](https://github.com/VecTrade-io/awesome-vectrade/actions/workflows/ci.yml/badge.svg)](https://github.com/VecTrade-io/awesome-vectrade/actions/workflows/ci.yml)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

> A curated list of [VecTrade](https://vectrade.io) integrations, tools, libraries, and community projects.

VecTrade is a unified financial data platform providing real-time quotes, fundamentals, technicals, news, options, earnings, and AI-powered analysis through a single API.

## Contents

- [Official SDKs](#official-sdks)
- [Package Managers](#package-managers)
- [AI & MCP Integrations](#ai--mcp-integrations)
- [Developer Tools](#developer-tools)
- [Example Projects](#example-projects)
- [Community SDKs](#community-sdks)
- [Tools & Utilities](#tools--utilities)
- [Content & Tutorials](#content--tutorials)
- [Related Projects](#related-projects)

## Official SDKs

Official client libraries maintained by the VecTrade team.

- [vectrade-python](https://github.com/VecTrade-io/vectrade-python) — Python SDK with async support, type hints, and pandas integration.
- [vectrade-node](https://github.com/VecTrade-io/vectrade-node) — TypeScript/Node.js SDK with full type safety and tree-shaking.
- [vectrade-cli](https://github.com/VecTrade-io/vectrade-cli) — Cross-platform CLI built in Go. Available via Homebrew, Scoop, and Docker.

## Package Managers

Distribution channels for the VecTrade CLI.

- [homebrew-vectrade](https://github.com/VecTrade-io/homebrew-vectrade) — Homebrew tap for macOS and Linux.
- [scoop-vectrade](https://github.com/VecTrade-io/scoop-vectrade) — Scoop bucket for Windows.

## AI & MCP Integrations

Integrations with AI frameworks and model context protocols.

- [vectrade-mcp](https://github.com/VecTrade-io/vectrade-mcp) — Model Context Protocol server for AI IDEs (Cursor, Windsurf, VS Code).
- [vectrade-ai-provider](https://github.com/VecTrade-io/vectrade-ai-provider) — Vercel AI SDK provider for financial tool calling.

## Developer Tools

Tools for working with the VecTrade API and ecosystem.

- [vectrade-openapi](https://github.com/VecTrade-io/vectrade-openapi) — OpenAPI 3.1 specification with 29 operations across 12 resource groups.
- [vectrade-sdk-generator](https://github.com/VecTrade-io/vectrade-sdk-generator) — SDK contract validator and cross-language alignment tool.
- [finkit](https://github.com/VecTrade-io/finkit) — Standalone financial analysis library (technical indicators, risk metrics, portfolio tools).

## Example Projects

Runnable demos and starter templates.

- [Python Quickstart](https://github.com/VecTrade-io/vectrade-examples/tree/main/python) — Basic Python SDK usage patterns.
- [TypeScript Quickstart](https://github.com/VecTrade-io/vectrade-examples/tree/main/typescript) — TypeScript SDK with async/await.
- [Vercel AI Chatbot](https://github.com/VecTrade-io/vectrade-examples/tree/main/typescript/vercel-ai-chatbot) — AI chatbot with financial tool calling.
- [LangChain Agent](https://github.com/VecTrade-io/vectrade-examples/tree/main/python/langchain_agent.py) — Multi-tool research agent with LangChain.
- [Portfolio Analysis](https://github.com/VecTrade-io/vectrade-examples/tree/main/python/portfolio_analysis.py) — Risk metrics and portfolio optimization with finkit.

## Community SDKs

Client libraries built by the community.

> Want to build an SDK in your language? See the [OpenAPI spec](https://github.com/VecTrade-io/vectrade-openapi) and [SDK generator](https://github.com/VecTrade-io/vectrade-sdk-generator).

- _Your SDK here — [submit a PR](https://github.com/VecTrade-io/awesome-vectrade/pulls)!_

<!-- Bounties available for:
- vectrade-go — Go client
- vectrade-rust — Rust client
- vectrade-ruby — Ruby client
- vectrade-java — Java/Kotlin client
- vectrade-csharp — C# / .NET client
Interested? Open an issue and we'll provide guidance + the OpenAPI spec. -->

## Tools & Utilities

Community-built tools and integrations.

- [VecTrade Rank Badge](https://vectrade.io/api/badge/USERNAME) — Dynamic SVG badge for GitHub READMEs showing your leaderboard rank. Usage: `![Rank](https://vectrade.io/api/badge/your-username)`
- [Leaderboard Embed Widget](https://vectrade.io/leaderboard/embed/USERNAME) — Iframe-embeddable rank card for personal websites and blogs.
- [Weekly Recap Generator](https://github.com/VecTrade-io/vectrade-core/blob/main/scripts/weekly_recap.py) — Auto-generate weekly leaderboard recaps for social media and Discord.

## Content & Tutorials

Blog posts, videos, and educational content.

- [How to Calculate Sharpe Ratio in Python](https://vectrade.io/blog/python-sharpe-ratio-calculation) — Complete guide with finkit examples and portfolio comparison.
- [Build a Stock Screener in 10 Lines of Python](https://vectrade.io/blog/python-stock-screener-tutorial) — Rule-based screening with operators, value+momentum example.
- [Python Technical Indicators Guide](https://vectrade.io/blog/python-technical-indicators-guide) — SMA, EMA, RSI, MACD, Bollinger Bands, ATR, VWAP, OBV with code.
- [VecTrade MCP Setup Guide](https://docs.vectrade.io/sdks/mcp) — Get 27 financial tools in Claude, Cursor, VS Code, and Windsurf.
- [Vercel AI Chatbot with Financial Tools](https://github.com/VecTrade-io/vectrade-examples/tree/main/typescript/vercel-ai-chatbot) — Full-stack AI chatbot with VecTrade tool calling.

## Related Projects

- [VecTrade Documentation](https://github.com/VecTrade-io/vectrade-docs) — Official documentation site source.
- [VecTrade Examples](https://github.com/VecTrade-io/vectrade-examples) — Official example repository.
- [VecTrade Status](https://status.vectrade.io) — Uptime monitoring for all VecTrade services.

## Use Cases

Real-world applications built with VecTrade.

- **Earnings Tracker** — Monitor earnings dates and surprise history for a watchlist. ([template](https://github.com/VecTrade-io/vectrade-examples/tree/main/use-cases))
- **Momentum Scanner** — Daily scanner for stocks breaking 52-week highs with volume confirmation.
- **AI Research Agent** — LangChain agent that researches stocks using VecTrade tools before generating a report.
- **Portfolio Risk Dashboard** — Jupyter notebook combining VecTrade API data with finkit risk metrics.

## Community & Support

- 💬 [Discord](https://discord.gg/vectrade) — Community chat, support, and showcase
- 📖 [Documentation](https://docs.vectrade.io) — Full API reference and guides
- 🐛 [GitHub Issues](https://github.com/VecTrade-io/vectrade-core/issues) — Bug reports and feature requests
- 🐦 [X / Twitter](https://x.com/vectrade_io) — Updates, tips, and weekly leaderboard recaps

---

## Contributing

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related rights to this work. See [LICENSE](LICENSE).
