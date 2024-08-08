# lets write a code for backtracking through the tree

# lets initialize a class for the tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# lets see if the leaf node exists 
def LeafNode(root):
    # if the root does not exist
    if not root or root.val == 0:
        return False
    
    # if there is no left or right child
    if not root.left and not root.right:
        return True
    # if only the left child exists
    if LeafNode(root.left):
        return True
    # if only the right child exists
    if LeafNode(root.right):
        return True
    return False

def LeafPath(root, path):
    # if root does not exist
    if not root or root.val == 0:
        return False
    # adding the value to the list
    path .append(root.val)

    # if there are no left and right child
    if not root.left and not root.right:
        return True
    # if there is only a left child
    if LeafPath(root.left, path):
        return True
    # if there is only a right child
    if LeafPath(root.right, path):
        return True
    path.pop()
    return False