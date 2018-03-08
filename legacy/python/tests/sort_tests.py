'''
Created on Feb 13, 2015

@author: ccoe
'''
import unittest

from sort import selection_sort, insertion_sort, heap_sort


class Sort_Tests(unittest.TestCase):

    def test_selection_sort(self):
        structure = [5, 250, 3, 2, -11, 4, 10, 6]
        selection_sort(structure)

        print(structure)
        last_item = None
        for item in structure:
            if last_item:
                self.assertTrue(item > last_item)
            last_item = item

    def test_insertion_sort(self):
        structure = [5, 250, 3, 2, -11, 4, 10, 6]
        insertion_sort(structure)

        print(structure)
        last_item = None
        for item in structure:
            if last_item:
                self.assertTrue(item > last_item)
            last_item = item

    def test_heap_sort(self):
        structure = [5, 250, 3, 2, -11, 4, 10, 6]
        heap_sort(structure)

        print(structure)
        last_item = None
        for item in structure:
            if last_item:
                self.assertTrue(item > last_item)
            last_item = item


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_selection_sort']
    unittest.main()
