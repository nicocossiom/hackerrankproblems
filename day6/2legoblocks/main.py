#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

MOD = 1000000007

def legoBlocks(n, m):
    row_combinations = [1, 1, 2, 4]
    while len(row_combinations) <= m:
        row_combinations.append(sum(row_combinations[-4:]) % MOD)
    total = [pow(c, n, MOD) for c in row_combinations]
    unstable = [0, 0]
    for i in range(2, m + 1):
        unstable.append(sum((total[j] - unstable[j]) * total[i - j] for j in range(1, i)) % MOD)
        # Print the number of stable wall combinations
    return((total[m] - unstable[m]) % MOD)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
