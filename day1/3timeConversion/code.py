#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s :str):
    h, m, sec = s.split(":")
    time = sec[2:4]
    h = int(h)
    if time == "PM": 
        if h!= 12:
            h += 12
    else:
        if h==12:
            h -= 12

    return(f"{h:02d}:{m}:{sec[0:2]}")
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
