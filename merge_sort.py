import numpy as np
import math


def merge(array, p, q, r):

    n1 = q - p + 1              # n1 denotes the length of sub-array1
    n2 = r - q                  # n2 denotes the length of sub-array2

    # create temporary arrays to store sub-arrays that are to be merged
    left = np.arange(n1)
    right = np.arange(n2)

    # copy data from initial array to the temporary arrays
    for i in range(n1):
        left[i] = array[p + i]

    for j in range(n2):
        right[j] = array[q + j + 1]

    i = 0                       # index of the first sub-array left
    j = 0                       # index of the second sub-array right
    k = p                       # index of the merged array

    while (i < n1) & (j < n2):
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1

    while i < n1:
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < n2:
        array[k] = right[j]
        j = j + 1
        k = k + 1

    return array


def merge_sort(array, p, r):
    if p < r:
        q = math.floor((p + r)/2)

        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)

    return array

"""
    Description:
    Suppose we have am array that has been split into two sub-arrays. The split occurred right before q,
    ie we have got two sub-arrays: array[p, q - 1] and array[q, r]. This function would merge the two sub-arrays 
    into one.
"""


test = np.array([1, 2, 9, 3, 6, 2, 1, 4])
arr = [1, 3, 5, 6, 2, 3, 5, 8]
print(merge_sort(test, 0, 7))
