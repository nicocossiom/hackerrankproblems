#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plus_minus(arr, n):
    neg, zero, pos = 0, 0, 0
    for item in arr:
        if item < 0: neg+=1
        if item == 0: zero+=1
        if item > 0: pos+=1
    print(pos/n)
    print(neg/n)
    print(zero/n)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr, n)
