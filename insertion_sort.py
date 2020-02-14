def insertion_sort(array):

    for index in range(1, len(array)):
        key = array[index]
        j = index - 1
        while (j >= 0) and (array[j] > key):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

    return array


my_array = [0, 2, 1, 6, 3, 1]
sorted_array = insertion_sort(my_array)
print("sorted array: {}".format(sorted_array))  # sorted array: [0, 1, 1, 2, 3, 6]

"""
    notes:
    Time complexity: O(n^2) - worst case is when the array is in reverse order
    Memory consumption: O(n)
    Invariant: first i entries are sorted
"""
