# Kiro Context

This document provides context for the Kiro AI assistant to understand the project.

Do NOT USE VENV

## Project Overview

This is a **Python-based Model Context Protocol (MCP) server** using the `FastMCP` class from the `mcp` SDK. It is designed to expose tools (like `greet`) over standard input/output (stdio) for integration with MCP clients (such as Claude Desktop or Kiro).

## Key Technologies

*   **Language:** Python 3
*   **SDK:** `mcp` (Model Context Protocol SDK)
*   **Library:** `FastMCP` (for simplified server creation)
*   **Logging:** `python-json-logger`
*   **Dependency Management:** `pip` / `requirements.txt`

## Project Structure

*   `main.py`: The entry point. Initializes the `FastMCP` server ("hello-world-server") and defines tools.
*   `requirements.txt`: Python dependencies.
*   `Makefile`: Development shortcuts (test, lint, clean). *Note: Some targets may reference legacy paths and might need adjustment.*

## Development Setup

```bash
make install
# Or:
python3 -m pip install --break-system-packages -r requirements.txt
```

## Running the Server

```bash
python3 main.py
```

*Note: This is an MCP server running over stdio — typically spawned by an MCP client, not run directly.*

## Resources

*   **MCP Python SDK:** [https://github.com/mcp-protocol/mcp-python-sdk](https://github.com/mcp-protocol/mcp-python-sdk)
*   **FastMCP Docs:** [https://gofastmcp.com/](https://gofastmcp.com/)
*   **`mcp` on PyPI:** [https://pypi.org/project/mcp/](https://pypi.org/project/mcp/)

## Known Issues

*   `Dockerfile`: Configured for Node.js — needs update for Python.
*   `cloudbuild.yaml`: Configured for Node.js/npm — needs update for Python.
