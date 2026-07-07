"""
Python MCP Client for the Internship Project.

This client connects to the MCP server, lists the available
tools, and demonstrates calling each tool with sample inputs.
"""

import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Server Configuration

server_params = StdioServerParameters(
    command="python",
    args=["server.py"]
)


async def execute_tool(session, title: str, tool_name: str, arguments: dict):
    """
    Helper function to execute an MCP tool and display its output.
    """
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    result = await session.call_tool(tool_name, arguments)

    print(result)


async def main():
    """
    Connect to the MCP server and demonstrate all available tools.
    """
    async with stdio_client(server_params) as streams:

        async with ClientSession(*streams) as session:

            await session.initialize()

            print("\nConnected to MCP Server Successfully!\n")

            tools = await session.list_tools()

            print("Available Tools:\n")

            for tool in tools.tools:
                print(f"• {tool.name}")

            await execute_tool(
                session,
                "1. Get All Users",
                "get_all_users",
                {}
            )

            await execute_tool(
                session,
                "2. Get User",
                "get_user",
                {
                    "user_id": 1
                }
            )

            await execute_tool(
                session,
                "3. Search User",
                "search_user",
                {
                    "name": "Nik"
                }
            )

            await execute_tool(
                session,
                "4. Get All Products",
                "get_all_products",
                {}
            )

            await execute_tool(
                session,
                "5. Get Product",
                "get_product",
                {
                    "product_id": 1
                }
            )

            await execute_tool(
                session,
                "6. Search Product",
                "search_product",
                {
                    "keyword": "Laptop"
                }
            )

            await execute_tool(
                session,
                "7. Get All Orders",
                "get_all_orders",
                {}
            )

            await execute_tool(
                session,
                "8. Add User",
                "add_user",
                {
                    "name": "Demo User",
                    "email": "demo@gmail.com"
                }
            )

            await execute_tool(
                session,
                "9. Remove User",
                "remove_user",
                {
                    "user_id": 21
                }
            )

            print("\nAll tool demonstrations completed successfully.")

if __name__ == "__main__":
    asyncio.run(main())