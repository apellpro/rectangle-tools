import unittest

# костыль который просто тут нужен (вероятно, из-за запуска тестов
# с помощью пакета unittest)
from sys import path
path.append('..')
try:
    from ..functions import intersection, union
except ImportError:
    from functions import intersection, union


class Testing(unittest.TestCase):

    def test_simple_intersection(self):
        self.assertEqual(intersection(2, 4, 5, 1, 3, 7, 6, 2), 4)
        self.assertEqual(union(2, 4, 5, 1, 3, 7, 6, 2), 20)
        self.assertEqual(intersection(-3, 1, 3, -1, -1, 3, 1, -3), 4)
        self.assertEqual(union(-4, 1, 4, -1, -1, 4, 1, -4), 28)

    def test_no_intersection(self):
        self.assertEqual(intersection(0, 2, 2, 0, 5, 2, 7, 0), 0)
        self.assertEqual(union(0, 2, 2, 0, 5, 2, 7, 0), 8)
        self.assertEqual(intersection(-1, 2, 0, 0, 0, 2, 1, 0), 0)
        self.assertEqual(union(-1, 2, 0, 0, 0, 2, 1, 0), 4)

    def test_one_in_one_intersection(self):
        self.assertEqual(intersection(0, 4, 4, 0, 1, 3, 3, 1), 4)
        self.assertEqual(union(0, 4, 4, 0, 1, 3, 3, 1), 16)
        self.assertEqual(intersection(0, 5, 5, 0, 0, 3, 3, 0), 9)
        self.assertEqual(union(0, 5, 5, 0, 0, 3, 3, 0), 25)

    def test_overlap(self):
        self.assertEqual(intersection(0, 100, 100, 0, 0, 100, 100, 0), 10000)
        self.assertEqual(union(0, 100, 100, 0, 0, 100, 100, 0), 10000)
