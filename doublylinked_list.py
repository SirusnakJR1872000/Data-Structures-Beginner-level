# lets write a code to implement a doubly linked list
# similar to singly linked list but here we also have a prev pointer
# first we will define a class for our node list

class ListNode:
    def __init__(self,val):
        # lets assign a value to the node in the list
        self.val = val
        # the next node will always be None because there is no other element
        self.next = None
        # here we have prev node and it would be set to None
        self.prev = None

   # lets implement the doubly linked list
class LinkedList:
    def __init__(self):
        # we will create a dummy head and dummy tail to handle edge cases
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        # now we will make the head and tail to pint at each other such that the structure is Head -> Tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # lets try adding node at the front of the list
    # current structure is Head -> Tail
    # we want to make it Head -> Current Node -> Tail
    def insertFront(self, val):
        # insert the node in the list
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        # now we have the structure as Head -> Node -> Tail
        # we want to make it as Head -> new node -> Node -> Tail
        self.head.next.prev = newNode
        self.head.next = newNode

    # lets try adding node at the front of the list
    # current structure is Head -> Tail
    # we want to make it Head -> Current Node -> Tail
    def insertEnd(self,val):
        # taking the value
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        # now we have the structure as Head -> Node -> Tail
        # we want to make it as Head -> Node -> newnode -> Tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # now lets try deleting a node from the front
    # we will remove the node after the dummy head ...........head -> node -> tail
    def removeFront(self):
        self.head.next.next.prev = self.head # getting to the node
        self.head.next = self.head.next.next # getting the refernce of tail

    # now lets try removing after the node
    # we will remov ethe node before the dummy tail .............head -> node -> tail
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail # getting at the node
        self.tail.prev.prev = self.tail.prev # getting the reference of head

    # now if we want to print the list
    def print(self):
        # we want to start printng after head as it is a dummy value
        curr = self.head.next
        # we want to run it till it reaches the tail
        while curr != self.tail:
            print(curr.val, "->")
            # increment the curr pointer
            curr = curr.next
        print()



