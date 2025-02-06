import unittest
from src.bin_search import binary_search


class TestBinsearch(unittest.TestCase):
    def test_binary_search(self):
        tlist = [1,2,3,4,5,6,7,8,9,10]

        val = binary_search(tlist, 42)
        self.assertEqual(val,-1)

        val = binary_search(tlist, 8)
        self.assertEqual(val, 7)
