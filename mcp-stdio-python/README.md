# MCP Stdio Python Server

A simple Model Context Protocol (MCP) server implemented in Python using `FastMCP`. This server is designed to communicate over `stdio` and serves as a foundational "Hello World" example for Python-based MCP integrations.

## Overview

This project provides a basic MCP server named `hello-world-server` that exposes several tools for greeting, system introspection, and CLI version checking. It uses `python-json-logger` for structured logging to stderr, ensuring that the stdout stream remains clean for the MCP protocol JSON-RPC messages.

## Prerequisites

- **Python 3.10+**
- `pip` (Python Package Installer)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd mcp-stdio-python
    ```

2.  **Install dependencies:**
    ```bash
    make install
    # Or manually:
    python3 -m pip install --break-system-packages -r requirements.txt
    python3 -m pip install --break-system-packages -r requirements-dev.txt
    ```

## Usage

This server is designed to be executed by an MCP client (like Claude Desktop or a Kiro CLI extension) that handles the stdio communication.

To run the server manually (starts listening on stdio):
```bash
python3 main.py
```

### Configuration for MCP Clients

```json
{
  "mcpServers": {
    "python-hello-world": {
      "command": "python3",
      "args": ["/path/to/mcp-stdio-python/main.py"]
    }
  }
}
```

*Note: Ensure the absolute path is correct and that the python command resolves to the environment where dependencies are installed.*

## Tools

### `greet`
- **Description:** Get a greeting from the local server.
- **Parameters:** `param` (string) — text or name to echo back.
- **Returns:** The string passed in `param`.

### `get_system_time`
- **Description:** Get the current system time on the host machine.
- **Returns:** ISO 8601 timestamp string.

### `get_system_info`
- **Description:** Get information about the host system including OS details, CPU count, and memory.
- **Returns:** Multiline string with OS, architecture, CPU count, and total memory (GB).

### `get_aws_cli_version`
- **Description:** Get the installed AWS CLI version.
- **Returns:** Version string, or an error message if AWS CLI is not installed.

### `get_kiro_cli_version`
- **Description:** Get the installed Kiro CLI version.
- **Returns:** Version string, or an error message if Kiro CLI is not installed.

## Development

The project includes a `Makefile` to simplify common development tasks.

| Command          | Description                        |
|------------------|------------------------------------|
| `make install`   | Install all dependencies           |
| `make run`       | Run the server                     |
| `make test`      | Run tests                          |
| `make lint`      | Lint code with `flake8`            |
| `make format`    | Format code with `black`           |
| `make type-check`| Type-check with `mypy`             |
| `make all`       | Install, test, lint, and type-check|
| `make clean`     | Remove compiled/temporary files    |

## Project Structure

- `main.py` — Entry point; defines the MCP server and all tools.
- `requirements.txt` — Runtime dependencies (`mcp`, `pydantic`, `python-json-logger`).
- `requirements-dev.txt` — Dev dependencies (`pytest`, `flake8`, `black`, `mypy`).
- `Makefile` — Commands for build, test, and maintenance.
- `test_logging.py` — Unit tests for logging behavior.
- `test_greet.py` — Unit tests for the `greet` tool.
