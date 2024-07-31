# lets write a code to implement fibonacci series
# lets first define a function which will accept the number 'n'

def fibonacci(n):

    # lets write our base condition 
    # in fibonacci if the number is 1 or less than 1 i.e. we return that respective number
    if n <= 1:
        return n
    
    # else we will return the sum of (n-1) + (n-2)
    return fibonacci(n-1) + fibonacci(n-2)