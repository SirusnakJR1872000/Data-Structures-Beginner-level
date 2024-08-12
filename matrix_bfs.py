from collections import deque

# consider a 2D matrix
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# lets define a function for BFS
def bfs(grid):
    # we get the rows from the outer size of the grid 
    # we get the columns from the inner size of the grid
    Rows, Cols = len(grid), len(grid[0])
    # we will keep a track of the nodes visited
    visit = set()
    # we will store the cells to be explored in BFS
    queue = deque()
    # we will first adding the starting cell
    queue.append((0,0))
    # we also add it to the visited node
    visit.add((0,0))

    # we will use a length variable to keep track of number of steps taken to reach that path
    length = 0
    # we will now run the loop till queue is not Null
    while queue:
        for i in range(len(queue)):
            # we will remove the leftmost element i.e.the first element from the queue
            r, c = queue.popleft()
            # now if we reach the right and bottom most corner then we return the value
            if r == Rows - 1 and c == Cols - 1:
                return length
            
            # now if we define the directions that is move up, down, left , right
            neighbors = [[0,1], [0, -1], [1, 0], [-1, 0]]
            # now we check for the offsets
            for dr, dc in neighbors:
                # we will check for the conditions:
                # node is out of bounds
                # already visited
                # is a bloacked node
                if (min(r + dr, c + dc) < 0 or r + dr == Rows or c + dc == Cols or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                # we will add it to queue for further exploration
                queue.append((r + dr, c + dc))
                # then we also add it to already visited
                visit.add((r + dr, c + dc))
            # finally we increment the length
            length += 1