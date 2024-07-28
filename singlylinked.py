# now lets write a code to implement singly linked list
# lets define  a class for ListNode

class ListNode:

    # define a constructor function
    def __init__(self, val):
        # we will initialize the first listnode where it takes the value and the next pointer is set to Null
        self.val = val
        self.next = None

# now lets define a linkedlist
class LinkedList:

    def __init__(self):
        # initializing a dummy node which makes removing the node from beginning very much easy
        self.head = ListNode(-1)
        self.tail = self.head

    # now lets try inserting element at the end
    def insertEnd(self, val):
        # for inserting we need to insert the value in the next node 
        # for this we will insert it in the next node to the tail
        self.tail.next = ListNode(val)
        # now after inserting we need to pass the reference to the next tail node to previous tail node to update it
        self.tail = self.tail.next

    # now lets try removing
    def delete(self, index):
        # we will initialize a counter variable to 0 to keep track of current position
        i = 0
        # initialize a curr variable to traverse through the list and point to current node
        curr = self.head
        # now we will iterate through the loop till we find the exact position that is just before the position of node that is to be deleted
        while i < index and curr:
            # we will increment the value of i to move to next target
            i += 1
            curr = curr.next

        # now we have to remove the node ahead of the current and make sure if curr and next curr is not empty
        if curr and curr.next:
            # we will first check if the element to be removed is the last node
            if curr.next == self.tail:
                # if this condition is satisfied then the tail pointer is set to the curr pointer which means that the last one is removed
                self.tail = curr
            # now we have to remove the element from the list therefore we will skip the element by calling next two times
            curr.next = curr.next.next  
    
    # now if we want to print the Linked List
    def print(self):
        # now we want to access the first node in the linked list
        # next is used because we used a dummy value of -1
        curr = self.head.next
        # now we will run the loop till curr is not None
        while curr:
            print(curr.val, " -> ", end = " ")
            # we need to update the curr pointer to traverse
            curr = curr.next
        print()
