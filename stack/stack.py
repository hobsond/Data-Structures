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
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#         # self.storage = ?

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = len((self.storage))

#     def pop(self):
#         if self.size is 0:
#             return None
#         else:
#             pop = self.storage.pop()
#             self.size = len(self.storage)
#             return pop

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 
    def __str__(self):
        return f"{self.value}"
    
    def getNext(self):
        return self.next
    
    def getValue(self):
        return self.value
    
    def setNext(self,value):
        self.next = value
  
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size= 0
    
    def __len__(self):
        return self.size
    
    def add_toTail(self,value):
        new_node = Node(value)
        
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            
        else:
            item = self.head
            while item.next:
                item = item.next
            item.next = new_node
            self.tail = new_node
           
        
    def delete_tail(self):
        # first check to see if the list is empty
        curr = self.head
        old = curr.next 
        while curr.next:
            if curr.next:
                old = curr.next.value
                
                break
            else:
                
                curr = curr.next
        
        curr.next = None
        self.tail = curr
        return old
            
            
            
    def listPrint(self):
        curr = self.head
        while curr is not None:
            print(curr.getValue())
            IndexError
            curr = curr.next
        print(curr)
            
                
            
             

        
class Stack:
    
    def __init__(self):
        self.storage = LinkedList()
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def push(self,value):
        self.storage.add_toTail(value)
        self.size +=1
    def pop(self):
        if self.size > 0:
            self.size-=1
            return self.storage.delete_tail()
            
            
sean = LinkedList()
sean.add_toTail('33')
sean.add_toTail('44')
sean.delete_tail()
sean.listPrint()
sean.delete_tail()
sean.listPrint()