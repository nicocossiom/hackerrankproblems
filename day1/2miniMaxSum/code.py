#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr:list):
    arr.sort()
    minimum = sum(arr[0:4])
    maximum = sum(arr[1:5])
    print(f"{minimum} {maximum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
