#!/usr/bin/env python
"""Write three functions that compute the sum of the numbers in a given list
using a for-loop, a while-loop, and recursion."""
import unittest


def sum_for(nums):
    """Compute the sum of the numbers in a given list using a for-loop."""
    total = 0
    for num in nums:
        total += num
    return total


def sum_while(nums):
    """Compute the sum of the numbers in a given list using a while-loop."""
    total = 0
    index = 0
    while index < len(nums):
        total += nums[index]
        index += 1
    return total


def sum_sum(nums):
    """Compute the sum of the numbers in a given list using recursion."""
    if len(nums) == 0:
        return 0
    return nums[0] + sum_sum(nums[1:])


def sum_comprehension(nums):
    """Compute the sum of the numbers in a given list using a list comprehension (additional)."""
    total = 0
    return [total := total + num for num in nums][-1]


def sum_real(nums):
    """Compute the sum of the numbers in the real life."""
    return sum(nums)


class SumFunctionsTestCase(unittest.TestCase):
    """Test sum functions."""

    def test_sum_for(self):
        """Test for-looper sum."""
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(sum_for(numbers), 15)

    def test_sum_while(self):
        """Test while-looper sum."""
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(sum_while(numbers), 15)

    def test_sum_sum(self):
        """Test recursive sum."""
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(sum_sum(numbers), 15)

    def test_sum_comprehension(self):
        """Test sum with list comprehension."""
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(sum_comprehension(numbers), 15)

    def test_sum_real(self):
        """Test real sum."""
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(sum_sum(numbers), 15)


if __name__ == '__main__':
    unittest.main(verbosity=2)
