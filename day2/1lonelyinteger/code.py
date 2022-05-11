#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the '1simpletexteditor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a: list):
    times = dict()
    for elem in a:
        if elem not in times:
            times[elem] = 1
        else: times[elem]+=1
    return [k for k, v in times.items() if v==1][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    fptr.write(str(result) + '\n')
    fptr.close()
