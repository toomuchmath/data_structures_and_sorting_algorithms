import time


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
print("sorted array: {}".format(sorted_array))

