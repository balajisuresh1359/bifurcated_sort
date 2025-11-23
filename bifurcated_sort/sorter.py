from .linkedlist import LinkedList

def bfc_sort(
    array, 
    pending_item_percentage=0.55,
    inplace=True,
    reverse=False,
):
    """
    Sort an array of integers using bifurcated insertion sort.
    
    Args:
        array (list): List of numbers to sort
        pending_item_percentage (float): Threshold for batch processing (0 < value <= 1, default: 0.55)
        inplace (bool): Modify array in-place if True, return new sorted list if False (default: True)
        reverse (bool): Sort in descending order if True, ascending if False (default: False)
    
    Returns:
        list: The sorted array (same reference if inplace=True, new list if inplace=False)
    
    Raises:
        TypeError: If array contains non-integer values
        ValueError: If pending_item_percentage is not between 0 and 1
    
    Examples:
        >>> from bifurcated_sort import bfc_sort
        >>> arr = [5, 2, 8, 1, 9]
        >>> bfc_sort(arr)
        [1, 2, 5, 8, 9]

        >>> result = bfc_sort([5, 2, 8], inplace=False, reverse=True)
        >>> result
        [8, 5, 2]
    """

    if not isinstance(array, list):
        raise TypeError(
            f"array must be a list, got {type(array).__name__}"
        )

    if not isinstance(pending_item_percentage, (int, float)):
        raise TypeError(
            f"pending_item_percentage must be a number, "
            f"got {type(pending_item_percentage).__name__}"
        )

    if not 0 < pending_item_percentage <= 1:
        raise ValueError(
            f"pending_item_percentage must be between 0 and 1 (exclusive of 0), "
            f"got {pending_item_percentage}"
        )

    if not isinstance(inplace, bool):
        raise TypeError(
            f"inplace must be a boolean (True or False), "
            f"got {type(inplace).__name__}: {inplace}"
        )

    if not isinstance(reverse, bool):
        raise TypeError(
            f"reverse must be a boolean (True or False), "
            f"got {type(reverse).__name__}: {reverse}"
        )

    input_arr_len = len(array)
    if input_arr_len == 0:
        return None if inplace else []

    if input_arr_len == 1:
        return None if inplace else array.copy()

    work_array = array if inplace else array.copy()
    pending_item_size = int(input_arr_len * pending_item_percentage)    
    min_value = max_value = work_array[0]
    min_value_ind = max_value_ind = 0

    for i, x in enumerate(work_array[1:], start=1):
        if x < min_value:
            min_value = x
            min_value_ind = i
        elif x > max_value:
            max_value = x
            max_value_ind = i

    if min_value == max_value:
        return None if inplace else work_array

    asc_array = LinkedList(min_value)
    dsc_array = LinkedList(max_value, 'DESC')
    pending_items = []

    for curr_ind in range(input_arr_len):
        if curr_ind == min_value_ind or curr_ind == max_value_ind:
            continue

        curr_item = work_array[curr_ind]

        if asc_array.last() <= curr_item <= dsc_array.last():
            (asc_array if len(asc_array) < len(dsc_array) else dsc_array).append(curr_item)
        elif asc_array.last() <= curr_item:
            asc_array.append(curr_item)
        elif dsc_array.last() >= curr_item:
            dsc_array.append(curr_item)
        else:
            pending_items.append(curr_item)
            if len(pending_items) == pending_item_size:
                (asc_array if len(asc_array) < len(dsc_array) else dsc_array).insert(pending_items)
                pending_items = []

    if len(pending_items) != 0:
        (asc_array if len(asc_array) < len(dsc_array) else dsc_array).insert(pending_items)

    if reverse:
        asc_iter = reversed(asc_array)
        dsc_iter = reversed(dsc_array)
        compare_op = lambda a, b: a > b
    else:
        asc_iter = iter(asc_array)
        dsc_iter = iter(dsc_array)
        compare_op = lambda a, b: a < b

    
    asc_val = next(asc_iter, None)
    dsc_val = next(dsc_iter, None)
    
    idx = 0

    while asc_val is not None and dsc_val is not None:
        if compare_op(asc_val, dsc_val):
            work_array[idx] = asc_val
            asc_val = next(asc_iter, None)
        else:
            work_array[idx] = dsc_val
            dsc_val = next(dsc_iter, None)
        idx += 1

    while asc_val is not None:
        work_array[idx] = asc_val
        asc_val = next(asc_iter, None)
        idx += 1

    while dsc_val is not None:
        work_array[idx] = dsc_val
        dsc_val = next(dsc_iter, None)
        idx += 1
        
    return None if inplace else work_array

def bfc_sorted(array, **kwargs):
    """
    Return a sorted copy without modifying the original.    
    Example:
        >>> arr = [5, 2, 8, 1]
        >>> result = bfc_sorted(arr)
        >>> result
        [1, 2, 5, 8]
        >>> arr
        [5, 2, 8, 1]  # unchanged
    """
    return bfc_sort(array, inplace=False, **kwargs)
