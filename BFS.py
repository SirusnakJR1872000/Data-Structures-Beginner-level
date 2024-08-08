# A Breadth First Search Tree is implemeneted using queues(to be precise deque - double ended queues)
# lets import it 
from collections import deque

# create a class for Tree where left and right are set to None
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def bfs(root):
        queue = deque()

        # we will check if root is not None
        if root:
            queue.append(root)

        level = 0 # the first level will be 0 and then we will increase it
        # now we run the loop till there are nodes in the queue/tree
        while len(queue) > 0: 
            print("level :", level)
            # now we will travel through the queue till its length
            for i in range(len(queue)):
                # first we will remove the left most child and store it in curr variable 
                curr = queue.popleft()
                print(curr.val)
                # now we will check if it has any child or not
                # if yes we will add it to the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # after adding we will increase the level by 1
            level += 1