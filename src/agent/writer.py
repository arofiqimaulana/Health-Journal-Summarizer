from __future__ import annotations

from typing import Any


def format_bullets(items: list[str]) -> str:
    if not items:
        return "- No items available yet."
    return "\n".join(f"- {item}" for item in items)


def format_source_overview(source_overview: list[dict[str, Any]]) -> str:
    if not source_overview:
        return "- No source overview is available yet."

    lines = []
    for source in source_overview:
        title = source.get("title", "Untitled source")
        study_type = source.get("study_type", "unknown")
        year = source.get("year", "unknown")
        main_finding = source.get("main_finding", "No main finding recorded.")
        lines.append(f"- {title} ({study_type}, {year}): {main_finding}")
    return "\n".join(lines)


def write_article(summary: dict[str, Any]) -> dict[str, Any]:
    """Convert an evidence summary into a more natural starter Medium-style article draft."""
    topic = summary.get("topic", "Untitled topic")
    key_findings = summary.get("key_findings", [])
    limitations = summary.get("limitations", [])
    caution_notes = summary.get("caution_notes", [])
    source_overview = summary.get("source_overview", [])
    source_count = summary.get("source_count", 0)
    evidence_strength = summary.get("evidence_strength", "not_assessed_yet")

    findings_text = format_bullets(key_findings)
    limitations_text = format_bullets(limitations)
    caution_text = format_bullets(caution_notes)
    sources_text = format_source_overview(source_overview)

    article = f"""# {topic}

## Introduction
This draft explores the topic of **{topic}** using a starter evidence-summary workflow. At this stage, the article is based on {source_count} structured source entry or entries collected during the research step.

## What the Current Sources Suggest
Here are the main findings gathered so far:
{findings_text}

## Source Overview
The current evidence base in this draft includes:
{sources_text}

## How Strong Is the Evidence?
At the moment, the evidence strength is labeled as: **{evidence_strength}**.

This label is still part of a development-stage workflow, so it should not be treated as a final scientific judgment. It is mainly here to help structure the writing and remind the reviewer to verify the real quality of the supporting studies.

## Important Limitations
A careful summary should always include its limitations:
{limitations_text}

## Caution Notes
Before turning this into a publishable article, keep these notes in mind:
{caution_text}

## Closing Note
This draft is meant for educational and workflow development purposes. It is not medical advice, diagnosis, or treatment guidance. Before publication, all placeholder evidence should be replaced with real peer-reviewed journal sources and reviewed manually.
"""

    return {
        "topic": topic,
        "title": topic,
        "draft": article,
        "status": "starter_article_draft",
    }
