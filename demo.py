import sys
import numpy as np
from app.mclaren import Palindrome

if __name__ == '__main__':   
 
    if len(sys.argv) == 2:
        plnd = Palindrome()
        plnd.getDistinct(sys.argv[1], 0)    
        if len(plnd.plength) > 2:
            maxindices = np.argsort(plnd.plength)[-3:]
            for i in reversed(maxindices):
                print 'Palindrome: {}'.format(plnd.palindromes[i])
                print 'Start Index: {}'.format(plnd.index[i])
                print 'Length of palindrome: {}'.format(plnd.plength[i])
        if len(plnd.plength) < 3:
            maxindices = np.argsort(plnd.plength)
            for i in reversed(maxindices):
                print 'Palindrome: {}'.format(plnd.palindromes[i])
                print 'Start Index: {}'.format(plnd.index[i])
                print 'Length of palindrome: {}'.format(plnd.plength[i])
    else:
        plnd = Palindrome()
        plnd.getDistinct('sqrrqabccbatudefggfedvwhijkllkjihxymnnmzpop', 0)
        if len(plnd.plength) > 2:
            maxindices = np.argsort(plnd.plength)[-3:]
            for i in reversed(maxindices):
                print 'Palindrome: {}'.format(plnd.palindromes[i])
                print 'Start Index: {}'.format(plnd.index[i])
                print 'Length of palindrome: {}'.format(plnd.plength[i])
