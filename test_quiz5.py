from unittest import TestCase
from quiz5 import is_sorted


class IsSortedTest(TestCase):
    def test_sorted_increasing(self):
        argument = is_sorted([1, 3, 6, 9])
        expected = True
        self.assertEqual(argument, expected)

    def test_sorted_decreasing(self):
        self.assertFalse(is_sorted([9, 5, 2]))

    def test_sorted_empty_list(self):
        self.assertTrue(is_sorted([]))

    def test_sorted_mixed(self):
        self.assertFalse(is_sorted([4, 6, 2, 9]))

    def test_sorted_zero(self):
        self.assertTrue(is_sorted([0, 0, 0]))
