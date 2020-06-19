class Stack(object):
    def __init__(self):
        self.item=[]
    def push(self,item=""):
        self.item.append(item)
        pass
    def pop(self):
        self.item.pop()
        pass
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None
    def isempty(self):
        if self.item==[]:
            return True
        else:
            return False

if __name__=="__main__":
    stack=Stack()
    stack.push("1")
    stack.push("2")
    stack.push("3")
    stack.push("4")
    stack.push("55")
    stack.push("6")
    stack.push("7")
    print(stack.size())
    print(stack.peek())
    stack.pop()
    print(stack.size())
    print(stack.peek())
    print(stack.isempty())
