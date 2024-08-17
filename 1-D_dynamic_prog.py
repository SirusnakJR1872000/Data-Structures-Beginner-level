# lets understand 1-D programming 
# lets consider an expample of fibonacci sequence
# f(n) = f(n-1) + f(n-2) + ....................
# lets first try the brute force approach/recursion
def bruteforce(n): # we take the value n
    # let handle the base if n is 1 or 0 then we just return the same number
    if n <= 1:
        return n
    # now we will recursively call the bruteforce()
    return bruteforce(n - 1) + bruteforce(n - 2)

# now one thing we need to understand here is that if the number is small then it doesnt matter if we are recursively 
# checking for the same value
# but if the number is too big then we would perform the operation on same number multiple times
# so lets try another approach of memoization
def memoization(n, cache):
    # lets handle the base case
    if n <= 1:
        return n
    # now we will store the operation performed number in the cache 
    # and if that number is already in cache we return that number
    if n in cache:
        return cache[n]
    
    cache[n] = memoization(n - 1) + memoization(n - 2)
    return cache[n]

# the process of memoization is considered as a Top - Down approach
# because we start from the value and then go till the base

# another approach is a bottom - up approach
# which is a true dynamic programming approach

def dp(n):
    # handling the edge case where if the input is less than 2 that is 0 or 1 
    # we just return that number itself
    if n < 2:
        return n 
    
    # lets define an array with 2 elements 
    dp = [0, 1]
    # we start from 2 because we already have fibonacci of 0 and 1 which are our base case
    i = 2
    # so we go from 2 till we reach that number
    while i <= n:
        # we store the second elemnent in temp variable 
        temp = dp[1]
        # update the variable 
        dp[1] = dp[0] + dp[1]
        # and swap the value
        dp[0] = temp
        # increment the variable
        i += 1
    return dp[1]

