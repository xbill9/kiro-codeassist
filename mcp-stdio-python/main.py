# main.py

import logging
import sys
import datetime
import platform
import os
import subprocess
from pythonjsonlogger.json import JsonFormatter
from mcp.server.fastmcp import FastMCP

# Set up logging to match index.ts behavior
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Set the root logger level

formatter = JsonFormatter()

# Handler for all levels to stderr
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setFormatter(formatter)
stderr_handler.setLevel(logging.INFO)  # Capture all levels from INFO up
logger.addHandler(stderr_handler)

# Initialize FastMCP server
mcp = FastMCP("hello-world-server")


@mcp.tool()
def greet(param: str) -> str:
    """
    Get a greeting from a local stdio server.
    """
    logger.debug("Executed greet tool")
    # FastMCP automatically wraps the return value in TextContent
    return param


@mcp.tool()
def get_system_time() -> str:
    """
    Get the current system time on the host machine.
    """
    logger.debug("Executed get_system_time tool")
    return datetime.datetime.now().isoformat()


@mcp.tool()
def get_system_info() -> str:
    """
    Get information about the host system including OS details,
    CPU count, and memory.
    """
    logger.debug("Executed get_system_info tool")
    info: dict[str, str | int | float | None] = {
        "OS": platform.system(),
        "OS Release": platform.release(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "CPU Count": os.cpu_count(),
    }

    # Try to extract total memory info across platforms
    if platform.system() == "Darwin":
        try:
            mem_bytes = int(
                subprocess.check_output(["sysctl", "-n", "hw.memsize"]).strip()
            )
            info["Total Memory (GB)"] = round(mem_bytes / (1024**3), 2)
        except Exception as e:
            logger.warning(f"Failed to get memory info on macOS: {e}")
    elif platform.system() == "Linux":
        try:
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    if line.startswith("MemTotal:"):
                        mem_kb = int(line.split()[1])
                        gb = round(mem_kb / (1024**2), 2)
                        info["Total Memory (GB)"] = gb
                        break
        except Exception as e:
            logger.warning(f"Failed to get memory info on Linux: {e}")
    elif platform.system() == "Windows":
        try:
            out = subprocess.check_output(
                ["wmic", "ComputerSystem", "get", "TotalPhysicalMemory"],
                text=True,
            )
            mem_bytes = int(out.strip().split("\n")[1].strip())
            info["Total Memory (GB)"] = round(mem_bytes / (1024**3), 2)
        except Exception as e:
            logger.warning(f"Failed to get memory info on Windows: {e}")

    return "\n".join(f"{key}: {val}" for key, val in info.items())


if __name__ == "__main__":
    # Explicitly use stdio transport
    mcp.run(transport="stdio")
