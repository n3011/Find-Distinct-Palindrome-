import unittest
from app.palindrome import Palindrome
import numpy as np


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.plnd = Palindrome()

    def test_Longest_palindrome(self):
        result = self.plnd.getLongestPalindrome('sqrrqabccbatudefggfedvwhijkllkjihxymnnmzpop')
        self.assertEqual(result[2], 'hijkllkjih')
    def test_distinct_palindrome(self):
        self.plnd.getDistinct('sqrrqabccbatudefggfedvwhijkllkjihxymnnmzpop', 0)
        maxindices = np.argsort(self.plnd.plength)[-3:] 
        self.assertEqual(self.plnd.palindromes[maxindices[0]], 'abccba')
        self.assertEqual(self.plnd.palindromes[maxindices[1]], 'defggfed')
        self.assertEqual(self.plnd.palindromes[maxindices[2]], 'hijkllkjih')
    def test_string_input(self):
        self.assertRaises(ValueError, self.plnd.getLongestPalindrome, '27sgyrk')
