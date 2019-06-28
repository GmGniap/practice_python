class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.getData

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
