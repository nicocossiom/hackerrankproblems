#!/bin/python3

from ensurepip import version
import math
import os
import random
import re
import sys



#
# Complete the 'countSignals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY frequencies
#  2. 2D_INTEGER_ARRAY filterRanges
#

def countSignals(frequencies, filterRanges):
    overlap = [0, 100000000]
    for r in filterRanges:
        if r[0] > overlap[0]:
            overlap[0] = r[0]
        if r[1] < overlap[1]:
            overlap[1] = r[1]
    res = 0
    for fr in frequencies:
        if fr in range(overlap[0], overlap[1]+1):
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    frequencies_count = int(input().strip())
    frequencies = []
    if 

    for _ in range(frequencies_count):
        frequencies_item = int(input().strip())
        frequencies.append(frequencies_item)
    filterRanges_rows = int(input().strip())
    filterRanges_columns = int(input().strip())
    filterRanges = []
    for _ in range(filterRanges_rows):
        filterRanges.append(list(map(int, input().rstrip().split())))
    result = countSignals(frequencies, filterRanges)

    fptr.write(str(result) + '\n')

    fptr.close()
