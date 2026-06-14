# Kiro MCP Tools Monorepo

This is the monorepo for **Kiro MCP tools** — a comprehensive collection of [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server implementations across a wide range of programming languages, plus Google Cloud Platform (GCP) integrations and supporting utilities.

## What's Here

Each subdirectory is a self-contained MCP server or utility, organized by function, transport, and language.

### MCP Servers — `greet` tool (`mcp-*`)
Simple MCP servers exposing a `greet` tool. Good starting points for new language implementations.

| Transport | Languages |
| :--- | :--- |
| `stdio` | C, C++, COBOL, C#, Dart/Flutter, Fortran, Go, Haskell, Java, Kotlin, Lisp, Perl, PHP, Python, Ruby, Rust, Swift, TypeScript, Zig |
| `https` (SSE) | C, C++, COBOL, C#, Dart/Flutter, Fortran, Go, Haskell, Java, Kotlin, Lisp, Perl, PHP, Python, Ruby, Rust, Swift, TypeScript, Zig |

### MCP Servers — Firestore Inventory (`firestore-*`)
MCP servers that manage a product inventory in Google Cloud Firestore, exposing CRUD tools to MCP clients.

| Transport | Languages |
| :--- | :--- |
| `stdio` | C, C++, COBOL, C#, Dart/Flutter, Fortran, Go, Haskell, Java, Kotlin, Lisp, Perl, PHP, Python, Ruby, Rust, Swift, TypeScript, Zig |
| `https` (SSE) | C, C++, COBOL, C#, Dart/Flutter, Fortran, Go, Haskell, Java, Kotlin, Lisp, Perl, PHP, Python, Ruby, Rust, Swift, TypeScript, Zig |

### Rust Utilities & GCP Integrations
Specialized Rust projects for Cloud Run, Pub/Sub, logging, and GCP API patterns.

| Directory | Description |
| :--- | :--- |
| `cloudrun-rust` | Minimal Cloud Run service |
| `mcp-cloudrun-rust` / `mcp-https-rust` | MCP server on Cloud Run |
| `mcp-client-rust` / `mcp-cli-rust` | MCP client implementations |
| `firestore-client-rust` / `firestore-cli-rust` | Firestore CLI/client tools |
| `pubsub-client-rust` | Pub/Sub messaging patterns |
| `logging-client-rust` / `log-rust` | Cloud Logging patterns |
| `weather-rust` | Weather utility service |
| `gcp-client-rust` | Generic GCP API client |
| `gcp-stdio-client-rust` / `gcp-https-client-rust` / `gcp-cloudrun-client-rust` | GCP client transport variants |

### Other
*   **`battle-royale/`**: Python-based simulations and fun experiments.
*   **`mcp-stdio-python-agy/`**: Python stdio MCP server variant using the `agy` pattern.

## Project Structure

Directories follow a consistent naming convention:
*   `mcp-[transport]-[lang]`: Basic MCP server with `greet` tool.
*   `firestore-[transport]-[lang]`: MCP server with Firestore inventory tools.
*   `gcp-[name]-rust`: GCP-specific Rust utility.

## Root Scripts

| Script | Description |
| :--- | :--- |
| `init.sh` | One-time setup: enables APIs, configures Docker, sets up Firestore |
| `set_env.sh` | Exports `PROJECT_ID`, `REGION`, etc. (`source ./set_env.sh`) |
| `backend.sh` | Build/deploy script for the inventory backend |
| `backend-open.sh` | Deploy to Cloud Run with public access |
| `backend-secure.sh` | Deploy to Cloud Run with restricted access |
| `startproxy.sh` | Start a local proxy for secure Cloud Run testing |
| `enablemcp.sh` | Configure environment for MCP interaction |

## Quick Start

### 1. Initialize
```bash
./init.sh
source ./set_env.sh
```

### 2. Run Locally (stdio)
Most directories use a standard `Makefile`:
```bash
cd mcp-stdio-python
make build
make run
```

### 3. Deploy to Cloud Run (https)
```bash
cd mcp-https-ts
make deploy
```

## AI Assistant Context

Most subdirectories include a `GEMINI.md` file with project-specific context for AI assistants. Each directory also follows standard `Makefile` targets (`build`, `run`, `test`, `deploy`).
