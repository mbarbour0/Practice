import unittest

from string_fun import get_anagrams


class AnagramTests(unittest.TestCase):
    def test_in_anagrams(self):
        self.assertIn('house', get_anagrams('treehouse'))

    def test_not_in_anagrams(self):
        self.assertNotIn('code', get_anagrams('treehouse'))
