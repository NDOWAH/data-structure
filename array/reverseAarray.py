
def reverseArray(arr, arr_size):
    """
    This functions takes an array and return its reverse.
    :param arr: the array we want to reverse
    :param arr_size: size of the array we want to reverse
    :return: type of arr
    """
    reverse_array = []
    if arr_size == 1 or arr_size == 0:
        return arr
    else:
        while arr_size >= 0:
            reverse_array.append(arr[arr_size-1])
            arr_size -= 1
    return reverse_array


print(reverseArray([1, 2, 6, 8, 9], 5))



