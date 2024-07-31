# lets write a code to implement factorial
# lets define a function
def factorial(n):
    # now lets check the base condition
    # we know that 0! = 1 and 1! = 1so no point in recursively calling it
    if n <= 1:
        return 1
    # else if the number is greater than 1 then we will subtract it by 1 and multiply by number by the factorial of the difference of (n-1)
    return n * factorial(n-1)
