from decimal import Decimal
class DisjointSet:
    def __init__(self):
        self.parent=self
        self.size=1
    def findParent(self):
        if self.parent!=self:
            self.parent=self.parent.findParent()
        return self.parent
    def union(self,other):
        if self==other:
            return
        root=self.findParent()
        other_root=other.findParent()
        if root==other_root:
            return
        if root.size>other_root.size:
            other_root.parent=root
            root.size+=other_root.size
        else:
            root.parent=other_root
            other_root.size+=root.size
def nc2(n):
    if n<2:
        return 0
    return Decimal(n*(n-1)/2)
def nc3(n):
    if n<3:
        return 0
    return Decimal(n*(n-1)*(n-2)/6)

n=int(input())
components=[None]*n
for i in range(n-1):
    a,b,c=input().split()
    a=int(a)-1
    b=int(b)-1
    if c=='r':
        continue
    if not components[a]:
        components[a]=DisjointSet()
    if not components[b]:
        components[b]=DisjointSet()
    components[a].union(components[b])



uniqueComponents=set()
for x in components:
    if x:
        uniqueComponents.add(x.findParent())
valid_triplets=Decimal(nc3(n))

for x in uniqueComponents:
    valid_triplets-=nc3(x.size)
    valid_triplets-=nc2(x.size)*(n-x.size)
print(int(valid_triplets)%(10**9+7))