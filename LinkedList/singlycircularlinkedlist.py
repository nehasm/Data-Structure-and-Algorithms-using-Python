class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class CircularLinkedlist:
    def __init__(self):
        self.head=None

    def insert(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            node.next=self.head
        else:
            iter=self.head
            while iter.next!=self.head:
                iter = iter.next
            iter.next=node
            node.next=self.head
    
    def delete(self,data):
        if self.head is None:
            print("linked list is empty")
            return
        iter=self.head
        if iter.data==data:
            if iter.next==self.head:
                iter=None
                self.head=None
                return
            else:
                while iter.next!=self.head:
                    iter=iter.next
                iter.next=self.head.next
                self.head=self.head.next
                iter=None
                return        
        else:
            while iter.next!=self.head:
                if iter.next.data==data:
                    temp=iter.next.data
                    iter.next=iter.next.next
                    temp == None
                    return
                iter=iter.next

    
    def print_list(self):
        C_ll=""
        iter=self.head
        while iter:
            C_ll+= str(iter.data)+" "
            iter=iter.next
            if iter==self.head:
                break
        return C_ll
        
if __name__=='__main__':
    CLL=CircularLinkedlist()
    data = [4,5,6,7]
    for i in data:
        CLL.insert(i)
    print(CLL.print_list())
    CLL.insert(8)
    print(CLL.print_list())
    CLL.delete(5)
    print(CLL.print_list())