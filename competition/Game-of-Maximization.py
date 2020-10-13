#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumStones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def check(arr):
    e=0
    o=0
    for i in range(len(arr)):
        if (i+1)%2==0:
            e+=arr[i]
        else:
            o+=arr[i]
    if e==o:
        return [True,e,o]
    else:
        return [False,e,o]
    
def maximumStones(arr):
    a = check(arr)
    if a[0]:
        return a[1]*2
    else:
        if a[1]>a[2]:
            return a[2]*2
        else:
            return a[1]*2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maximumStones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()