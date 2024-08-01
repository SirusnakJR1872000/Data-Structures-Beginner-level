# lets write a code to implement a morege sort
# first lets define a function which will take the array, starting point, ending point 
def mergeSort(arr, s, e):
    # now we will check if the value is less than equal to 1 because if it is then we can just return the array as there is only on element
    if e - s + 1 <= 1:
        return arr
    
    # now lets calculate the middle index 
    m = (s+e) / 2

    # next we need to sort the left side
    mergeSort(arr, s, m)

    # next the right half
    mergeSort(arr, m+1, e)

    # now we merge both the halves
    merge(arr, s, m, e)

    return arr

# now we need to write a function to merge in place
def merge(arr, s, m, e):
    # now we know that it is two branch recursion so two halves are created
    L = arr[s: m+1]
    R = arr[m+1: e]

    i = 0 # index for left
    j = 0 # index for right
    k = s # index for arr

    # now we need to merge two sorted array into original array
    while i < len(L) and j < len[R]:
        # now we comapare the elements of left and right array
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1 #increment the counter for array

    # if there are some elements left in the array we will just add them to the original array
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1