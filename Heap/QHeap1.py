import heapq
n=int(input())
a=[]
for i in range(n):
    s=list(map(int,input().split(' ')))
    if(s[0]==1):
        heapq.heappush(a,s[1])
    elif(s[0]==2):
        if(a[0]==s[1]):
            a.remove(s[1])
            heapq.heapify(a)
        else:
            a.remove(s[1])
    else:
        print(a[0])