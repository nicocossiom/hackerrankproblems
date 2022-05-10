#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    queue = list()
    for item in s:
        if item in "([{":
            queue.append(item)
        else:
            if len(queue) == 0:
                return "NO"
            corresponding = queue.pop()
            if corresponding == "[" and item != "]":
                return "NO"
            elif corresponding == "(" and item != ")":
                return "NO"
            elif corresponding == "{" and item != "}":
                return "NO"
    if len(queue) > 0: return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
