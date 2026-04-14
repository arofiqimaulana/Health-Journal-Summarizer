# Health-Journal-Summarizer

Health-Journal-Summarizer is a beginner-friendly agentic AI project for turning health topics into journal-based summaries and Medium-style article drafts.

This project is designed to help learners build a simple but structured workflow that goes from:

- topic selection
- research planning
- starter journal research notes
- evidence summarization
- article draft writing

The current version is intentionally simple. It focuses on workflow clarity, modular design, and safety-aware health content generation.

## Why This Project Exists

Many people want to learn from scientific health literature, but reading journals directly can feel slow, technical, and difficult to turn into public-friendly writing.

This project exists to help bridge that gap by creating a workflow that:

- starts from a health topic
- organizes journal-style research notes
- builds a cautious evidence summary
- turns the result into a readable draft for general audiences

It is also a learning project for understanding the basics of agentic AI.

## Current Features

- topic backlog stored in JSON
- modular agent structure
- planner, researcher, summarizer, and writer components
- structured outputs saved to files
- documentation for workflow, architecture, safety, prompts, and roadmap
- beginner-friendly codebase

## Project Workflow

The current workflow looks like this:

`Topic -> Planner -> Researcher -> Summarizer -> Writer -> Output Files`

For each selected topic, the system currently produces:

- a workflow plan
- research notes
- an evidence summary
- a draft article

## Project Structure

```txt
health-journal-summarizer/
├── README.md
├── docs/
├── src/
├── data/
├── outputs/
├── tests/
├── scripts/
└── config/
```

Important folders:

- `docs/` contains project documentation
- `src/` contains source code for the workflow
- `data/topics/` stores topic ideas
- `outputs/` stores generated files
- `config/` stores prompts and example settings

## Quick Start

### 1. Prepare topics

Add health topics to:

- `data/topics/science-topics.json`

Example:

```json
[
  {
    "title": "Manfaat jalan kaki setelah makan",
    "status": "idea",
    "priority": "high"
  }
]
```

### 2. Run the workflow

```bash
python src/main.py
```

### 3. Check outputs

Generated files are saved to:

- `outputs/plans/`
- `outputs/research-notes/`
- `outputs/summaries/`
- `outputs/drafts/`

## Documentation

Detailed documentation is available in the `docs/` folder:

- `docs/index.md`
- `docs/getting-started.md`
- `docs/workflow.md`
- `docs/architecture.md`
- `docs/prompts.md`
- `docs/safety.md`
- `docs/roadmap.md`

## Safety Note

This project works in the health domain, so caution matters.

The current system is designed for:

- educational use
- literature summarization
- workflow learning
- draft writing support

It is **not** designed for:

- medical diagnosis
- personalized treatment advice
- emergency triage
- replacing professional healthcare guidance

All outputs should be reviewed by a human before publication.

## Current Limitations

The current version still uses starter logic and placeholder research behavior.

That means:

- sample journal-like sources may still appear in the workflow
- evidence strength is not yet fully validated
- outputs are intended for development and learning
- real peer-reviewed source validation is still required before publishing

## Roadmap Direction

Near-term priorities include:

- improving research realism
- strengthening evidence summaries
- improving article writing quality
- adding tests
- making the workflow more robust

See `docs/roadmap.md` for more detail.

## Who This Is For

This project is especially suitable for:

- beginners learning agentic AI
- health content writers
- learners who like reading journal-based content
- builders who want a safe and structured AI writing workflow

## Final Note

This project is not trying to be a fully autonomous medical system.

Its goal is much more practical:

build a small, understandable, and safety-aware workflow for turning health topics into better structured learning and writing outputs.
