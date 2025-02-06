from typing import List


def binary_search(arr: List, target: int) -> int:
    """
    Performs binary search on a sorted array to find the index of the target element.

    Parameters:
    arr: The sorted array to search in.
    target: The element to search for.

    Returns:
    The index of the target element if found, otherwise -1.
    """

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
