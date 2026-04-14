from agent.researcher import research_topic


def test_research_topic_returns_starter_research_notes():
    topic = {
        "title": "Manfaat jalan kaki setelah makan",
        "status": "idea",
        "priority": "high",
    }

    research_notes = research_topic(topic)

    assert research_notes["topic"] == "Manfaat jalan kaki setelah makan"
    assert research_notes["status"] == "starter_research_notes"
    assert "search_queries" in research_notes
    assert isinstance(research_notes["search_queries"], list)
    assert "selected_sources" in research_notes
    assert isinstance(research_notes["selected_sources"], list)
    assert len(research_notes["selected_sources"]) > 0
