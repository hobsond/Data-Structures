
from singly_linked_list.singly_linked_list import LinkedList,Node
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
            
            
