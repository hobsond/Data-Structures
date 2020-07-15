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
        self.head = theNext
        return curr
            
       
            
            
            
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
        curr = self.head 
        
        while curr.next:
            curr = curr.next
            
        curr.next = newNode
        newNode.pre = curr
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
        prev.next =None
        self.tail = prev
        
        return curr
    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        curr = self.head 
        while curr is not None:
            if curr.value is node:
                break
            else:
                if curr is None:
                    return
                else:
                    curr = curr.next
        if curr.prev is None:
            return
            
        if curr.next is None:
            curr.prev.next = None
        
        s = curr.prev
        t = curr.next
        s.next = t
        t.prev = s
        self.add_to_head(curr.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        
        curr = self.head 
        while curr.value is not node:
            if curr.value is node:
                break
            else:
                curr = curr.next
            
        if curr is None:
            return None
        prev = curr.prev
        cNext = curr.next
        prev.next = cNext
        cNext.prev = prev
        x = self.head
        while x.next:
            x = x.next
        x.prev = self.tail
        x.next = curr
        curr.prev = x
        curr.next = None
        self.tail = curr

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            
            curr = curr.next
    
    

sean= DoublyLinkedList()

