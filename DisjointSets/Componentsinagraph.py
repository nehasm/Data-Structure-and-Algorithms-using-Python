import os
import sys

import os
import sys
sys.setrecursionlimit(100000)
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.comp=0
        self. visited=dict()
        self.V=[]
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.visited[u]=False
        self.visited[v]=False
        self.V.append(u)
    def DFSVis(self,v):
        self.visited[v]=True
        self.comp+=1
        for i in self.graph[v]:
            if self.visited[i]==False:
                self.DFSVis(i)
        
    def DFS(self,v):
        self.comp=0
        self.DFSVis(v)
        return self.comp
def componentsInGraph(gb):
    grap=Graph()
    cc=[]
    for i in gb:
        grap.addEdge(i[0],i[1])
    for j in grap.V:
        if grap.visited[j]==False:
            cc.append(grap.DFS(j))
    return [min(cc),max(cc)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
