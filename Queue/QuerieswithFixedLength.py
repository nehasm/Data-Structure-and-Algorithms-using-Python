import os
import sys

# Complete the solve function below.
def solve(arr,queries):
    n=len(arr)
    result=[]
    for d in queries:
        M=0
        k=0
        for r in range(d):
            if arr[r]>M:
                M=arr[r]
                k=r        
        m=M
        s=1
        e=d
        while e<n:
            if s-1==k or arr[e]>M:
                M=arr[s]
                k=s
                for r in range(s+1,e+1):
                    if arr[r]>M:
                        M=arr[r]
                        k=r
                m=min(m,M)
            s+=1
            e+=1
        result.append(m)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
