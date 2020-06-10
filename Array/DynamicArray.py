import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastAns = 0
    anslist = []
    seqLists = [[] for i in range(n)]

    for i in range(len(queries)):
        q_type = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]

        if q_type == 1:
            seq = (x^lastAns) % n
            seqLists[seq].append(y)
        else:
            seq = (x^lastAns) % n
            size = len(seqLists[seq])
            index = y % size
            lastAns = seqLists[seq][index]
            anslist.append(lastAns)

    return anslist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
