import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    size = len(a)
    part1=[]
    part2=[]
    if size%2==0:
        for i in range(0,int(size/2)):
            part1.append(a[i])
        part1=part1[::-1]
        for i in range(int(size/2),size):
          part2.append(a[i])
        part2=part2[::-1]
        part2.extend(part1)
    else:
      for i in range(0,int(size/2)):
        part1.append(a[i])
      part1=part1[::-1]
      for i in range(int(size/2),size):
        part2.append(a[i])
      part2=part2[::-1]
      part2.extend(part1)
    return part2
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
