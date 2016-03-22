import sys
import numpy as np
#----------------------------------#
#Written By Mrinal Haloi-----------#
#-----------------------------------#
class Palindrome(object):
    def __init__(self, *args, **kwargs):
        self.palindromes = []
        self.index = []
        self.plength = []   

    def getLongestPalindrome(self, string):
        if not string.isalpha():
            raise ValueError
        maxLength = 1
        start = 0
        length = len(string)
        startidx = 0
        endidx = 0

        for i in xrange(1, length):
            startidx = i - 1
            endidx = i
            while startidx >= 0 and endidx < length and string[startidx] == string[endidx]:
                if endidx - startidx + 1 > maxLength:
                    start = startidx
                    maxLength = endidx - startidx + 1
                startidx -= 1
                endidx += 1
 
            startidx = i - 1
            endidx = i + 1
            while startidx >= 0 and endidx < length and string[startidx] == string[endidx]:
                if endidx - startidx + 1 > maxLength:
                    start = startidx
                    maxLength = endidx - startidx + 1
                startidx -= 1
                endidx += 1

        return start, maxLength, string[start:start + maxLength]

    def getDistinct(self, string, offset):
        #global palindromes, index, plength
        if len(string) == 1:
            return 1
        result = self.getLongestPalindrome(string)
        self.palindromes.append(string[result[0]:result[0] + result[1]])
        self.index.append(result[0]+offset)
        self.plength.append(result[1])
        if result[1] == len(string):
            return 1
        if not result[0] == 0:
            string1 = string[:result[0]]
            if len(string1) >1:
                self.getDistinct(string1, 0)
        if not result[0] == (len(string) - result[1]):
            string2 = string[result[0]+result[1]:]
            if len(string2) > 1:
                self.getDistinct(string2, result[0]+result[1] + offset)
