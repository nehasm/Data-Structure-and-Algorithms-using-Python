import os
import sys
import bisect


def runningMedian(a):
    l=[]
    result=[]
    for i in a:
        bisect.insort(l,i)
        if(len(l)%2==0):
            result.append((l[(len(l)//2)-1]+l[len(l)//2])/2)
        else:
            result.append(l[len(l)//2])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
