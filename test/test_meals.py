from emoji_meals import mealify
import unittest

class TestRecipes(unittest.TestCase):

    def test_order_invariant(self):
        expected = "🍝"
        self.assertEqual(mealify("🌾🍅"), expected)
        self.assertEqual(mealify("🍅🌾"), expected)

    def test_multiple_args(self):
        expected = "🍝"
        self.assertEqual(mealify("🌾","🍅"), expected)
        self.assertEqual(mealify("🍅","🌾"), expected)

    def test_odd_grouping(self):
        expected = "🍕"
        self.assertEqual(mealify("🍞🍅", "🧀"), expected)
        self.assertEqual(mealify("🍞","🍅🧀"), expected)
        self.assertEqual(mealify("🍞","🧀🍅"), expected)

    def test_returns_none(self):
        self.assertIsNone(mealify(""))
        self.assertIsNone(mealify("🦝"))
        self.assertIsNone(mealify("RECIPE"))
