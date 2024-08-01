# now we will implement a code for bucket sort
# so lets say we have an array : [0,0,2,1,2,2]

# lets define a fucntion first
def bucketSort(arr):
    # since we have only 3 values : 0 , 1 , 2
    counts = [0,0,0]

    # we want to count the quantity of each value in the array
    for n in arr:
        counts[n] += 1

    # now we will fill each bucket in the original array
    # lets initialize a variable to fill elements back in the array
    i = 0
    # we will run the loop till the number of values we have 0,1,2
    for n in range(len(counts)): 
        # we will run the loop till the number of elements in the bucket
        for j in range(len(counts[n])):
            arr[i] = n
            i += 1
    return arr