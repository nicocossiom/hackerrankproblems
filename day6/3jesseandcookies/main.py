#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, cookies):
    iters = 0
    while(not all(x >= k for x in cookies)) and len(cookies) != 1:
        cookies.sort()
        least = cookies.pop(0)
        sec_least = cookies.pop(0)
        cookies.append(least + 2*sec_least)
        iters += 1
    return iters if len(cookies) != 1 else -1




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
