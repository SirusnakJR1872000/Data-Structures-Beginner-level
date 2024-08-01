#lets write a code to implement insertion sort
# lets define a function which will take the array
def insertionSort(arr):
    # now we need a pointer to traverse from the element at index 1 till the end of the array
    # from index 1 because we assume the first element is sorted 
    for i in range(1, len(arr)):
        # now we need another pointer to check to the left of the initial pointer
        j = i - 1
        # now we will run a loop till we go out of bounds and J+1 is less than j
        while j >= 0 and arr[j+1] < arr[j]:
            # we swap them
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            # now we decrement the j counter which we used to compare
            j -= 1
    # now we can return the array
    return arr
