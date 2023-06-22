#!/usr/bin/env python
"""Write a program to generate all potential anagrams of an input string.
For example, the potential anagrams of "biro" are
biro bior brio broi boir bori
ibro ibor irbo irob iobr iorb
rbio rboi ribo riob roib robi
obir obri oibr oirb orbi orib."""
import unittest


def anagrams(input_str):
    """Generate all potential anagrams of an input string."""
    result = [input_str]
    for swap_position in range(len(input_str)):
        result, partial_anagrams = [], result
        for partial in partial_anagrams:
            for i, char in enumerate(partial[swap_position:], swap_position):
                result.append(partial[:swap_position] + char +
                              partial[swap_position:i] + partial[i+1:])
    return result


class TestAnagramGenerator(unittest.TestCase):
    """Tests for the anagrams() function."""

    def test_anagrams(self):
        """Test generating anagrams for a string."""
        input_str = "biro"
        expected_anagrams = [
            'biro', 'bior', 'brio', 'broi', 'boir', 'bori',
            'ibro', 'ibor', 'irbo', 'irob', 'iobr', 'iorb',
            'rbio', 'rboi', 'ribo', 'riob', 'roib', 'robi',
            'obir', 'obri', 'oibr', 'oirb', 'orbi', 'orib'
        ]
        result = anagrams(input_str)
        self.assertCountEqual(result, expected_anagrams)

    def test_anagrams_empty_string(self):
        """Test generating anagrams for an empty string."""
        input_str = ""
        expected_anagrams = [""]
        result = anagrams(input_str)
        self.assertEqual(result, expected_anagrams)

    def test_anagrams_single_character(self):
        """Test generating anagrams for a single character."""
        input_str = "a"
        expected_anagrams = ["a"]
        result = anagrams(input_str)
        self.assertEqual(result, expected_anagrams)


if __name__ == '__main__':
    unittest.main(verbosity=2)
