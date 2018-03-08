'''
Created on Feb 13, 2015

@author: ccoe
'''
import unittest

from search import binary_search_iter, binary_search_recurs


class Search_Tests(unittest.TestCase):

    def test_binary_search_iter(self):
        structure = [1, 2, 3, 4, 5]
        item = 5
        result = binary_search_iter(structure, item)
        self.assertEqual(result, 4)

        structure = (1, 2, 3, 4, 5)
        item = 5
        result = binary_search_iter(structure, item)
        self.assertEqual(result, 4)

        structure = [1, 2, 3, 4, 5]
        item = 20
        result = binary_search_iter(structure, item)
        self.assertIsNone(result)

    def test_binary_search_recurs(self):
        structure = [1, 2, 3, 4, 5]
        item = 5
        result = binary_search_recurs(structure, item)
        self.assertEqual(result, 4)

        structure = (1, 2, 3, 4, 5)
        item = 5
        result = binary_search_recurs(structure, item)
        self.assertEqual(result, 4)

        structure = [1, 2, 3, 4, 5]
        item = 20
        result = binary_search_recurs(structure, item)
        self.assertIsNone(result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
