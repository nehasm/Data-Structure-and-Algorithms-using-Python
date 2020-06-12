class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        iter = self.head
        l = ''
        while iter:
            l += str(iter.data) + ' , '
            iter = iter.next
        print(l)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        iter = last_node
        l = ''
        while iter:
            l += iter.data + ' , '
            iter = iter.prev
        print("Link list in reverse: ", l)

    def get_last_node(self):
        iter = self.head
        while iter.next:
            iter = iter.next

        return iter

    def get_length(self):
        count = 0
        iter = self.head
        while iter:
            count+=1
            iter = iter.next

        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        iter = self.head

        while iter.next:
            iter = iter.next

        iter.next = Node(data, None, iter)

    def insert_at_index(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_beginning(data)
            return

        count = 0
        iter = self.head
        while iter:
            if count == index - 1:
                node = Node(data, iter.next, iter)
                if node.next:
                    node.next.prev = node
                iter.next = node
                break

            iter = iter.next
            count += 1

    def remove_at_index(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        iter = self.head
        while iter:
            if count == index:
                iter.prev.next = iter.next
                if iter.next:
                    iter.next.prev = iter.prev
                break

            iter = iter.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["pink","red","green","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("black")
    ll.print_forward()
    ll.insert_at_beginning("blue")
    ll.print_forward()
    ll.insert_at_index(4,"brown")
    ll.print_forward()
    ll.insert_at_index(2,"yellow")
    ll.print_forward()
    ll.remove_at_index(3)
    ll.print_forward()
    print(ll.get_length())



