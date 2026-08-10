# client.py
import asyncio
from fastmcp import Client

async def main():
    async with Client("weather.py") as client:
        
        print("====== 1. Check tools ======")
        tools = await client.list_tools()
        for tool in tools:
            print(f"Found: {tool.name} - {tool.description}")
            
        print("\n====== 2. Testing tools ======")
        # Testing on CA
        target_state = "CA"
        print(f"Checking {target_state}'s alerts...")
        
        result = await client.call_tool("get_alerts", {"state": target_state})
        
        print("\n[Results]:")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

