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
        newNode = ListNode(value)
        if self.head is None:
            self.head = newNode
            return 
        else:
            newNode.next = self.head
            self.head = newNode
            
      
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # first i will check if the head is None
        if self.head is None:
        # if it is none i will return nothing
            return
        else:
        # select the current head and create a variable 
            currentHead = self.head
        # making select the current heads next
        # and set the head to the head 
            self.head = currentHead.next
        # return head
            return self.head
            
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # take in the value add it to the list node
        newNode = ListNode(value)
        # and then check if the current tail is none
        if self.tail is None:
        # if the current tail is none i will set the the tail the new node
            self.tail = newNode
        else:
            currentTail = self.head
            while currentTail is not None:
                if currentTail.next is None:
                    break
                else:
                    currentTail = currentTail.next
            currentTail.next = newNode
            newNode.prev = currentTail
            self.tail = newNode
            return self.tail
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # Removing the current tail
        # first check if the current tail is None
        if self.tail is None:
        # if so return nothing
            return 
        else:
        # else first make a variable of the current tail
            current = self.tail
        # then create a variable fror the courrent previous
            previous = current.prev
        # then set the previous next to be none
            previous.next = None
        # set the that previous node as the new tail 
            val = current
            self.tail = previous
            return val
        # and then return the old current tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

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
        pass
    
    
myList = DoublyLinkedList()
myList.add_to_head(11)
myList.head.next = ListNode(44)
myList.head.next.prev = myList.head

myList.add_to_tail(33)
print(myList.head.value)
print(myList.tail.value)