"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

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
        return self.next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return 
        curr = self.tail
        
        curr.next = newNode
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
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = None
        self.tail = curr
    
    def listPrint(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next
            
            
            
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        
        return self.storage.add_to_tail(value)

    def pop(self):
        self.size -= 1
        return self.storage.remove_tail()
    


kid = Stack()

sean = LinkedList()
sean.add_to_tail(33)
sean.add_to_tail(44)
sean.remove_tail()
sean.listPrint()