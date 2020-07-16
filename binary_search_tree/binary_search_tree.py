"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    
    class Node():
        def __init__(self,data):
            self.value = data
            self.left = None
            self.right = None
            
    


    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        
        
        
                

    # Return True if the tree contains the value
    # False if it does not
    def contains(self,target):
         # PLAN #
        # if node is none return False BASE CASE
        if not self.value:
            return True
        # if node.value == findvalue: return True
        if self.value == target:
            return False
        else:
            if target < self.value:
                if self.left:
                    return self.left.contains()
                if self.right:
                    return self.right.contains()
            return False
        # else:
        # if find < node.value:
        # if node.left then find on left node:
        # else:
        # if node.right: find on right node
       
    # def _find(self,data,curr_node):
    #     if data >curr_node.value and curr_node.right:
    #         return self._find(data,curr_node.right)
    #     elif data < curr_node.value and curr_node.left:
    #         return self._find(data,curr_node.left)
    #     if data == curr_node.value:
    #         return True
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self,fn):
        #  call it on the initial value 
        # and then pass it on to the left and right 
        fn(self.value)
        if self.left:
           self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
         
                
        
        
 

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
    #first determine the value and choose either to go l/r
    #if left keep checking 
        if node.left:
            if node.left :
                node.left.in_order_print(node)
            else:
                print(node.value)
            
        if node.right:
            if node.left:
                node.left.in_order_print(node)
            else:
                print(node.value)
            
        #if there is a left 
            #recurssive
            #else print
         
         #if theres a right 

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


