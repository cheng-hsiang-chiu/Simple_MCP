# A simple MCP practice


## Prerequisites
```
mkdir mcp-weater-practice && cd mcp-weather-practice
uv add fastmcp httpx
uv tool install ollmcp
uv add langchain-ollama
```


## Test MCP Server with MCP client
```
uv run client.py
```

## Integrate with Ollama
```
ollmcp -j mcp-config.json
```

