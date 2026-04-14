from agent.summarizer import summarize_evidence

def test_summarize_evidence_uses_selected_sources():
    research_notes = {
        "topic": "Manfaat jalan kaki setelah makan",
        "recommended_study_types": ["systematic_review", "randomized_controlled_trial"],
        "search_queries": ["walking after meals systematic review"],
        "selected_sources": [
            {
                "title": "Sample walking after meals trial",
                "study_type": "randomized_controlled_trial",
                "year": 2022,
                "main_finding": "Short walks after meals may improve short-term glucose control.",
                "important_limitation": "Small sample size.",
                "source_link": "https://example.org/walking-trial",
            }
        ],
    }

    summary = summarize_evidence(research_notes)

    assert summary["topic"] == "Manfaat jalan kaki setelah makan"
    assert summary["source_count"] == 1
    assert "key_findings" in summary
    assert len(summary["key_findings"]) == 1
    assert "source_overview" in summary
    assert len(summary["source_overview"]) == 1
    assert "limitations" in summary
    assert len(summary["limitations"]) > 0
