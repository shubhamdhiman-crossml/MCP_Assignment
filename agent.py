"""
Hospital AI Agent using LangChain, Google Gemini, and Model Context Protocol (MCP)

This module initializes an AI-powered hospital assistant that connects to an
MCP server to retrieve patient records and billing information. The agent
uses Google Gemini via LangChain as the language model and dynamically
invokes MCP tools to answer user queries.

Key Features:
- Connects to a local MCP server using MultiServerMCPClient (stdio transport)
- Wraps MCP tools for use with a LangChain agent
- Uses Google Gemini (gemini-2.5-flash) for natural language understanding
- Supports interactive command-line queries for hospital database access
- Asynchronous execution for non-blocking tool calls and model responses

Requirements:
- langchain
- langchain_google_genai
- langchain_mcp_adapters
- Valid Google API Key stored in cred.py
- Running MCP server (mcp_server.py)

"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient 
from prompt import system_prompt
from cred import GOOGLE_API_KEY

import asyncio

async def main():

    client = MultiServerMCPClient(  
            {
                "Hospitality": {
                    "transport": "stdio",  # Local subprocess communication
                    "command": "python",
                    # Absolute path to your math_server.py file
                    "args": ["C:/Users/ShubhamDhiman/Desktop/Hospital_Database/mcp_server.py"]
                }
                }
        )

    # -------------------- LLM --------------------


    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
    )


    # -------------------- MCP TOOL WRAPPERS --------------------


   
    tools = await client.get_tools()

   
    # -------------------- AGENT --------------------
    agent = create_agent(
    tools = tools,
    model=llm,
    system_prompt=system_prompt
    )


    # -------------------- RUN --------------------


    print("Hospital AI Agent Ready!\n")
    print (" Welcome to the Hospital Database ")

    while True:
        query = input(" Enter Your Query (Else Exit) : ")
        if query.lower() == "exit":
            break

        response =await agent.ainvoke({"messages":[{"role":"user", "content":query}]})
        print(response["messages"][-1].content)


if __name__== "__main__":
    asyncio.run(main())