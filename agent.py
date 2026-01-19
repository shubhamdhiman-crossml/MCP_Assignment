import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient 
from prompt import system_prompt

import asyncio

load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
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
    model="gemini-2.5-flash-lite",
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