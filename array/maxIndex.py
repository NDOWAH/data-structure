import doctest

def maxIndex(arr) -> int:
    """
    This functions takes in an array with its size and return the max of j-i such that
    arr[i] <= arr[j]
    :param arr: integer array
    :return: int
    >>> maxIndex([9, 2, 3, 4, 5, 6, 7, 8, 18])
    8
    >>> maxIndex([34, 8, 10, 3, 2, 80, 30, 33, 1])
    6
    >>> maxIndex([1, 2, 3, 4, 5, 6])
    5
    """
    # To do: modify code to track the i and j
    # positions for which max difference occurred

    index_differences = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] - arr[j] > 0 or i == j:
                continue
            index_differences.append(j - i)
    return max(index_differences)


