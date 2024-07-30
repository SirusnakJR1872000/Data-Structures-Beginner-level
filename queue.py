# now we will implement a queue 
# in queue we follow FIFO concept - First In First Out
# lets first define a list node
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None # since the list is going to be empty in the beginning 

# now lets create a class for queue
class Queue:
    def __init__(self):
        # we will implement a dummy node so that we can handle edge cases
        self.left = self.right = None

    # now lets try adding elements to the queue
    def enqueue(self,val):
        # first lets add the element to the node
        newNode = ListNode(val)

        # now we need to check if the list is not empty
        if self.right:
            self.right.next = newNode # we will add the node to the next of the right dummy
            self.right = self.right.next # then we can update the right pointer
        # now if the queue is empty
        else:
            self.left = self.right = newNode # only one node

    # now lets see how we can delete an element from the queue
    def dequeue(self):
        # first we will check if the list is empty or not
        if not self.left:
            return None
        
        # if the queue had some nodes then we remove the left one because queue follows FIFO concept
        else:
            val = self.left.val # we will fetch the value and store it in a variable
            # now we need to make the next node as the left node as we are removing the first element
            self.left = self.left.next
            # now if there is no node left
            if not self.left:
                self.right = None # we will set the right dummy to None indicating the queue is empty
            # now we can return the value
            return val
        
    # now lets see how we can print the queue
    def print(self):
        # we will maintain a current pointer to traverse
        curr = self.left # it will start from left and go till right
        while curr:
            print(curr.val, "->")
            curr =  curr.next
        print()
