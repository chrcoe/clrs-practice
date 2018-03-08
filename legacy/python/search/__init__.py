

def binary_search_iter(structure, item, *, low=0, high=None):
    '''
    Takes in a pre-sorted array, an item to search for and a range to search for.

    Uses an iterative approach.

    This algorithm runs in O(log(n)) because it is cutting down the search scope
    by half each time through the loop.

    @param structure: the array, or list to search through
    @param item: the item to search for
    @param low: the minimum value in the structure, if None, it will prime the
        function with the starting index in the structure
    @param high: the maximum value in the structure, if None, it will prime the
        function with the last index in the structure
    '''
    if not high:
        high = len(structure) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if item is structure[mid]:
            return mid
        elif item > structure[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None


def binary_search_recurs(structure, item, *, low=0, high=None):
    '''
    Takes in a pre-sorted array, an item to search for and a range to search for.

    Uses a recursive approach.

    This algorithm runs in O(log(n)) because it is cutting down the search scope
    by half each time through the loop.

    @param structure: the array, or list to search through
    @param item: the item to search for
    @param low: the minimum value in the structure, if None, it will prime the
        function with the starting index in the structure
    @param high: the maximum value in the structure, if None, it will prime the
        function with the last index in the structure
    '''
    if not high:
        high = len(structure) - 1

    if low > high:
        # stopping condition 1
        return None
    mid = int((low + high) / 2)
    if item is structure[mid]:
        # stopping condition 2
        return mid
    elif item > structure[mid]:
        # search upper half
        return binary_search_recurs(structure, item, low=mid + 1, high=high)
    else:
        # search lower half
        return binary_search_recurs(structure, item, low=low, high=mid - 1)


