# Find the smallest valuein an array
def findSmallest(arr):
    # Store the smalest value
    smallest = arr[0]
    # Store the smallest index of the smallest value
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index= i
    return smallest_index

# Sort array
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # find the smallest elemet in the array
        smallest = findSmallest(arr)
        # add the element to the new array
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 100, "e", "a"]))