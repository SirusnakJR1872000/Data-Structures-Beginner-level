# code for static array
# we will performing some basic function like inserting and deleting an element at the end of the array and also from the middle of the array

# the variables required would be:
# arr: array
# i: position
# n: element to be inserted 
# length: number of elements
# capacity: size of the array

# lets start with the first function

# here we will insert the element at the end of the array

def insertEnd(arr, n, length, capacity):
    # now we need to check if there is some space in the array
    # for that the length of the array should be less than that of the capacity
    if length < capacity:
        arr[length] = n
        # here we have inserted the value at the end of the array
        # after this we need to increment the length since we just inserted an element
        return length + 1
    return length

# now lets perfrom insertion in the middle of the array

def insertMiddle(arr, n, i, length, capacity):
    # now lets check if there is space in the array
    if length < capacity:
        # we need to shift the elements to the right to make room for the new element in the middle of the array
        for index in range(length - 1, i - 1, -1):
            # we are moving from back hence we are decrementing our counter
            arr[index + 1] = arr[index]
            # here we have shfted the element to the right by incrementing the pointer and now we will insert the element at the desired place
        arr[i] = n
        # now we will increment the length since we inserted a new element
        return length + 1 
    return length

def deleteEnd(arr, length):
    # for deleting an element we need to make sure that the array is not empty
    # we can do that by checking if length of the array is greater than 0
    if length > 0:
        # now we have to assign value 0 which is a default value to the end of the array so that we can overwrite it later
        arr[length - 1] = 0
        # now we just have to decrement the value of length by 1 since we deleted an element 
        return length - 1
    return length

def deleteMiddle(arr, i, length):
    # we need to check if the specified position is within the range of the array
    if i < length:
        # if this condition is satisfies then we can shift the elements towards the left
        for index in range(i + 1, length):
            arr[index - 1] = arr[index]
            # so we just assigned a previous position to the next element of the specified position
        return length - 1 
    return length

# now lets print the array
def printArray(arr, capacity):
    for i in range(capacity):
        print(arr[i], end= '')
    print()

# now its time for main function so that we can allow user to insert their specific values

def main():

    # lets intake the capacity of the array

    capacity = int(input("Enter the capacity of the array :"))
    
    # now after taking the capacity we can assign the 'capacity' number of zeroes and as we know zero is a default value and can be overwritten

    arr = [0] * capacity

    # lets assign length to be zero as well

    length = 0

    # writing a menu for user to choose the desired operation

    while True:
        print("\n Menu ")
        print(" Insert element at the end of the array")
        print(" Insert element in the middle of the array")
        print(" Delete element at the end of the array")
        print(" Delete element in the middle of the array")
        print(" Print the Array ")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter the element to be inserted at the end of the array: "))
            length = insertEnd(arr, n, length, capacity) # call the function

        elif choice == 2:
            n = int(input("Enter the element to be inserted: "))
            i = int(input("Enter the position at which the elemwnt is to be inserted: "))
            # now we have to check if the entered value is in the range of the array
            # we can do that checking if it lies between 0 and length and the actual array
            if 0 <= i <= length:
                length = insertMiddle(arr, n, i, length, capacity) # call the function
            else:
                print("Enter a valid choice.")

        elif choice == 3:
            length = deleteEnd(arr, length) # call the function

        elif choice == 4:
            i = int(input("Enter the position at which the value is supposed to be deleted"))
            # now we have to check if it is within the bound sof the array
            if 0 <= i <= length:
                length = deleteMiddle(arr, i, length) # call the function
            else:
                print("Enter a valid choice")
        
        elif choice == 5:
            print("Array :", end = '')
            printArray(arr, capacity) # call the function
        
        else:
            print("Please enter a valid choice.")

if __name__ == "__main__":
        main()
    
            




