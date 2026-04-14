from __future__ import annotations

import json
from pathlib import Path

from agent.planner import build_plan
from agent.researcher import research_topic
from agent.summarizer import summarize_evidence
from agent.writer import write_article


ROOT_DIR = Path(__file__).resolve().parent.parent
TOPICS_PATH = ROOT_DIR / "data" / "topics" / "science-topics.json"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def pick_first_topic(topics):
    if not topics:
        return None
    return topics[0]


def print_section(title: str) -> None:
    print(f"\n{'=' * 12} {title} {'=' * 12}")


def print_json(data) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False))


def slugify(text: str) -> str:
    return text.lower().replace(" ", "-")


def save_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        file.write(content)


def save_json(path: Path, content) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(content, file, indent=2, ensure_ascii=False)


def main() -> None:
    print("\nHealth-Journal-Summarizer")
    print("Starter workflow is running...")

    if not TOPICS_PATH.exists():
        print(f"\nTopic file not found: {TOPICS_PATH}")
        return

    topics = load_json(TOPICS_PATH)
    topic = pick_first_topic(topics)

    if topic is None:
        print("\nNo topics found in science-topics.json")
        return

    plan = build_plan(topic)
    research_notes = research_topic(topic)
    summary = summarize_evidence(research_notes)
    article = write_article(summary)

    slug = slugify(topic.get("title", "untitled-topic"))

    plan_output_path = ROOT_DIR / "outputs" / "plans" / f"{slug}.json"
    research_output_path = ROOT_DIR / "outputs" / "research-notes" / f"{slug}.json"
    summary_output_path = ROOT_DIR / "outputs" / "summaries" / f"{slug}.json"
    draft_output_path = ROOT_DIR / "outputs" / "drafts" / f"{slug}.md"

    save_json(plan_output_path, plan)
    save_json(research_output_path, research_notes)
    save_json(summary_output_path, summary)
    save_text(draft_output_path, article["draft"])

    print_section("Selected Topic")
    print(topic.get("title", "Untitled topic"))

    print_section("Saved Files")
    print(f"Plan          : {plan_output_path}")
    print(f"Research Notes: {research_output_path}")
    print(f"Summary       : {summary_output_path}")
    print(f"Draft         : {draft_output_path}")

    print_section("Plan")
    print_json(plan)

    print_section("Research Notes")
    print_json(research_notes)

    print_section("Evidence Summary")
    print_json(summary)

    print_section("Article Draft")
    print(article["draft"])


if __name__ == "__main__":
    main()
