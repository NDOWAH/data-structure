import doctest


def reverseArray(arr, arr_size):
    """
    This functions takes an array and return its reverse.
    :param arr: the array we want to reverse
    :param arr_size: size of the array we want to reverse
    :return: type of arr
    >>> reverseArray([1, 2, 6, 8, 9], 5)
    [9, 8, 6, 2, 1]
    >>> reverseArray([1, 2, 5, 9], 4)
    [9, 5, 2, 1]
    >>> reverseArray([12, 5, 3, 1], 4)
    [1, 3, 5, 12]
    >>> reverseArray([12], 1)
    [12]
    >>> reverseArray([], 0)
    []
    """
    reverse_array = []
    if arr_size == 1 or arr_size == 0:
        return arr
    else:
        while arr_size >= 0:
            reverse_array.append(arr[arr_size-1])
            arr_size -= 1
    return reverse_array[:-1]




