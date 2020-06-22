import os
import sys
import heapq

def cookies(k, A):
    heapq.heapify(A)
    count=0
    try:
       while A[0]<k:
           least=heapq.heappop(A)           
           secondleast=heapq.heappop(A)
           sweetness=(1*least)+(2*secondleast)
           heapq.heappush(A,sweetness)
           count+=1
       return count
    except:
        return -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
