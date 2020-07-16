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
        
            

jj= LinkedList()
jj.add_toTail(33)
jj.add_toTail(30)
jj.delete_head()
jj.listPrint()