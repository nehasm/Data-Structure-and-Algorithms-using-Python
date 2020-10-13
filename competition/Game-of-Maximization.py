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
def checksum(arr):
    even=0
    odd=0
    for i in range(len(arr)):
        if (i+1)%2==0:
            even+=arr[i]
        else:
            odd+=arr[i]
    if even==odd:
        return [True,even,odd]
    else:
        return [False,even,odd]
def makearr(arr,even,odd):
    while even!=odd:
        if even>odd:
            return 
    
def maximumStones(arr):
    # Write your code here
    c = checksum(arr)
    if c[0]:
        return c[1]*2
    else:
        if c[1]>c[2]:
            return c[2]*2
        else:
            return c[1]*2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maximumStones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()