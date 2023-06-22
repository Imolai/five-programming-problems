#!/usr/bin/env python
"""Write a program to determine if the parentheses (), the brackets [], and the braces {}, in
a string are balanced.
For example:
{{)(}} is not balanced because ) comes before (
({)} is not balanced because ) is not balanced between {} and similarly the { is not
balanced between ()
[({})] is balanced
{}([]) is balanced
{()}[[{}]] is balanced."""
import unittest


def is_balanced(expression):
    """Check if the parentheses, brackets, and braces in a string are balanced."""
    stack = []
    opening = "({["
    closing = ")}]"

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            if opening.index(stack[-1]) == closing.index(char):
                stack.pop()
            else:
                return False

    return len(stack) == 0


class TestBalancedExpression(unittest.TestCase):
    """Tests for the is_balanced() function."""

    def test_balanced_expression(self):
        """Test a balanced expression."""
        expression = "{[()]}"
        self.assertTrue(is_balanced(expression))

    def test_unbalanced_expression(self):
        """Test an unbalanced expression."""
        expression = "{[()]}}"
        self.assertFalse(is_balanced(expression))

    def test_empty_expression(self):
        """Test an empty expression."""
        expression = ""
        self.assertTrue(is_balanced(expression))

    def test_expression_with_no_brackets(self):
        """Test an expression with no brackets."""
        expression = "abc"
        self.assertTrue(is_balanced(expression))

    def test_expression_with_only_opening_brackets(self):
        """Test an expression with only opening brackets."""
        expression = "{{{[("
        self.assertFalse(is_balanced(expression))

    def test_expression_with_only_closing_brackets(self):
        """Test an expression with only closing brackets."""
        expression = "}])}"
        self.assertFalse(is_balanced(expression))


if __name__ == '__main__':
    unittest.main(verbosity=2)
