# A simple MCP practice


## Prerequisites
```
mkdir mcp-weater-practice && cd mcp-weather-practice
uv add fastmcp httpx
uv tool install ollmcp
uv add langchain-ollama
uv tool install mcp-cli
```


## Test MCP Server with MCP client
```
uv run client.py
```

## Option 1 : Integrate with Ollama
```
ollmcp -j mcp-config.json
```

## Option 2 : Integrate with MCP CLI 
```
export GROQ_API_KEY="Your GROQ API KEY"
mcp-cli --provider groq --model qwen/qwen3.6-27b --config-file mcp-config.json
```
