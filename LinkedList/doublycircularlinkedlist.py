class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        node=Node(data)
        if self.head is None:
            self.head = node
            node.next=self.head
            node.prev=self.head
        else:
            self.head.prev.next=node
            node.prev=self.head.prev
            node.next=self.head
            self.head.prev=node

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
                self.head.prev.next=self.head.next
                self.head.next.prev=self.head.prev
                self.head=self.head.next
                iter=None
                return     
        else:
            while iter:
                if iter.data==data:
                    iter.prev.next=iter.next
                    iter.next.prev=iter.prev
                    iter=None
                    return
                iter=iter.next
        return 


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
    CDLL=CircularDoublyLinkedList()
    data = [4,5,6,7]
    for i in data:
        CDLL.insert(i)
    print(CDLL.print_list())
    CDLL.insert(8)
    print(CDLL.print_list())
    CDLL.delete(5)
    print(CDLL.print_list())
    CDLL.delete(4)
    print(CDLL.print_list())
