#!/usr/bin/env python
"""Write a function that combines two lists by alternatingly taking
elements. For example: given the two lists `[a, b, c]` and
`[1, 2, 3]`, the function should return `[a, 1, b, 2, c, 3]`."""
import unittest


def combine_lists_basic(list1, list2):
    """Combine two lists by alternatingly taking elements."""
    combined = []
    # we can mix them until the shortest lasts
    min_len = min(len(list1), len(list2))

    for i in range(min_len):
        combined.append(list1[i])
        combined.append(list2[i])

    # after mixing, we can add the rest
    if len(list1) > min_len:
        combined.extend(list1[min_len:])
    elif len(list2) > min_len:
        combined.extend(list2[min_len:])

    return combined


def combine_lists_zip(list1, list2):
    """Combine two lists by zipping elements."""
    combined = []
    for item1, item2 in zip(list1, list2):
        combined.extend([item1, item2])

    if len(list1) > len(list2):
        combined.extend(list1[len(list2):])
    elif len(list2) > len(list1):
        combined.extend(list2[len(list1):])

    return combined


class CombineFunctionsTestCase(unittest.TestCase):
    """Test combine functions."""

    def test_combine_lists_basic(self):
        """Test basic combine."""
        list1 = ['a', 'b', 'c']
        list2 = [1, 2, 3]
        self.assertEqual(combine_lists_basic(
            list1, list2), ['a', 1, 'b', 2, 'c', 3])

    def test_combine_lists_zip(self):
        """Test zipper combine."""
        list1 = ['a', 'b', 'c']
        list2 = [1, 2, 3]
        self.assertEqual(combine_lists_zip(list1, list2),
                         ['a', 1, 'b', 2, 'c', 3])


if __name__ == '__main__':
    unittest.main(verbosity=2)
