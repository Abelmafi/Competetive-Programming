#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    
    elivation = 0
    v_counter = 0
    for i in path:
        if elivation == 0:
            if i == 'D':
                v_counter += 1
                elivation -= 1
            else:
                elivation += 1
        else:
            if i == 'D':
                elivation -= 1
            else:
                elivation += 1
    return v_counter
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
