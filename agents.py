from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    MODEL_NAME
)

from tools import search_web


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def ask_llm(prompt: str) -> str:

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


# -------------------------
# Planner Agent
# -------------------------

def planner_agent(query):

    prompt = f"""
You are a research planning agent.

Break the following research question
into 3-5 smaller research tasks.

Research question:
{query}

Return only the research tasks.
"""

    return ask_llm(prompt)


# -------------------------
# Researcher Agent
# -------------------------

def researcher_agent(query):

    search_results = search_web(query)

    prompt = f"""
You are a research agent.

Research question:
{query}

Search results:
{search_results}

Extract the most useful factual information
from these results.

Clearly separate facts from uncertain claims.
"""

    return ask_llm(prompt)


# -------------------------
# Analyst Agent
# -------------------------

def analyst_agent(query, research):

    prompt = f"""
You are an analytical research agent.

Question:
{query}

Research collected:
{research}

Analyze the information.

Identify:
1. Important findings
2. Supporting evidence
3. Contradictions
4. Missing information
5. Key conclusions

Do not invent facts.
"""

    return ask_llm(prompt)


# -------------------------
# Critic Agent
# -------------------------

def critic_agent(query, analysis):

    prompt = f"""
You are a critical reviewer.

Research question:
{query}

Analysis:
{analysis}

Check the analysis for:

- Unsupported claims
- Logical errors
- Missing evidence
- Contradictions
- Possible hallucinations

Return:
1. Problems found
2. Corrections
3. Whether the analysis is reliable
"""

    return ask_llm(prompt)


# -------------------------
# Final Synthesis Agent
# -------------------------

def synthesis_agent(
    query,
    research,
    analysis,
    critique
):

    prompt = f"""
You are the final research synthesis agent.

Research question:
{query}

Research:
{research}

Analysis:
{analysis}

Critic review:
{critique}

Create a clear, structured final answer.

Requirements:

- Answer the original question directly.
- Use only supported information.
- Do not invent facts.
- Mention uncertainty where appropriate.
- Use headings and bullet points.
"""

    return ask_llm(prompt)


# -------------------------
# Complete Agentic Workflow
# -------------------------

def run_research(query):

    plan = planner_agent(query)

    research = researcher_agent(
        query
    )

    analysis = analyst_agent(
        query,
        research
    )

    critique = critic_agent(
        query,
        analysis
    )

    final_answer = synthesis_agent(
        query,
        research,
        analysis,
        critique
    )

    return {
        "plan": plan,
        "research": research,
        "analysis": analysis,
        "critique": critique,
        "final_answer": final_answer
    }
