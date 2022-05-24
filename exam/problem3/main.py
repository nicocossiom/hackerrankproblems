#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER k
#
def pair_op(a, b, k):
    return a + k == b

def countPairs(numbers, k):
    right_ptr = 1
    left_ptr = result = 0
    numbers.sort()
    while right_ptr < len(numbers):
        value = numbers[right_ptr]-numbers[left_ptr]
        if value == k:
            left_ptr+=1
            right_ptr+=1
            result +=1
        elif value < k:
            right_ptr += 1
        else:
            left_ptr += 1
            if left_ptr == right_ptr:
                right_ptr +=1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    k = int(input().strip())

    result = countPairs(numbers, k)

    fptr.write(str(result) + '\n')

    fptr.close()
