from __future__ import annotations

from typing import Any
import requests
import datetime


DEFAULT_STUDY_TYPES = [
    "systematic_review",
    "meta_analysis",
    "randomized_controlled_trial",
    "cohort_study",
]


SAMPLE_JOURNAL_SOURCES = [
    {
        "title": "Sample systematic review on physical activity and cardiometabolic health",
        "study_type": "systematic_review",
        "year": 2023,
        "main_finding": "Regular physical activity is associated with improved cardiometabolic markers in adults.",
        "important_limitation": "This is a placeholder source and should be replaced with a real journal article.",
        "source_link": "https://example.org/systematic-review-physical-activity",
    },
    {
        "title": "Sample randomized trial on walking after meals",
        "study_type": "randomized_controlled_trial",
        "year": 2022,
        "main_finding": "Short walks after meals may help improve short-term glucose control in some populations.",
        "important_limitation": "This is a placeholder trial and does not represent a verified source.",
        "source_link": "https://example.org/rct-walking-after-meals",
    },
    {
        "title": "Sample cohort study on sleep and appetite regulation",
        "study_type": "cohort_study",
        "year": 2021,
        "main_finding": "Poor sleep duration may be associated with changes in appetite regulation and eating patterns.",
        "important_limitation": "This is a placeholder cohort study for workflow development only.",
        "source_link": "https://example.org/cohort-sleep-appetite",
    },
]


def build_search_queries(title: str) -> list[str]:
    return [
        f"{title} systematic review",
        f"{title} meta analysis",
        f"{title} randomized controlled trial",
        f"{title} cohort study",
    ]


def select_sample_sources(title: str) -> list[dict[str, Any]]:
    lower_title = title.lower()

    if "jalan kaki" in lower_title or "walking" in lower_title:
        return SAMPLE_JOURNAL_SOURCES[:2]

    if "tidur" in lower_title or "sleep" in lower_title:
        return [SAMPLE_JOURNAL_SOURCES[2]]

    return SAMPLE_JOURNAL_SOURCES


def research_topic(topic: dict[str, Any]) -> dict[str, Any]:
    """Create structured starter research notes for a topic.

    This version is still beginner-friendly, but it is more realistic than a plain
    placeholder because it returns sample journal-style sources, search queries, and
    guidance for what should be validated later with real evidence.
    """
    title = topic.get("title", "Untitled topic")
    selected_sources = select_sample_sources(title)

    return {
        "topic": title,
        "status": "starter_research_notes",
        "recommended_study_types": DEFAULT_STUDY_TYPES,
        "search_queries": build_search_queries(title),
        "selected_sources": selected_sources,
        "research_notes": [
            "Replace all sample sources with real peer-reviewed journal articles before publishing.",
            "Prefer systematic reviews and meta-analyses when available.",
            "Record study design, population, main findings, and limitations for each source.",
            "Do not treat placeholder links as valid scientific references.",
        ],
        "next_action": "Validate and replace sample journal sources with real literature search results.",
    }
