#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    l = len(s)
    i = 0
    j = l - 1
    while i < l:
        if s[i] != s[j]:
            break
        i += 1
        j -= 1
    if i > j: return -1
    a = i + 1
    b = j
    while a < j and b > i + 1:
        if s[a] != s[b]:
            return j
        a += 1
        b -= 1
    return i


    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()