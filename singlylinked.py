# lets write a code to implement a singly linked list
# now first we will implement a ListNode

class ListNode:
    def __init__(self, val):
        self.val = val # storing the value 
        self.next = None # reference to the next node(None since it is empty now)

# now we will implement a LinkedList
class LinkedList:
    def __init__(self):
        self.head = ListNode(-1) # we will store a arbitrary value -1 so that we can easily remove it
        self.tail = self.head # we need to initialize tail at the same place as that of head because initially only one element

    # now lets insert an element in the LinkedList
    def insert(self, val):
        self.tail.next = ListNode(val) # we will insert val at the end of the last node i.e. creating a new node
        self.tail = self.tail.next # now we will just update the tail pointer

    # now lets see how to delete an element from linked list
    def delete(self, index):
        # we will initialize a counter variable to traverse through the list 
        # and another variable to keep a track of the head variable
        i = 0
        curr = self.head
        # now we need to traverse through the loop till we reach the element before the element that is to be actually removed
        while i < index and curr:
            # we will increment the i counter and the curr counter
            i += 1
            curr = curr.next

            # we will make sure if the curr and curr.next are not 'None'
            if curr and curr.next:
                # now we have to make sure if the element is the last node or not
                if curr.next == self.tail:
                    # if it is the last element then we have to set the tail to curr val
                    self.tail = curr
                # if it is not the last element then we will assign the next counter to the next one
                curr.next = curr.next.next

        # now lets try printing the list
        def print(self):
            # we will assign a value to the head 
            curr = self.head
            # we will run the loop till curr is not None
            while curr:
                print(curr.val, "->", end=" ")
            print() 

    
