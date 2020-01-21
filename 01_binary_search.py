def binary_search(list, item):
    # low and high keep track of which list you'll search in
    low = 0
    high = len(list) - 1
    
    # While you havent narrowed it down to one element
    while low <= high:
        # ....check the niddle element
        mid = (low + high) // 2
        guess = list[mid]
        # found the item
        if guess == item:
            return mid
        # guess was too high
        if guess > item:
            high = mid + 1
        # the guess wast too low
        else:
            low = mid + 1
            
    # item doesn't exist
    return None

my_list = [1, 3, 5, 7, 9, 11]
print(binary_search(my_list, 5)) # => 2

print(binary_search(my_list, 2))