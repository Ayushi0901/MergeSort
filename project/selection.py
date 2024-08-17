def selection_sort(data):
    # First, shift all the None elements (if any) to the front of the list
    none_count = data.count(None)
    data = [x for x in data if x is not None]
    data = [None] * none_count + data
    
    for i in range(none_count, len(data) - 1):
        min_idx = i

        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j

        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]

    return data

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
    ['banana', 'apple', 'orange', 'grape', 'mango']  # List with strings
]

for test in test_cases:
    print(f"Original: {test}")
    sorted_test = selection_sort(test.copy())
    print(f"Sorted: {sorted_test}")
    print('-' * 40)
