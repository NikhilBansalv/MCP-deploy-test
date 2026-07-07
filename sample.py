import inspect
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Test")

print(inspect.signature(mcp.streamable_http_app))