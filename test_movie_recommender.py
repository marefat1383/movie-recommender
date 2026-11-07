import unittest

from movie_recommender import recommend


class MovieRecommenderTests(unittest.TestCase):
    def test_space_query_returns_titles(self):
        results = recommend("space adventure")
        self.assertEqual(len(results), 3)
        self.assertIn("Galactic Voyage", results)

    def test_empty_query_is_rejected(self):
        with self.assertRaises(ValueError):
            recommend("   ")


if __name__ == "__main__":
    unittest.main()
