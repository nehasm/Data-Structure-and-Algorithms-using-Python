#Min Heap
class BMin_Heap(object):
    def __init__(self):
        self.heap = [0]
        self.cur_size = 0

    # for shifting the node up
    def shiftUp(self, index):
        while (index // 2) > 0:
            if self.heap[index] < self.heap[index // 2]:     # (cur_size // 2) is the parent 
                temp = self.heap[index // 2]
                self.heap[index // 2] = self.heap[index]
                self.heap[index] = temp
            index = index // 2

    # to insert a node in the heap
    def insert(self, key):
        self.heap.append(key)
        self.cur_size += 1
        self.shiftUp(self.cur_size)

    # for shifting down a node
    def shiftDown(self, index):
        while(index * 2) <= self.cur_size:
            minimumChild = self.minChild(index)
            if self.heap[index] > self.heap[minimumChild]:
                temp = self.heap[index]
                self.heap[index] = self.heap[minimumChild]
                self.heap[minimumChild] = temp
            index = minimumChild
        
    # for finding the child with minimum value
    def minChild(self,i):
        if i * 2 + 1 > self.cur_size:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
        
    # for deleting a node from the heap and maintaining the heap property
    def delete(self):
        deletedNode = self.heap[1]
        self.heap[1] = self.heap[self.cur_size]
        self.cur_size -= 1
        self.heap.pop()
        self.shiftDown(1)
        return deletedNode
    
    # for building heap
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.cur_size = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.shiftDown(i)
            i = i - 1
                
bh = BMin_Heap()
bh.buildHeap([7,8,9,5,6,2,3,1])

print('Deleted:',bh.delete())
print('Deleted:',bh.delete())
print('Deleted:',bh.delete())
bh.insert(3)
print('Deleted:',bh.delete())