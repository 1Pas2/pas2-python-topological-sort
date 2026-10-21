import unittest
import pas2_topological_sort as api


class Tests(unittest.TestCase):
    def test_dependencies_first(self):
        order = api.sort_dependencies(
            {"app": ["db", "cache"], "db": [], "cache": ["db"]}
        )
        self.assertLess(order.index("db"), order.index("cache"))
        self.assertLess(order.index("cache"), order.index("app"))

    def test_implicit_and_duplicate(self):
        self.assertEqual(api.sort_dependencies({"a": ["b", "b"]}), ["b", "a"])

    def test_cycle_and_empty(self):
        self.assertEqual(api.sort_dependencies({}), [])
        with self.assertRaises(ValueError):
            api.sort_dependencies({"a": ["b"], "b": ["a"]})


if __name__ == "__main__":
    unittest.main()
