# python-mcp-server-basics

A minimal MCP server in Python: one tool and one resource over a folder of store policies, connected to Claude Code.

- A **tool** is a function Claude can call to do something. `find(word)` returns every line of the policies that
  contains a word, with the file it is in.
- A **resource** is data Claude can read, addressed by a URI. `policy://{name}` is the full text of one policy:
  `returns`, `price-match` or `warranty`.

The policies are plain text files in `docs/`. The whole server is `server.py`.

## Run it

You need [uv](https://docs.astral.sh/uv/) and Python 3.13 or later.

    uv sync
    uv run pytest

## Connect it to Claude Code

From this folder:

    claude mcp add store-policies -- uv run server.py

Then start `claude` here and ask, for example, "How many days do I have to return something?" Claude calls `find`,
reads the matching policy, and answers from it. `/mcp` shows the server, its tool and its resource.

## Where it comes from

The MCP chapter of the Python essentials for RAG video: https://joelstevick.com
