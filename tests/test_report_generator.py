from utils.report_generator import (
    generate_report,
    STRENGTH,
    WEAKNESS,
    WARNING
)


def test_strong_resume():

    scores = {
        "skills": 35,
        "sections": 20,
        "structure": 15,
        "technical_profile": 15,
        "readability": 10
    }

    report = generate_report(scores)

    assert len(report[STRENGTH]) == 5
    assert len(report[WEAKNESS]) == 0
    assert len(report[WARNING]) == 0


def test_weak_resume():

    scores = {
        "skills": 10,
        "sections": 5,
        "structure": 15,
        "technical_profile": 4,
        "readability": 10
    }

    report = generate_report(scores)

    assert len(report[STRENGTH]) == 2
    assert len(report[WEAKNESS]) == 3
    assert len(report[WARNING]) == 0


def test_warning_generation():

    scores = {
        "skills": 35,
        "sections": 20,
        "structure": 5,
        "technical_profile": 15,
        "readability": 4
    }

    report = generate_report(scores)

    assert len(report[WARNING]) == 2


def test_mixed_resume():

    scores = {
        "skills": 35,
        "sections": 8,
        "structure": 14,
        "technical_profile": 3,
        "readability": 4
    }

    report = generate_report(scores)

    assert len(report[STRENGTH]) == 2
    assert len(report[WEAKNESS]) == 2
    assert len(report[WARNING]) == 1


def test_report_item_structure():

    scores = {
        "skills": 35,
        "sections": 20,
        "structure": 15,
        "technical_profile": 15,
        "readability": 10
    }

    report = generate_report(scores)

    item = report[STRENGTH][0]

    assert "metric" in item
    assert "title" in item
    assert "severity" in item
    assert "score" in item
    assert "message" in item