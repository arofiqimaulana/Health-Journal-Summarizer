# Documentation Index

Welcome to the documentation for **Health-Journal-Summarizer**.

This project is a beginner-friendly agentic AI workflow for turning health topics into journal-based summaries and Medium-style article drafts.

The documentation in this folder is designed to help you understand the project from multiple angles: what it does, how it works, how it is structured, and what safety rules guide it.

## Documentation Overview

Use the following documents as your main guide:

- `getting-started.md`  
  A practical introduction to running the project for the first time.

- `workflow.md`  
  Explains the end-to-end workflow, from topic selection to article draft generation.

- `architecture.md`  
  Describes the main components of the system, including planner, researcher, summarizer, and writer.

- `prompts.md`  
  Documents the prompt design used by the agent components.

- `safety.md`  
  Explains the safety boundaries and health-content precautions used in the project.

- `roadmap.md`  
  Describes the staged development direction of the project.

## Suggested Reading Order

If you are new to the project, this reading order is recommended:

1. `../README.md`
2. `getting-started.md`
3. `workflow.md`
4. `architecture.md`
5. `safety.md`
6. `prompts.md`
7. `roadmap.md`

## What This Project Tries to Do

Health-Journal-Summarizer is designed to help with a structured workflow that:

- starts from a health topic
- organizes research notes
- creates a cautious evidence summary
- turns the result into a draft article for general readers

The project is also meant as a learning tool for understanding agentic AI in a practical and manageable way.

## What This Project Does Not Try to Do

This project is not intended to:

- diagnose health conditions
- replace medical professionals
- provide personalized treatment advice
- publish medical claims without review

Its role is educational and workflow-oriented, not clinical.

## Current State

At the current stage, the project already includes:

- core documentation
- a starter workflow in `src/main.py`
- planner, researcher, summarizer, and writer modules
- saved outputs for plans, research notes, summaries, and article drafts

The project is still in an early development stage, so some parts remain intentionally simple and beginner-friendly.

## Where to Start in the Code

If you want to explore the code, start here:

- `src/main.py`

Then continue to:

- `src/agent/planner.py`
- `src/agent/researcher.py`
- `src/agent/summarizer.py`
- `src/agent/writer.py`

## Final Note

This documentation is meant to grow with the project.

As the workflow becomes more capable, the docs should continue to reflect the real structure, real limitations, and real goals of the system.
