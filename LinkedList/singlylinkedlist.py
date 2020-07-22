#single linked list
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head == None:
            self.head=Node(data,None)
            return
        iter=self.head
        while iter.next:
            iter=iter.next
        iter.next=Node(data,None)

    def print(self):
        if self.head==None:
            print("Linked list is empty")
            return
        iter=self.head
        l=""
        while iter:
            l+=str(iter.data)+","
            iter=iter.next
        return print(l)

    def get_length(self):
        count=0
        iter=self.head
        while iter:
            count+=1
            iter=iter.next
        return count
    
    def insert_values(self,data_l):
        self.head=None
        for data in data_l:
            self.insert_at_end(data)

    def insert_at_index(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count=0
        iter=self.head
        while iter:
            if count == index - 1:
                node=Node(data,iter.next)
                iter.next=node
                break
            iter=iter.next
            count+=1

    def remove_at_index(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head=self.head.next
            return
        count=0
        iter=self.head
        while iter:
            if count==index-1:
                iter.next=iter.next.next
                break
            iter=iter.next
            count+=1
    
    def insert_after_value(self,data_after,data_insert):
        if self.head==Node:
            return 
        if self.head.data== data_after:
            self.head.next=Node(data_insert,self.head.next)
            return
        iter=self.head
        while iter:
            if iter.data == data_after:
                iter.next=Node(data_insert,iter.next)
                break
            iter=iter.next
            
    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        iter=self.head
        while iter.next:
            if iter.next.data==data:
                iter.next=iter.next.next
                break
            iter=iter.next

if __name__=="__main__":
    ll=Linkedlist()
    ll.insert_values(["black","blue","yellow","red","orange"])
    ll.insert_at_index(1,"pink")
    ll.remove_at_index(3)
    ll.print()
    ll.insert_at_beginning("green")
    ll.insert_at_end("white")
    ll.print()
    print(ll.get_length())
    ll.insert_after_value("orange","brown")
    ll.remove_by_value("red")
    ll.print()




    