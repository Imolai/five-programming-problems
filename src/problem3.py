#!/usr/bin/env python
"""Write a function that computes the list of the first 100 Fibonacci
numbers. By definition, the first two numbers in the Fibonacci
sequence are 0 and 1, and each subsequent number is the sum of the
previous two. As an example, here are the first 10 Fibonnaci
numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

OUTPUT
test_fibonacci (__main__.FibonacciFunctionsTestCase)
Test fibonacci. ... ok
test_first_n_fibonacci (__main__.FibonacciFunctionsTestCase)
Test first num Fibonacci numbers. ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""
import unittest


def fibonacci(num):
    """Return a list containing the Fibonacci series up to num."""

    fibonacci_nums = []
    this, after = 0, 1
    # generate Fibonacci numbers between zero and num
    while this < num:
        fibonacci_nums.append(this)
        this, after = after, this+after

    return fibonacci_nums

def first_n_fibonacci(num):
    """Return a list containing the first num Fibonacci numbers."""

    fibonacci_nums = []
    this, after = 0, 1
    # generate num pieces of Fibonacci numbers
    for _ in range(num):
        fibonacci_nums.append(this)
        this, after = after, this + after

    return fibonacci_nums[:num]


class FibonacciFunctionsTestCase(unittest.TestCase):
    """Test Fibonacci functions."""

    def test_fibonacci(self):
        """Test fibonacci."""
        result = fibonacci(50)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_first_n_fibonacci(self):
        """Test first num Fibonacci numbers."""
        result = first_n_fibonacci(100)
        self.assertEqual(len(result), 100)


if __name__ == '__main__':
    unittest.main(verbosity=2)
