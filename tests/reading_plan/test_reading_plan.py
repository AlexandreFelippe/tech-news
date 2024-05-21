from tech_news.analyzer.reading_plan import ReadingPlanService
from unittest.mock import Mock, patch
import pytest


fake_news = [
    {"title": "Notícia 1", "reading_time": 5},
    {"title": "Notícia 2", "reading_time": 8},
    {"title": "Notícia 3", "reading_time": 12},
    {"title": "Notícia 4", "reading_time": 3},
]

result = {
    "readable": [
        {"unfilled_time": 2, "chosen_news": [
            ("Notícia 1", 5), ("Notícia 4", 3)]},
        {"unfilled_time": 2, "chosen_news": [("Notícia 2", 8)]}
    ],
    "unreadable": [("Notícia 3", 12)]
}


def test_reading_plan_group_news():
    mock = Mock(return_value=fake_news)

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        mock
    ):
        assert ReadingPlanService.group_news_for_available_time(10) == result
        mock.assert_called_once()
