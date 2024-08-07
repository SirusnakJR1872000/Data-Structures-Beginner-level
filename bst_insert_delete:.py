class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# now lets try inserting a value in the tree
def insert(root, val):

    if not root:
        return False
    
    if val < root.val:
        root.left = insert(root.left, val)

    elif val < root.val:
        root.right = insert(root.right, val)

    return root

# now lets try finding the minimum value in the tree
def findminimum(root):
    curr = root
    while curr and curr.left:
        curr = curr. left
    return curr

# now lets try to remove and return a value from the tree

def remove(root, val):

    if not root:
        return False
    
    if val < root.val:
        root.left = remove(root.left, val)

    elif val > root.val:
        root.right = remove(root.right, val)

    else:
        if not root.left:
            return root.right

        elif not root.right:
            return root.left
        
        else:
            minNode = findminimum(root.right)
            root.val = minNode
            root.right = remove(root.right, minNode.val)
    return root