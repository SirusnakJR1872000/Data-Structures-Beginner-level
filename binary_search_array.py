# suppose we have an array
arr = [1,3,3,4,5,6,7,8]

def binarySearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else :
            return mid
    return -1