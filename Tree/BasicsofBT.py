class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)

        return elements      

    def preorder_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()

        return elements 

    def find_max(self):
        if self.right is None:
            return self.data 
        return self.right.find_max() 

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum=self.left.calculate_sum() if self.left else 0
        right_sum=self.right.calculate_sum() if self.right else 0
        return left_sum + self.data + right_sum

    
def BuildTree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
if __name__=="__main__":
    colors=["black","brown","red","blue","yellow","orange"]
    color_tree=BuildTree(colors)
    print(color_tree.search("red"))
    number_tree=BuildTree([17, 4, 1, 20, 9, 23, 18, 34])
    print("Inordertraversal ",number_tree.inorder_traversal())
    print("PostOrder Traversal ",number_tree.postorder_traversal())
    print("PreOrder Traversal ",number_tree.preorder_traversal())
    print(number_tree.find_min())
    print(number_tree.find_max())
    print(number_tree.calculate_sum())