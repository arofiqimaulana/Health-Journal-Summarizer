from __future__ import annotations
import os
import json
from typing import Any
import google.generativeai as genai
from pydantic import BaseModel

api_key = os.environ.get("GEMINI_API_KEY")

class SummaryOutput(BaseModel):
    topic: str
    summary: str
    key_findings: list[str]
    evidence_strength: str
    limitations: list[str]
    caution_notes: list[str]

def summarize_evidence(research_notes: dict[str, Any]) -> dict[str, Any]:
    """Turn research notes into an evidence summary using Gemini AI."""
    topic = research_notes.get("topic", "Untitled topic")
    selected_sources = research_notes.get("selected_sources", [])
    search_queries = research_notes.get("search_queries", [])

    if not selected_sources:
        return {
            "topic": topic,
            "summary": f"No sources have been selected yet for the topic: {topic}.",
            "key_findings": [],
            "evidence_strength": "none",
            "source_count": 0,
            "source_overview": [],
            "limitations": ["No journal sources available."],
            "caution_notes": ["No evidence to summarize."],
            "open_questions": search_queries,
        }

    source_overview = []
    for source in selected_sources:
        source_overview.append({
            "title": source.get("title"),
            "study_type": source.get("study_type"),
            "year": source.get("year")
        })

    if not api_key:
        print("WARNING: GEMINI_API_KEY not found. Using naive fallback summary.")
        return {
            "topic": topic,
            "summary": "Fallback summary due to missing API key.",
            "key_findings": ["Needs AI for extraction."],
            "evidence_strength": "unknown",
            "source_count": len(selected_sources),
            "source_overview": source_overview,
            "limitations": ["API key missing."],
            "caution_notes": ["Fallback data only."],
            "open_questions": search_queries,
        }

    generation_config = genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema=SummaryOutput
    )
    model = genai.GenerativeModel("gemini-2.0-flash", generation_config=generation_config)
    
    sources_text = json.dumps(selected_sources, indent=2)
    prompt = f"""
    You are an AI Medical Summarizer. The topic is: "{topic}".
    Here are the PubMed sources retrieved:
    {sources_text}
    
    Please read the titles and study types to infer the overall evidence. Since we only have titles, do your best to summarize what the evidence likely points to, while remaining VERY CAUTIOUS.
    Provide your answer strictly following the JSON schema.
    Ensure that limitations and caution notes reflect the fact that we only read abstracts/titles.
    Output language: Indonesian.
    """
    
    print("Calling Gemini for Summarizer...")
    try:
        response = model.generate_content(prompt)
        result = json.loads(response.text)
        result["source_count"] = len(selected_sources)
        result["source_overview"] = source_overview
        result["open_questions"] = search_queries
        return result
    except Exception as e:
        print(f"Gemini API failed in summarizer: {e}")
        return {
            "topic": topic,
            "summary": "Failed to generate AI summary.",
            "key_findings": [],
            "evidence_strength": "unknown",
            "source_count": len(selected_sources),
            "source_overview": source_overview,
            "limitations": ["API failure"],
            "caution_notes": ["API failure"],
            "open_questions": search_queries,
        }
