# lets write a code for implementing a quick sort
# quick sort is the one where we pick a pivot element and compare all the elements

# lets write a function 
def QuickSort(arr: list[int], s: int, e: int) -> list[int]:
    # if array has only 1 element then we just return the array
    if e - s + 1 <= 1:
        return arr
    
    # lets pick the pivot as the last element
    pivot = arr[e]
    # and assign a pointer to the array from the start
    left = s

    for i in range(s, e): # we run the loop from start till the end
        # now we need to move elements smaller than pivot on left
        if arr[i] < pivot: # if the element is smaller than pivot then we swap
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            # increment the left pointer
            left += 1

    # move pivot in-between left and right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # quick sort left side
    QuickSort(arr, s, left - 1)

    # quick sort right side
    QuickSort(arr, left + 1, e)

    return arr
