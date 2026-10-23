"""Example tests for StudySprint. Two small tests to copy from in Lesson 12."""
from features.reports import average_score

import unittest

from features import core


class TestCore(unittest.TestCase):
    def test_check_answer_is_case_insensitive(self):
        card = {"id": 1, "question": "Capital of France?", "answer": "Paris", "category": "geo"}
        self.assertTrue(core.check_answer(card, "paris"))
        self.assertFalse(core.check_answer(card, "London"))

    def test_add_card_gives_a_new_id(self):
        data = {"cards": [{"id": 1, "question": "q", "answer": "a", "category": "general"}]}
        card = core.add_card(data, "New question?", "yes")
        self.assertEqual(card["id"], 2)
        self.assertEqual(len(data["cards"]), 2)

    def test_average_score(self):
        data = {"history": [5, 6, 4]}
        self.assertEqual(average_score(data), 5.0)

    def test_average_score_true(self):
        data = {"history":[5, 6, 4]}
        self.assertTrue(average_score(data) == 5.0)

    def test_average_score_false(self):
        data ={"history": [5, 6, 4]}
        self.assertFalse(average_score(data) == 4.0)
if __name__ == "__main__":
    unittest.main()
