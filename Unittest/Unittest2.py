import unittest

class SimpleTestCase(unittest.TestCase):
    def test_simple(self):
        assert 10 - 10 == 0
