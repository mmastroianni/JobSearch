import unittest
from src.tree_map import TreeMap


class TestTreeMapExample(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_inorder_keys(self):
        theMap = TreeMap()
        theMap.insert(1,1)
        theMap.insert(2,2)
        theMap.insert(3,3)
        vals = theMap.get_inorder_keys()
        tvals = [1,2,3]
        self.assertEqual(vals, tvals)
