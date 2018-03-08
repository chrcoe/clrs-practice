import math


def __swap(list_, first_index, second_index):
    list_[first_index], list_[second_index] = list_[
        second_index], list_[first_index]


def __heapify(list_, count):
    # start value is assigned based on the index of previous parent node
    start = int((count - 2) / 2)

    while start >= 0:
        __sift_down(list_, start, count - 1)
        start -= 1


def __sift_down(list_, start, end):
    '''
    This re-sorts the given list from the start to end indices.

    @param list_: the list to sort
    @param start: the index to start sorting at
    @param end: the index to sort down to
    '''

    def _has_one_child(root, end):
        # root has at least one child node
        return root * 2 + 1 <= end

    def _left_child(root):
        return root * 2 + 1

    def _has_sibling(child, end):
        return child + 1 <= end

    def _less_than_sibling(child):
        return list_[child] < list_[child + 1]

    def _out_of_order(root, child):
        return list_[root] < list_[child]

    # initialize the root to be the head value
    root = start

    while _has_one_child(root, end):
        child = _left_child(root)

        if _has_sibling(child, end) and _less_than_sibling(child):
            child += 1  # point to right child instead
        if _out_of_order(root, child):  # out of max-heap order
            __swap(list_, root, child)
            root = child
        else:
            return


def __merge(list_, p, q, r):
    # chap 4 in CLRS
    n1 = q - p + 1
    n2 = r - q
    # L(1..n + 1) and R(1..n + 1)
    l = list_[:n1 + 1]
    r = list_[:n2 + 1]

    for i in range(n1):
        l[i] = list_[p + i - 1]

    for j in range(n2):
        r[j] = list_[q + j]

    l[n1 + 1] = 'sentinel'
    r[n2 + 1] = 'sentinel'

    i = 1
    j = 1

    for k in range(p, r):
        if l[i] <= r[j]:
            list_[k] = l[i]
            i = i + 1
        else:
            list_[k] = r[j]
            j = j + 1


def selection_sort(list_):
    '''
    Sorts a list by looping the list_ and finding the minimum value and
    swapping it with the next item in the list.

    This algorithm takes O(n^2) for all situations because no matter what, both
    loops must run to completion.

    @param list_: a list to sort
    '''
    num_of_items = len(list_)

    for j in range(0, num_of_items - 1):
        # start with first item and make it the smallest
        smallest = j
        for i in range(j + 1, num_of_items):
            # check each additional item, if one is smaller than the current
            # smallest, set the smallest to the smaller item
            if list_[i] < list_[smallest]:
                smallest = i
        # after all items have been checked, swap the current smallest and the
        # current item
        __swap(list_, j, smallest)


def insertion_sort(list_):
    '''
    Sorts a list by looping over it and putting each item in the proper place.

    This algorithm takes O(n^2) for worst case scenarios.  When the list is
    nearly sorted, it takes O(n).

    @param list_: a list to sort
    '''
    # loop through the list indices
    for i in range(1, len(list_)):
        current_key = list_[i]
        index = i - 1
        while index >= 0 and list_[index] > current_key:
            # do the insert by swapping items
            __swap(list_, index, index + 1)
            # decrement the index
            index -= 1
        list_[index + 1] = current_key


def heap_sort(list_):
    '''
    Sorts an array-like list from min to max value using a heap.

    This algorithm takes O(nlogn) for worst and average case scenarios.

    @param list_: a list to sort
    '''
    num_of_items = len(list_)

    # will need to add the list to a heap where root is the max value
    __heapify(list_, num_of_items)

    # loop over items, swapping the max value (which is the root) of the heap
    # with the last element of the heap
    end = num_of_items - 1
    while end > 0:
        __swap(list_, end, 0)
        end -= 1  # change end value to preserve the previous max value
        __sift_down(list_, 0, end)  # resorts the heap to be in proper order


def merge_sort(list_, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(list_, p, q)
        merge_sort(list_, q + 1, r)
        __merge(list_, p, q, r)

if __name__ == '__main__':
    test = [5,2,4,7,1,3,2,6]
    merge_sort(test, len(test) // 2, len(test))
    print(test)
