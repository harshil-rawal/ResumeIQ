from utils.ats import calculate_ats_score


def test_ats_initialization():
    statistics = {
        "total_skills": 0,
        "total_categories": 0,
        "category_names": [],
        "category_distribution": {},
        "largest_category": None,
        "smallest_category": None
    }

    result = calculate_ats_score("", {}, statistics)

    assert result["overall_score"] == 0
    assert "breakdown" in result
    assert "report" in result
    assert "strength" in result["report"]
    assert "weakness" in result["report"]
    assert "warning" in result["report"]