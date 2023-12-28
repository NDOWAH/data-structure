def maxIndex(arr) -> str:
    """
    This functions takes in an array with its size and return the max of j-i such that
    arr[i] <= arr[j]
    :param arr: integer array
    :return: int
    """
    index_differences = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j or arr[i] > arr[j]:
                continue
            index_differences.append(j - i)
            i_index = i
            j_index = j
    return f'{max(index_differences)} i->{i_index}, j->{j_index}'


print(maxIndex([34, 8, 10, 3, 2, 80, 30, 33, 1]))
