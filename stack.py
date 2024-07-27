# now lets implement a stack 

# implementing a stack is trivial using a dynamic array

# lets define a class 

class Stack:
    # lets define a constructor for the class stack
    # it is used to initialize a new instance of the class
    def __init__(self):
        # now we can initialize an empty list to store the elements in the stack
        self.stack = []

    # now lets create a function to push an element on the top of the stack
    def push(self, n):
        # we can use append() it will add the element to the end of the list
        self.stack.append(n)

    # now lets write a function to remove the last element from the stack
    def pop(self):
        # we can use pop() to do so, if it is passed without argument it will remove last element by default
        return self.stack.pop()
    

