# AgentBot
Agentic-AI-Chatbot
Introduction
The Agentic AI Chatbot application allows users to interact with AI-powered agents using advanced LLMs. It integrates LangGraph, FastAPI, Streamlit, and Tavily Search for an interactive chatbot experience with optional web search capabilities.

Features
Select AI models from Groq (Llama-3.3, Mixtral-8x7b) or OpenAI (GPT-4o-mini).
Chat with AI agents using a user-friendly Streamlit interface.
You can enable web search functionality to gather more relevant responses.
The backend is built with FastAPI for scalability and efficiency.
Uses LangChain and LangGraph for intelligent agent interactions.
Architectural Diagram
Architectural Diagram

Figure: This diagram illustrates the architecture of our AI chatbot project.

Installation and Setup Guide
Using pipenv
Install pipenv (if not already installed):

 pip install pipenv
.env File
Create a .env file to store your private API keys for Groq, Tavily, and OpenAI.
Use this command to load environment variables: pipenv shell
Phase-1 (Create AI Agent)
Create an ai_agent.py file, and set up LLM Tools and AI Agent with Search Tool Functionality.
Install these Dependencies in phase-1 with pipenv:
 pipenv install langchain_groq
 pipenv install langchain_openai
 pipenv install langchain_community
pipenv install langgraph
Phase-2 (Setup Backend with FastAPI)
Create a backend.py file and set up the Pydantic Model (Schema Validation).
Setup AI Agnet from FrontEnd Request.
Run the App and explore Swaggers UI docs.
Install these Dependencies in phase-2 with pipenv:
 pipenv install pydantic
 pipenv install fastapi
 pipenv install uvicorn
Phase-3 (Setup FrontEnd)
Create a frontend.py file and set up UI with Streamlit.
Connect with the backend via URL.
Install this Dependency in phase-3 with pipenv:
 pipenv install streamlit
How to Run:
First load environment variables using: pipenv shell
Make sure the backend Python script is running in a separate terminal using the command: python backend.py
Then run the frontend file using the command: streamlit run frontend.py
Tools & Technologies
LangGraph ReAct Agents
FastAPI for API calls
Groq & Open AI for LLM
Streamlit for UI (FrontEnd)
LangChain for Tools
Uvicorn for hosting app
Python
VS Code
About
End to End AI Agent Chatbot with FastAPI, LangGraph, Langchain | Groq & OpenAI for LLM Model | Tavily for Search

Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 1 watching
Forks
 1 fork
Report repository
Releases
No releases published
Packages
No packages published
Languages
Python
100.0%
Footer
©
