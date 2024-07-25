# code for array 
def insert(arr, n, length, capacity):
    # for inserting we need to make sure that we have space in our array
    # and to ensure that there is space in the array the length of the array should be less than the capacity of array
    if length < capacity:
        arr[length] = n
        # inserting the value at that particular length
        # after inserting we have to increase the value of length since we have added an element to array
        return length + 1
    # if there is no space we will normally return the length
    return length

# if we want to delete the element from the array
def delete(arr, length):
    # we need to check if the array is empty or not 
    # that means the length should be greater than 0
    if length > 0:
        arr[length - 1] = 0
        # here we set a default value to 0 for the last element because we don't really delete the element we just keep it ready for overwriting
        return length - 1
    return length

# if we want to insert element in the middle to the array
def insertmiddle(arr, n, length, capacity, i):
    # again for insertion we need to make sure that the array has space in it
    if length < capacity:
        for index in range(length - 1, i -1, -1):
            arr[index + 1] = arr[index]
            #here each element is moved to the right to make space for the element to be inserted
        arr[i] = n
        #here we inserted the elemnent at the specified position
        # so now we have to increase the length by 1 and return the value
        return length + 1
    return length

# suppose we want to delete a value from the middle of the array
def removemiddle(arr, i, length):
    # to remove an element we need to make sure that the index is within the bounds of array
    if i < length:
        # we need to shift the elements to the left to overwrite the position of the deleted element
        for index in range(i + 1, length):
            # we will go to the element specified to be removed and we will shift it to the left
            # so here we assign the index of the previous element to the next element 
            arr[index - 1] = arr[index]
        return length - 1
    return length

def printarray(arr, capacity):
    for i in range(capacity):
        print(arr[i], end='')
    print()

# main function to get values from a user

def main():
    #get the capacity of array
    capacity = int(input("Enter the capacity of array : "))
    # now we need to create a array with specified capacity and we will assign 'capacity' no. of zeroes indicating fixed nature of arrays and 0 is a default value
    arr = [0] * capacity
    # now set the initial length to 0 indicating that the array is empty for now
    length = 0

    while True:
        print("\n Menu ")
        print("1. Insert element at the end of array ")
        print("2. Insert element at the middle of array ")
        print("3. Remove element from the end of the array ")
        print("4. Remove element from the middle of array ")
        print("5. Print the array ")
        choice = int(input("Enter your choice ; "))

        if choice == 1:
            n = int(input("Enter the value to be inserted : "))
            length = insert(arr, n, length, capacity)

        elif choice == 2:
            i = int(input("Enter the position at which the element is to be inserted: "))
            n = int(input("Enter the element to be inserted: "))
            # now we have to check whether the entered index is a valid index or not
            # for that index to be valid it should lie between 0 and the length of array
            if 0 <= i <= length:
                length = insertmiddle(arr, n, length, capacity, i)
            else: 
                print("Invalid index. Please try again")

        elif choice == 3:
            length = delete(arr, length)

        elif choice == 4:
            i = int(input("Enter the index from which the element is to be removed: "))
            # now we need to check if it is a valid index
            # for the index to be valid it should lie between 0 and the length of array
            if 0 <= i <= length:
                length = removemiddle(arr, i, length)
            else:
                print("Invalid index. Please try again")
            
        elif choice == 5:
            print("Array : ", end = '')
            printarray(arr, capacity)

        else:
            print("Invalid Input. Please try again.")

if __name__ == "__main__":
    main()

