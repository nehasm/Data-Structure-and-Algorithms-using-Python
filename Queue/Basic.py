class Queue(object):
    def __init__(self,limit=15):
        self.queue=[]
        self.limit=limit
    
    def __str__(self):
        return " ".join([str(i) for i in self.queue])

    def  isempty(self):
        return len(self.queue)<=0
    
    def isfull(self):
        return len(self.queue)>=self.limit
    
    def insertRear(self,data):
        if self.isfull():
            return
        else:
            self.queue.append(data)
    
    def insertFront(self,data):
        if self.isfull():
            return
        else:
            self.queue.insert(0,data)

    def deleteRear(self):
        if self.isempty():
            return
        else:
            self.queue.pop()
    
    def deleteFront(self):
        if self.isempty():
            return
        else:
            self.queue.pop(0)
    
if __name__=="__main__":
    myqueue=Queue()
    myqueue.insertFront(1)
    myqueue.insertFront(2)
    myqueue.insertFront(3)
    myqueue.insertRear(4)
    myqueue.insertRear(5)
    myqueue.insertRear(6)
    print(myqueue)
    myqueue.deleteFront()
    print(myqueue)
    myqueue.deleteRear()
    print(myqueue)

