# lets implement a Depth First Search (DFS)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inOrder(root):
    if not root:
        return 
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def preOrder(root):
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)

    