# weather.py
from typing import Any
import httpx
from fastmcp import FastMCP

mcp = FastMCP("US-Weather-Service")

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """ Sent requet to NWS API """
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }

    async with httpx.AsyncClient(verify=False, trust_env=False) as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"API request fails: {e}")
            return None

def format_alert(feature: dict) -> str:
    """ Format alert """
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No instruction provided')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """ 
    Get the weather alerts of certain state
  
    Args:
        state: Two-letters State in US (e.g.: CA, NY, TX)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state.upper().strip()}"
    data = await make_nws_request(url)
    
    if not data or "features" not in data:
        return f"❌ Fail to get {state}'s alert。"

    if not data["features"]:
        return f"✅ No {state}'s alert is available。"

    alerts = [format_alert(feature) for feature in data['features'][:3]]
    
    header_info = f"⚠️ Got {len(data['features'])} alerts，list top 3：\n"
    return header_info + "\n---\n".join(alerts)

if __name__ == "__main__":
    mcp.run()

