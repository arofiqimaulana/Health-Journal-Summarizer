from __future__ import annotations

from typing import Any


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
    {
        "step": "Review outputs before publishing",
        "purpose": "Ensure safety, clarity, and accuracy before use.",
        "expected_output": "Human-reviewed final output",
    },
]


def build_plan(topic: dict[str, Any]) -> dict[str, Any]:
    """Create a starter plan for processing one topic.

    This planner is intentionally simple so beginners can see how planning fits into the
    workflow before adding more advanced orchestration.
    """
    title = topic.get("title", "Untitled topic")
    priority = topic.get("priority", "unknown")
    status = topic.get("status", "unspecified")

    return {
        "topic": title,
        "priority": priority,
        "status": status,
        "goal": f"Create a journal-based summary and Medium-style draft for: {title}",
        "steps": DEFAULT_PLAN_STEPS,
        "success_criteria": [
            "One topic is selected clearly.",
            "Research notes are prepared.",
            "Evidence summary mentions limitations.",
            "Article draft is created.",
            "Outputs are reviewed by a human before publishing.",
        ],
    }
