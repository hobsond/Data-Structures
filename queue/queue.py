"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head= None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def addToHead(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.size +=1
            return self.head
        else:
            current = self.head
            newNode.next = current
            self.head = newNode.getValue()
            self.size +=1
            return self.head
    def removeHead(self):
        if self.head is None:
            return 
        else:
            current = self.head
            self.size -= 1
            self.head = current.getNext()
            return self.head
            
            
            
        





class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        # self.storage = ?
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.addToHead(value)

    def dequeue(self):
        if len(self.storage) > 0:
            self.size -= 1
            return self.storage.removeHead()
        else :
            return None
