import os
from heapq import heapify,heappush,heappop
def minimumAverage(customers,starts,n):
    minheap=[]
    heapify(minheap)
    time=customers[0][0]
    result=0
    while customers!=[]:
        try:
            while customers[0][0]<=time:
                heappush(minheap,customers[0][1])
                customers.pop(0) 
        except IndexError:
            break     
        try:
            time+=heappop(minheap)
        except:               
            time=customers[0][0]
            continue
        result+=time
    while minheap!=[]:
        time+=heappop(minheap)
        result+=time
    return (result-starts)//n 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    customers = []
    starts=0
    for _ in range(n):
        temp=list(map(int, input().rstrip().split()))
        customers.append(temp)
        starts+=(temp[0])
    customers.sort(key = lambda x: x[0])
    result = minimumAverage(customers,starts,n)
    fptr.write(str(result) + '\n')
    fptr.close()
