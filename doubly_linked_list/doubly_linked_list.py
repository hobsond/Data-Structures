"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def listPrint(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next
        
  
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #if the self head is empty i will insert the new node as the head
        if self.head is None:
            newNode = ListNode(value)
            self.head = newNode
            self.tail = newNode
            return
        else:
            newNode = ListNode(value)
            curr = self.head
            curr.prev = newNode
            newNode.next = curr
            self.head = newNode
            
      
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        curr = self.head
        theNext = curr.next
        theNext.prev = None
        self.head = theNext
        return curr.value
            
       
            
            
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail is None:
            newNode = ListNode(value)
            self.head = newNode
            self.tail = newNode
            return
        newNode = ListNode(value)
        curr = self.tail
        curr.next = newNode
        newNode.prev = curr
        self.tail = newNode
            
        
        
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        curr = self.tail
        prev = curr.prev
        prev.next = None
        self.tail = prev
        
        return curr
    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        curr = self.head 
        # while self.head is not node:
            

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        
        curr = self.head 
        while curr is not None:
            if curr.value is node:
                break
            else:
                curr = curr.next
            
        if curr is None:
            return 
        elif curr.next is None:
          return
        
        elif curr.prev is None:
            x= curr.next
            x.prev = None
            self.head = x
            currt = self.tail
            currt.next = curr
            curr.prev = currt
            self.tail = curr
        else:
            
            prev = curr.prev
            oNext= curr.next
            prev.next = oNext
            oNext.prev= prev
            currT = self.tail
            currT.next = curr
            curr.prev = currT
            self.tail = curr
            

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        curr = self.head
        while curr is not None:
            if curr.value is node:
                break
            else:
                curr = curr.next
        if curr.next is None:
            prev=curr.prev
            prev.next = None
            self.tail = prev
            return 
        if curr.prev is None:
            newNxt = curr.next
            newNxt.prev= None
            self.head = newNxt
            return
        else:
            prev= curr.prev
            newNxt = curr.next
            prev.next = newNxt
            newNxt.prev = prev
            return    
        
            
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        curr = self.head
        while curr is not None:
            if curr.value < curr.next.value:
                break
            else:
                curr = curr.next
                
        return curr.value
            
    
    

sean= DoublyLinkedList()

# sean.add_to_tail(22)
sean.add_to_head(33)
sean.add_to_head(44)
sean.add_to_tail(200)
# sean.listPrint()
# print('removed head')
# sean.remove_from_head()
# sean.listPrint()
# print('remove tail')
# sean.remove_from_tail()
# sean.listPrint()

# sean.move_to_end(44)
print()
sean.listPrint()
