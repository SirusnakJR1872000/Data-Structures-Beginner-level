# nows lets understand 2-D dynamic programming with the help of the code 
# where we want to find the path from upper left most corner of the gird to the bottom right most corner
# so lets define a function to travel and we can only travel downwards and rightwards

def bruteforce(r, c, rows, cols):
    # we will check the base condition where:
    # if the r and c equals to rows or columns then we are out of bounds
    if r == rows or c == cols:
        return 0
    # and if we reach the last corner then we return true value
    if r == rows - 1 and c == cols - 1:
        return 1
    
    # now we just recursively call the function but we can only move in 2 directions 
    # that is down and right
    # hence we increment r and c
    return (bruteforce(r + 1, c, rows, cols) + bruteforce(r, c + 1, rows, cols))

# the process of memoization is considered as a Top - Down approach
# because we start from the value and then go till the base

def memoization(r, c, rows, cols, cache):
    # so we check for base conditions
    # if we are out of bounds
    if r == rows or c == cols:
        return 0
    # also we check if that place is stored in cache or not
    if cache[r][c] > 0:
        return cache[r][c]
    # if we have reached the end 
    if r == rows - 1 and c == cols - 1:
        return 1
    
    cache[r][c] = (memoization(r + 1, c, rows, cols, cache) + memoization(r, c + 1, rows, cols, cache))
    return cache[r][c]

# another approach is a bottom - up approach
# which is a true dynamic programming approach

def dp(rows, cols):
    # we will convert all elements of previosu row to zero becuase we are going from bottom to up
    prevRow = [0] * cols

    # now we keep on going till the end of the row and we reach the last element of previous row
    for r in range(rows - 1, -1, -1):
        # we convert everything to 0 in current row because we can easily overwrite 0
        currRow = [0] * cols
        # we convert the last element of the currRow to 1
        currRow[cols - 1] = 1
        # now we go from the last element to first element in the current row
        for c in range(cols - 2, -1, -1):
            # we add the diagonal elements
            currRow[c] = currRow[c + 1] + prevRow[c]
        # now we just make the current row as previous row
        prevRow = currRow
    return prevRow[0]



