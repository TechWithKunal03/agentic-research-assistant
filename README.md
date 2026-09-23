# agentic-research-assistant
Multi-agent AI research assistant using LangGraph, RAG, vector search, and LLMs for evidence-backed research.
# 🤖 Agentic AI Research Assistant

A multi-agent AI research assistant that autonomously
plans research tasks, gathers information, analyzes
evidence, performs critical review, and generates a
structured final response.

## 🚀 Features

- Multi-agent research workflow
- Autonomous research planning
- Web-based information retrieval
- LLM-powered analysis
- Critic agent for hallucination checking
- Final answer synthesis
- Interactive Streamlit interface

## 🧠 Agent Architecture

User Query
    ↓
Planner Agent
    ↓
Researcher Agent
    ↓
Analyst Agent
    ↓
Critic Agent
    ↓
Synthesis Agent
    ↓
Final Answer

## 🛠️ Tech Stack

- Python
- OpenAI API
- Streamlit
- FAISS
- Sentence Transformers
- BeautifulSoup
- Requests

## 📂 Project Structure

```text
agentic-research-assistant/
│
├── app.py
├── agents.py
├── rag.py
├── tools.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md
