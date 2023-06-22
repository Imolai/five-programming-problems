#!/usr/bin/env python
"""Write a function that given a list of non negative integers,
arranges them such that they form the largest possible number. For
example, given [50, 2, 1, 9], the largest formed number is 95021."""
import unittest
from functools import cmp_to_key


def largest_number(nums):
    """Arrange a list of non negative integers to form the largest possible number."""
    nums = [str(num) for num in nums]

    # custom sorting: which order of numbers is greater?
    def compare(left, right):
        return int(right + left) - int(left + right)

    nums.sort(key=cmp_to_key(compare))

    largest_num = ''.join(nums)
    return int(largest_num)


class LargestNumberTestCase(unittest.TestCase):
    """Test largest number creation."""

    def test_largest_number(self):
        """Test largest_number function."""
        nums = [50, 2, 1, 9]
        result = largest_number(nums)
        self.assertEqual(result, 95021)

        nums = [5, 50, 56]
        result = largest_number(nums)
        self.assertEqual(result, 56550)

        nums = [420, 42, 423]
        result = largest_number(nums)
        self.assertEqual(result, 42423420)


if __name__ == '__main__':
    unittest.main(verbosity=2)
