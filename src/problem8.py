#!/usr/bin/env python
"""Validate credit card number by Luhn algorithm.

0.) Given a Credit card number: 79927398713

1.) Starting from the rightmost digit, double the value of every second digit:
 7    9    9    2    7    3    9    8    7    1    3
      *2         *2         *2        *2        *2       
============================
       18.        4.         6.         16.        2


2.) If doubling of a number results in a two digit number i.e greater than 9
    (e.g., 6 × 2 = 12), then add the digits of the product (e.g.,
    12: 1 + 2 = 3, 15: 1 + 5 = 6), to get a single digit number.)

7    9    9    2    7    3    9    8    7    1    3
      *2         *2         *2        *2        *2       
============================
       18.        4.         6.         16.        2
============================
        9.         4.         6.         7.          2


3.) Now take the sum of all the digits.

7    9    9    2    7    3    9    8    7    1    3
      *2         *2         *2        *2        *2       
=============================
       18.        4.         6.         16.        2
=============================
        9.         4.         6.         7.          2
=============================
7.    9.   9.   4.   7.   6.   9.   7.    7.   2.   3.     =.    70

4.) If the total modulo 10 is equal to 0 (if the total ends in zero) then the
    number is valid according to the Luhn formula; else it is not valid.
"""

import unittest


def double_second(num: int) -> list[str]:
    """Double the value of every second digit, starting from the rightmost digit."""
    num_str = str(num)
    double_lst = []
    for i in range(len(num_str)-1, -1, -1):
        if i % 2 != 0:
            double_lst.insert(0, str(int(num_str[i]) * 2))
        else:
            double_lst.insert(0, num_str[i])
    return double_lst


def sum_str(nums_str: str) -> str:
    """Summarize a number given in a string."""
    total = 0
    for num_str in nums_str:
        total += int(num_str)
    return str(total)


def add_digits(num_str: str) -> list[str]:
    """Add the digits of the product, if doubling of a number results in a two digit number."""
    sum_lst = []
    for double_str in num_str:
        if len(double_str) > 1:
            sum_lst.append(sum_str(double_str))
        else:
            sum_lst.append(double_str)
    return sum_lst


class LuhnAlgorithmTestCase(unittest.TestCase):
    """Test Luhn algorithm application."""

    def test_double_second(self):
        """Does the second digit duplication work?"""
        num = 79927398713
        expected_result = ['7', '18', '9', '4',
                           '7', '6', '9', '16', '7', '2', '3']
        result = double_second(num)
        self.assertEqual(result, expected_result)

    def test_sum_str(self):
        """Does the sum generation work from a list of numbers in string format?"""
        nums_str = ['18', '4', '6', '16', '2']
        expected_result = '46'
        result = sum_str(nums_str)
        self.assertEqual(result, expected_result)

    def test_add_digits(self):
        """Can the function add the digits of the number if it has 2, or more digits?"""
        num_str = ['18', '4', '6', '16', '2']
        expected_result = ['9', '4', '6', '7', '2']
        result = add_digits(num_str)
        self.assertEqual(result, expected_result)

    def test_luhn_algorithm_valid(self):
        """Does the algorithm work by a valid number?"""
        card_number = 79927398713
        sum_of_list = int(
            sum_str(''.join(add_digits(double_second(card_number)))))
        result = sum_of_list % 10 == 0
        self.assertTrue(result)

    def test_luhn_algorithm_invalid(self):
        """Does the algorithm work by an invalid number?"""
        card_number = 79927398714
        sum_of_list = int(
            sum_str(''.join(add_digits(double_second(card_number)))))
        result = sum_of_list % 10 == 0
        self.assertFalse(result)


if __name__ == '__main__':
    # MANUAL TEST:
    # CARD_NUMBER = 79927398713
    # print(list(str(CARD_NUMBER)))
    # double_list = double_second(CARD_NUMBER)
    # print(double_list)
    # sum_list = add_digits(double_list)
    # print(sum_list)
    # sum_of_list = int(sum_str(''.join(sum_list)))
    # print(sum_of_list)
    # if sum_of_list % 10 == 0:
    #     print('Number is VALID')
    # else:
    #     print('Number is INvalid')
    unittest.main(verbosity=2)
