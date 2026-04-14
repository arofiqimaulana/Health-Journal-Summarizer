from __future__ import annotations

from typing import Any


def summarize_evidence(research_notes: dict[str, Any]) -> dict[str, Any]:
    """Turn research notes into a more realistic starter evidence summary.

    This version reads selected_sources and turns them into structured findings,
    limitations, and a cautious evidence overview.
    """
    topic = research_notes.get("topic", "Untitled topic")
    selected_sources = research_notes.get("selected_sources", [])
    recommended_study_types = research_notes.get("recommended_study_types", [])
    search_queries = research_notes.get("search_queries", [])

    if not selected_sources:
        return {
            "topic": topic,
            "summary": f"No sources have been selected yet for the topic: {topic}.",
            "key_findings": [],
            "evidence_strength": "not_assessed_yet",
            "source_count": 0,
            "source_overview": [],
            "limitations": [
                "No journal sources were available in research_notes.",
                "Evidence summary cannot be generated without source material.",
            ],
            "caution_notes": [
                "Do not publish content until real scientific sources are added.",
            ],
            "open_questions": search_queries,
        }

    source_overview = []
    key_findings = []
    limitations = []

    for source in selected_sources:
        source_title = source.get("title", "Untitled source")
        study_type = source.get("study_type", "unknown")
        year = source.get("year", "unknown")
        main_finding = source.get("main_finding", "No main finding recorded.")
        important_limitation = source.get("important_limitation", "No limitation recorded.")

        source_overview.append(
            {
                "title": source_title,
                "study_type": study_type,
                "year": year,
                "main_finding": main_finding,
            }
        )
        key_findings.append(main_finding)
        limitations.append(f"{source_title}: {important_limitation}")

    evidence_strength = "preliminary_placeholder"

    if any(source.get("study_type") == "systematic_review" for source in selected_sources):
        evidence_strength = "moderate_placeholder"

    summary_text = (
        f"This starter evidence summary for '{topic}' is based on {len(selected_sources)} "
        f"sample source(s). The current output is useful for workflow development, but all "
        f"sample sources must be replaced with real peer-reviewed literature before publication."
    )

    caution_notes = [
        "This summary currently uses sample journal-like sources for development purposes.",
        "Do not interpret placeholder findings as verified scientific conclusions.",
        "Replace all sample sources with real literature and review the evidence manually before publishing.",
    ]

    if "animal" in " ".join(key_findings).lower():
        caution_notes.append(
            "At least one finding may involve non-human evidence. Confirm study population before writing conclusions."
        )

    return {
        "topic": topic,
        "summary": summary_text,
        "key_findings": key_findings,
        "evidence_strength": evidence_strength,
        "source_count": len(selected_sources),
        "recommended_study_types": recommended_study_types,
        "source_overview": source_overview,
        "limitations": limitations,
        "caution_notes": caution_notes,
        "open_questions": search_queries,
    }
