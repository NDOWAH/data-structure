def minMax(arr):
    """
    this function finds the min and max element in an array using the min number of comparison.
    :param arr: array we want to find the min/max element
    :return: tuple with first element min and last element max
    >>> minMax([1,2,5, 7, 10, 15, 20])
    (1, 20)
    >>> minMax([8, 5, 2, 45, 0, 30])
    (2, 45)
    >>> minMax([50, 20, 15, 5, 3, 2])
    (2, 50)
    >>> minMax([12])
    (12, 12)
    >>> minMax([])
    ()
    """
    result = []
    if len(arr) == 0:
        return tuple(arr)
    if len(arr) == 1:
        result.append(arr[0])
        result.append(arr[0])
        return tuple(result)
    arr.sort()
    result.append(arr[0])
    result.append(arr[len(arr)-1])
    return tuple(result)


arr = [50, 20, 15, 5, 3, 2]

print(arr.sort())
