from __future__ import annotations
import os
import json
from typing import Any
import google.generativeai as genai
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

class PlanStep(BaseModel):
    step: str
    purpose: str
    expected_output: str

class PlanOutput(BaseModel):
    topic: str
    priority: str
    status: str
    goal: str
    english_search_queries: list[str] = Field(description="List of 2-3 PubMed search queries in English. Very important to translate Indonesian topic to English medical terms.")
    steps: list[PlanStep]
    success_criteria: list[str]


DEFAULT_PLAN_STEPS = [
    {
        "step": "Select one health topic from the backlog",
        "purpose": "Choose a clear topic that will be processed in the workflow.",
        "expected_output": "A single selected topic",
    },
    {
        "step": "Search for relevant scientific journal sources",
        "purpose": "Prepare research material from reliable evidence.",
        "expected_output": "Starter research notes and candidate sources",
    },
    {
        "step": "Summarize the evidence carefully",
        "purpose": "Turn research notes into an evidence-based summary.",
        "expected_output": "Evidence summary with limitations and caution notes",
    },
    {
        "step": "Write a Medium-style draft",
        "purpose": "Convert the summary into a readable public-facing article draft.",
        "expected_output": "Starter article draft",
    },
]


def build_plan(topic: dict[str, Any]) -> dict[str, Any]:
    """Create a plan dynamically using Gemini AI."""
    title = topic.get("title", "Untitled topic")
    priority = topic.get("priority", "unknown")
    status = topic.get("status", "unspecified")

    if not api_key:
        print("WARNING: GEMINI_API_KEY not found. Using naive fallback plan.")
        return {
            "topic": title,
            "priority": priority,
            "status": status,
            "goal": f"Create a journal-based summary and Medium-style draft for: {title}",
            "english_search_queries": [title], # Not ideal, but fallback
            "steps": DEFAULT_PLAN_STEPS,
            "success_criteria": ["Finish process"],
        }
    
    generation_config = genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema=PlanOutput
    )
    model = genai.GenerativeModel("gemini-2.0-flash", generation_config=generation_config)
    
    prompt = f"""
    You are an AI Health Workflow Planner. We have a research topic: "{title}".
    Priority: {priority}.
    
    Your task is to plan the research workflow. 
    Critically: The topic is usually in Indonesian, but PubMed search MUST be in English.
    Please provide 2-3 precise english search queries (e.g. "hypertension physical exercise clinical trial") in the `english_search_queries` field.
    Fill out the rest of the JSON schema with logical workflow steps and success criteria.
    """
    
    print("Calling Gemini for Planner...")
    try:
        response = model.generate_content(prompt)
        # Parse JSON
        result = json.loads(response.text)
        return result
    except Exception as e:
        print(f"Gemini API failed: {e}")
        return {
            "topic": title,
            "priority": priority,
            "status": status,
            "goal": "Fallback plan due to API error",
            "english_search_queries": [title],
            "steps": DEFAULT_PLAN_STEPS,
            "success_criteria": [],
        }
