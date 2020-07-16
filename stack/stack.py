

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
        # refrence to head of the list
        self.head = None
        # refernce to tail
        self.tail = None
    
    def add_toTail(self,value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.setNext(new_node)
            
            self.tail=new_node
           
        
    def delete_tail(self):
        # first check to see if the list is empty
        if self.tail is None:
            return
        # old = self.tail
        
        curr = self.head
        while curr.next is not self.tail:
            old = curr.next
            curr= curr.next
        curr.next = None
        self.tail = curr
        return old.getValue()
        
            
    def delete_head(self):
        if self.head is None:
            return
        curr = self.head
        newNext = curr.next
        self.head = newNext
        curr.next = None
        
            
    def listPrint(self):
        curr = self.head
        while curr is not None:
            print(curr.getValue())
            IndexError
            curr = curr.next
        
            


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


            
