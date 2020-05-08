from emoji_meals import mealify
import unittest

class TestRecipes(unittest.TestCase):

    def test_order_invariant(self):
        expected = "🍝"
        actual = mealify("🌾🍅")
        self.assertEqual(expected, actual)
        actual = mealify("🍅🌾")
        self.assertEqual(expected, actual)

    def test_returns_none(self):
        self.assertIsNone(mealify(""))
        self.assertIsNone(mealify("🦝"))
        self.assertIsNone(mealify("RECIPE"))
