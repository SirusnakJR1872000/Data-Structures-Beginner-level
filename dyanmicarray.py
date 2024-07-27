# now we will implement a dynamic array 
# unlike static array where there is fixed capacity dynamic array does not have a fixed capacity 
# here we double the size of the array and create a new one

# first we start by creating a class so that we can keep everything under the same hood

class Array:
    def __int__(self):
        # we will initialize the size to 2 in the beginning
        self.capacity = 2
        # setting the initial length (number of elements) to zero
        self.length = 0
        # we will create 2 elements both set to 0 as it can be overwritten (defualt value)
        self.arr = [0] * 2

    # now lets insert element at the end of the array
    def insertLast(self, n):
        # now we have to check if there is any space in the array
        # if the length is equal to that of the capcity then we do not have any space in the array
        # hence we would need to call the resize function (twice the size of the array)
        if self.length == self.capacity:
            self.resize()

        # inserting at the next empty position
        # after resizing the array we would insert the element at the next possible position
        self.arr[self.length] = n
        # after this we can increase the length of the array
        self.length += 1

    # now we need to resize the array if the array is full
    def resize(self):
        # we will create a array of double size
        self.capacity = 2 * self.capacity
        # now we will again initialize zeroes which is the default value to that of the new size
        newArr = [0] * self.capacity

        # now we need to copy the elements to the new array
        # so we will run a loop until the length of the updated array
        for i in range(self.length):
            newArr[i] = self.arr[i]
        # now we will reassign the reference of new Array to original Array
        self.arr = newArr

    # now lets write a function to remove the last element from the array
    def removeLast(self):
        # to remove an element from the array we need to make sure that array has some elements and is not empty
        # hence the length should be greater than 0
        if self.length > 0:
            # now by decreasing the length of the array we are actually removing the last element as the space is deallocated
            self.length -= 1

    # if we want to get the value at ith position
    def get(self, i):
        # we need to check if the given position is within the length of the array
        # we can do that by checking if the value of mentioned position is less than the length of array
        if i < self.length:
            # now we can return the value at the ith position in the array 
            return self.arr[i]
        # here we would throw out of bounds exception if the mentioned position is out of the bounds 

    # now if we need to insert the element at the ith position
    def insertAt(self, i, n): # we need the position(i) at which the element(n) is to be inserted
    # we need to check if the specified position is within the range
        if i < self.length:
            # now we can just assign the value at that position 
            self.arr[i] = n
            return

    # lets print the array 
    def printArray(self): # we need to pass the array
    # we will run the loop till the length of the array
        for i in range(self.length): 
            # we will print the array by accessing each index
            print(self.arr[i])
        print()


        


