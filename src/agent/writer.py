from __future__ import annotations
import os
import json
from typing import Any
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")

def write_article(summary: dict[str, Any]) -> dict[str, Any]:
    """Convert an evidence summary into a natural Medium-style article draft using Gemini AI."""
    topic = summary.get("topic", "Untitled topic")
    
    if not api_key:
        print("WARNING: GEMINI_API_KEY not found. Using naive fallback writer.")
        return {
            "topic": topic,
            "title": topic,
            "draft": "# Fallback Draft\n\nPlease add a Gemini API Key to generate real articles.",
            "status": "starter_article_draft",
        }

    model = genai.GenerativeModel("gemini-2.0-flash")
    summary_text = json.dumps(summary, indent=2, ensure_ascii=False)
    
    prompt = f"""
    You are an expert Health & Wellness writer writing for a platform like Medium.
    You have been provided with an AI-generated evidence summary on the topic: "{topic}".
    
    Evidence Summary:
    {summary_text}
    
    Task: Write an engaging, accessible, and cautious Medium-style article draft in Indonesian based ONLY on the evidence provided above.
    
    Requirements:
    - Include a catchy title.
    - Write an engaging introduction.
    - Discuss what the current scientific literature suggests based on the key findings.
    - Mention the evidence strength and the sources overview.
    - Explicitly state the limitations and provide caution notes to the reader so they don't treat this as medical advice.
    - Format the entire article in Markdown (`#`, `##`, `-`, `**`, etc.).
    - Do not invent medical facts. If the evidence is weak, say it's weak.
    """
    
    print("Calling Gemini for Writer...")
    try:
        response = model.generate_content(prompt)
        article = response.text
    except Exception as e:
        print(f"Gemini API failed in writer: {e}")
        article = f"# Error generating article for {topic}\n\n{e}"

    return {
        "topic": topic,
        "title": topic,
        "draft": article,
        "status": "ai_generated_article_draft",
    }
