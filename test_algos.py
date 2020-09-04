import unittest
from unittest.mock import patch
from io import StringIO
import super_algos


class TestFunctions(unittest.TestCase):

    def test_find_min(self):

        answer = super_algos.find_min([])
        self.assertEqual(answer,-1)
        answer = super_algos.find_min(['1'])
        self.assertEqual(answer,-1)
        answer = super_algos.find_min(['1','3','6'])
        self.assertEqual(answer,-1)
        answer = super_algos.find_min([2,3,7,8,'1'])
        self.assertEqual(answer,-1)
        answer = super_algos.find_min([4,3,8,4,9,2,5])
        self.assertEqual(answer, min([4,3,8,4,9,2,5]))

    def test_sum_all(self):

        answer = super_algos.sum_all([])
        self.assertEqual(answer,-1)
        answer = super_algos.sum_all(['1'])
        self.assertEqual(answer,-1)
        answer = super_algos.sum_all(['1','3','6'])
        self.assertEqual(answer,-1)
        answer = super_algos.sum_all([2,3,7,8,'1'])
        self.assertEqual(answer,-1)
        answer = super_algos.sum_all([4,3,8,4,9,2,5])
        self.assertEqual(answer, sum([4,3,8,4,9,2,5]))

    def test_find_possible_strings(self):
        
        combination = super_algos.find_possible_strings(['a','b',1],2)
        self.assertEqual(combination,[])
        combination = super_algos.find_possible_strings([1],2)
        self.assertEqual(combination,[])
        combination = super_algos.find_possible_strings(['a','b'],1)
        self.assertEqual(combination,['a','b'])
        combination = super_algos.find_possible_strings(['a','b'],2)
        self.assertEqual(combination,['aa','ab','ba','bb'])