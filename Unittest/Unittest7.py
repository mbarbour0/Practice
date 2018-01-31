import unittest

from string_fun import get_anagrams


class AnagramTestCase(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            get_anagrams('')

    def test_no_args(self):
        with self.assertRaises(ValueError):
            get_anagrams()
