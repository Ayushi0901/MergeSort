def insertion_sort(arr):
    # First, move all None values to the front
    none_count = arr.count(None)
    arr = [x for x in arr if x is not None]
    arr = [None] * none_count + arr

    length = len(arr) # Compute the length of the list
    
    # Now, apply insertion sort to the non-None part.
    for i in range(none_count + 1, length):
        temp = arr[i] 
        j = i - 1

        while (j >= none_count and arr[j] > temp):
            arr[j + 1] = arr[j] # Right shift the greater element by 1 place.
            j -= 1 # Decrement j by 1

        arr[j + 1] = temp

    return arr

test_cases = [
    [],  # Empty list
    [1, 2, 3, 4, 5],  # Already sorted list
    [5, 4, 3, 2, 1],  # Reverse sorted list
    [3, 1, 4, 1, 5, 9, 2, 6, 5],  # List with duplicates
    [-3, 1, -4, 0, 2, -1],  # List with negative numbers
    [3, 0, -2, 1, 5, 0, 4],  # List with zero
    [42],  # Single element list
    [100, 20, 50, 30, 80, 10, 90, 60, 40, 70],  # Large list
    [None, 3, None, 1, 2, None],  # List with None values
    [-4, 7, 9, 0, 14, None, None, 5, 2, 10, None, -101, -5, None, 3, 1, 35], # Combination of positive, negative, zero and None values
    ['banana', 'apple', 'orange', 'grape']  # List with strings
]

for test in test_cases:
    print(f'Original: {test}')
    result = insertion_sort(test.copy())
    print(f'Sorted: {result}')
    print('-' * 40)
