#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfAlerts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER precedingMinutes
#  2. INTEGER alertThreshold
#  3. INTEGER_ARRAY numCalls
#

def numberOfAlerts(precedingMinutes, alertThreshold, numCalls):
    s = [0]*(len(numCalls)+1)
    result = 0
    for i in range(1, len(s)):
        s[i] = numCalls[i-1] + s[i-1]
    for i in range(len(numCalls)+1):
        if (s[i] - s[i-precedingMinutes])/precedingMinutes > alertThreshold:
            result +=1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    precedingMinutes = int(input().strip())

    alertThreshold = int(input().strip())

    numCalls_count = int(input().strip())

    numCalls = []

    for _ in range(numCalls_count):
        numCalls_item = int(input().strip())
        numCalls.append(numCalls_item)

    result = numberOfAlerts(precedingMinutes, alertThreshold, numCalls)

    fptr.write(str(result) + '\n')

    fptr.close()
