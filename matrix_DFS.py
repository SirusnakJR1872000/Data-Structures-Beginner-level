# lets write a code for Matrix DFS (Depth First Search)

# following is the 2D array
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# now lets define a function dfs
def dfs(grid, r, c, visit):
    # ROWS would have the outer list length  
    # COLS would have the first inner list
    ROWS, COLS = len(grid), len(grid[0])
    # now we will check the 4 conditions:
    # if position is out of bounds in 2 cases 
    # if the node is already vsisted
    # if there is an obstacle
    if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 1):
        return 0
    # now if we have reached the right and bottom most node 
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    
    # we will add this path
    visit.add((r,c))

    # now we we will set the initial count to 0 and perform the 4 operations:
    # moving up, down, left, right
    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    # now we will remove the node from the visited in case we hava another probable path from that node
    visit.remove((r,c))
    return count