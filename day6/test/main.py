#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    tank = 0
    start = 0
    for (liters, km) in petrolpumps:
        tank += liters - km
        if (tank < 0):
            tank = 0
            start += 1
    return start

    tank += liters
    if tank >= km:
        tank-=km
        path.append(path[-1]+1)
        return truckTour(petrolpumps,path , tank)
    else:
        new_path = [path[0]+1]
        return truckTour(petrolpumps,new_path, 0)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
