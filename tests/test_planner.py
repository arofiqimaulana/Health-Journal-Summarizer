from agent.planner import build_plan


def test_build_plan_returns_expected_structure():
    topic = {
        "title": "Manfaat jalan kaki setelah makan",
        "status": "idea",
        "priority": "high",
    }

    plan = build_plan(topic)

    assert plan["topic"] == "Manfaat jalan kaki setelah makan"
    assert "goal" in plan
    assert "steps" in plan
    assert isinstance(plan["steps"], list)
    assert len(plan["steps"]) > 0
    assert "success_criteria" in plan
