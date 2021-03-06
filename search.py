#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here

    if index >= len(array):     #check if index is valid
        return None     
    elif array[index] == item:  #'is' checks the equivelence in reference, '==' checks if they are identical
        return index
        
    index += 1
    return linear_search_recursive(array, item, index)

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    
    left = 0
    right = len(array) - 1

    while left <= right:
        median_index = (left + right) // 2
        median_value = array[median_index]

        if median_value == item:
            return median_index

        if item > median_value:         # item is to the right of the median
            left = median_index + 1
        else:
            right = median_index - 1    # item is to the left of the median

    return None # not found


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

    

    if left == None or right == None:
        left = 0
        right = len(array) - 1
    elif left > right:
        return None

    median_index = (right + left) // 2
    median_value = array[median_index]

    if median_value == item:
        return median_index

    if item > median_value:
        left = median_index + 1
    else: 
        right = median_index - 1

    # if right == left:
    #     if array[right] == item:
    #         return right
    #     return None

    return binary_search_recursive(array, item, left, right)




if __name__ == '__main__':
    print(binary_search_iterative([1, 3, 5, 9], 10))







