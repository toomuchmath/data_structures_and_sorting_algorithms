def parent(i):  # find the parent's index of an index, i
    return (i - 1) // 2


def left(i):  # find the left index of a given index i
    return 2 * i + 1


def right(i):  # find the right index of a given index i
    return 2 * (i + 1)


def max_heapify(array, i):
    l = left(i)
    r = right(i)
    if l < len(array) and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r < len(array) and array[r] > array[largest]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)

    return array


def build_max_heap(array):
    i = (len(array) - 1) // 2
    while i >= 0:
        max_heapify(array, i)
        i = i - 1
    return array


def heap_sort(array):
    build_max_heap(array)
    i = len(array) - 1
    sorted_list = []
    while i >= 1:
        array[0], array[i] = array[i], array[0]
        sorted_list
        array.pop()
        max_heapify(array, 0)
    return array


test = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print(build_max_heap(test))


