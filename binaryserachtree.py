# lets write a code to implement a binary search tree
# initialize a class for tree node

class TreeNode:
    def __init__(self, val):
        self.val = val # we take in a value
        # initially we will assign None to the left and right pointer
        self.left = None 
        self.right = None
    
# if we want to search an element in the tree
def search(root, target): # takes in the tree and the target value
    # if there is no root that is tree does not exist
    if not root:
        return False
    
    # if the target is less than root we will search through the left side
    if target < root.val:
        return search(root.left, target)
    
    # if target is greater than root node we will search the right side
    elif target > root.val:
        return search(root.right, target)
    
    # if target is equal to root node we return the root
    else:
        return True
