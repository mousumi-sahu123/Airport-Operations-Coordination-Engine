import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.2)

def run_initial_agent_check():
    message = HumanMessage(content="Hello! Verify Gemini AI agent environment setup for Airport Operations Coordination Engine.")
    response = llm.invoke([message])
    return response.content

if __name__ == "__main__":
    print("Testing Gemini AI Agent Environment...")
    print("Agent Response:", run_initial_agent_check())