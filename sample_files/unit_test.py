# test_example.py

import unittest
from bubble_sort import bubble_sort
from palindrome import is_palindrome


class TestSortingAndPalindrome(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(
            bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90]
        )
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("Hello"))


if __name__ == "__main__":
    unittest.main()


# python -m unittest test_example.py
