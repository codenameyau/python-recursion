"""
merge_sort.py

Conceptually, merge sort works as follows:
1. Divide the unsorted list into n sublists, each containing 1 element
   (a list of 1 element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until
   there is only 1 sublist remaining. This will be the sorted list.

Notes:
You can probably optimize this solution by replacing the list pops
with indices. It will be an exercise for you! :)
"""

def sort(array=None):
    # Base Case.
    length = len(array)
    if length < 2:
        return array

    # Divide array.
    half_of_length = length / 2
    sorted_left = sort(array[0:half_of_length])
    sorted_right = sort(array[half_of_length:])
    merged_array = []

    # Perform merge with comparisons as long as both arrays are not empty.
    while sorted_left and sorted_right:
        left_element = sorted_left[0]
        right_element = sorted_right[0]
        if left_element <= right_element:
            merged_array.append(sorted_left.pop(0))
        else:
            merged_array.append(sorted_right.pop(0))

    # Perform the rest of the merge for the remaining array.
    while sorted_left:
        merged_array.append(sorted_left.pop(0))
    while sorted_right:
        merged_array.append(sorted_right.pop(0))
    return merged_array
