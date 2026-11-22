"""A minimal MCP server: one tool and one resource over a folder of store policies.

A tool is a function Claude can call to do something; a resource is data Claude can read, addressed by a URI.
Run by Claude Code (see the README):  uv run server.py"""
from pathlib import Path

from mcp.server.mcpserver import MCPServer

DOCS = Path(__file__).resolve().parent / "docs"
mcp = MCPServer("store-policies")


@mcp.tool()
def find(word: str) -> list[str]:
    """Every line of the store policies that contains a word, with the file it is in."""
    return [f"{path.name}: {line.strip()}"
            for path in sorted(DOCS.glob("*.txt"))
            for line in path.read_text(encoding="utf-8").splitlines()
            if word.lower() in line.lower()]


@mcp.resource("policy://{name}")
def policy(name: str) -> str:
    """The full text of one store policy, by name: returns, price-match or warranty."""
    return (DOCS / f"{name}.txt").read_text(encoding="utf-8")


if __name__ == "__main__":
    mcp.run()
