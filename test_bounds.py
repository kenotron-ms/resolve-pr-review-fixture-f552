import unittest

from bounds import clamp


class ClampTests(unittest.TestCase):
    def test_inside_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_below_lower(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_above_upper(self):
        self.assertEqual(clamp(42, 0, 10), 10)

    def test_lower_boundary(self):
        self.assertEqual(clamp(0, 0, 10), 0)

    def test_upper_boundary(self):
        self.assertEqual(clamp(10, 0, 10), 10)


if __name__ == "__main__":
    unittest.main()
