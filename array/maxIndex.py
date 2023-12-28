def maxIndex(arr) -> str:
    """
    This functions takes in an array with its size and return the max of j-i such that
    arr[i] <= arr[j]
    :param arr: integer array
    :return: int
    """
    # To do: modify code to track the i and j
    # positions for which max difference occurred

    index_differences = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] - arr[j] > 0 or i == j:
                continue
            print(f'{i}<-->{j}')
            index_differences.append(j - i)
    return max(index_differences)


print(maxIndex([2, 9, 8, 1, 20]))
