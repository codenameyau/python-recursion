"""
merge_sort.py

Conceptually, merge sort works as follows:
1. Divide the unsorted list into n sublists, each containing 1 element
   (a list of 1 element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until
   there is only 1 sublist remaining. This will be the sorted list.
"""

def sort(array=None):
    # Base Case.
    length = len(array)
    if length < 2:
        return array

    # Divide array.
    half_of_length = length / 2
    left_array = sort(array[0:half_of_length])
    right_array = sort(array[half_of_length:])
    merged_array = []

    # Perform merge with comparisons as long as both arrays are not empty.
    while left_array and right_array:
        if left_array[0] <= right_array[0]:
            merged_array.append(left_array.pop(0))
        else:
            merged_array.append(right_array.pop(0))

    # Perform the rest of the merge for the remaining array.
    while left_array:
        merged_array.append(left_array.pop(0))
    while right_array:
        merged_array.append(right_array.pop(0))
    return merged_array


def sort_efficiently(array=None):
    # Base Case.
    length = len(array)
    if length < 2:
        return array

    # Divide Array.
    half_of_length = length / 2
    left_array = sort(array[0:half_of_length])
    right_array = sort(array[half_of_length:])
    merged_array = []

    # Perform merge with indices.
    left_index, right_index = 0, 0
    left_length, right_length = len(left_array), len(right_array)

    while left_index < left_length and right_index < right_length:
        left_element = left_array[left_index]
        right_element = right_array[right_index]
        if left_element <= right_element:
            merged_array.append(left_element)
            left_index += 1
        else:
            merged_array.append(right_element)
            right_index += 1

    # Concat the merged array with the rest of the unvisited elements.
    return merged_array + left_array[left_index:] + right_array[right_index:]
