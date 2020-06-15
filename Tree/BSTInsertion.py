class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        itr = self.root
        if not itr: 
            self.root = Node(val)
            return self.root
        
        while itr:
            if itr.info > val: 
                if itr.left:
                    itr = itr.left
                else:
                    itr.left = Node(val)
                    break
            else: 
                if itr.right:
                    itr = itr.right
                else:
                    itr.right = Node(val)
                    break
        
        return self.root

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
