
class Node:
    def __init__(self,value=None,next_node=None):
        self.value = value
        self.next = next_node
        
    def get_value(self):
        return self.value
    
    def getNext(self):
        return self.next
    
    def set_Next(self,value):
        self.next = value
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head = newNode
            return 
        curr = self.tail
        
        curr.set_Next(newNode)
        self.tail = newNode
        
    def remove_head(self):
        if self.head is None:
            return
        curr = self.head
        newHead = self.head.getNext()
        
        self.head = newHead
        
        return curr.get_value()
    
    def remove_tail(self):
        if self.tail is None:
            return
        currT= self.tail
        curr = self.head
        while curr.next:
            curr= curr.getNext()
        curr.set_Next(None)
        self.tail = curr
        return currT.get_value()
        
sean=LinkedList()

sean.add_to_tail(33)
sean.add_to_tail(22)
sean.remove_tail()