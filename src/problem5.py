#!/usr/bin/env python
"""Write a program that outputs all possibilities to put + or - or
nothing between the numbers 1, 2, ..., 9 (in this order) such that
the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 =
100."""
import unittest
from itertools import product


def find_expressions():
    """Output all possibilities to put + or - or nothing between the numbers
    1, 2, ..., 9 (in this order) such that the result is always 100."""

    results, numbers = [], range(1, 10)
    # iterate on arrangements of operators
    for perm in product(['+', '-', ''], repeat=8):
        tuples = zip(numbers, perm + ('', ))  # add something for digit 9
        # create expression as string
        expression = ''.join([str(e1) + e2 for (e1, e2) in tuples])
        if eval(expression) == 100:
            results.append(expression)
    return results


class FindExpressionsTestCase(unittest.TestCase):
    """Test finding expressions."""

    def test_find_expressions(self):
        """Test find_expressions."""
        expected_results = ['1+2+3-4+5+6+78+9',
                            '1+2+34-5+67-8+9',
                            '1+23-4+5+6+78-9',
                            '1+23-4+56+7+8+9',
                            '12+3+4+5-6-7+89',
                            '12+3-4+5+67+8+9',
                            '12-3-4+5-6+7+89',
                            '123+4-5+67-89',
                            '123+45-67+8-9',
                            '123-4-5-6-7+8-9',
                            '123-45-67+89']

        result = find_expressions()
        self.assertEqual(result, expected_results)


if __name__ == '__main__':
    unittest.main(verbosity=2)
