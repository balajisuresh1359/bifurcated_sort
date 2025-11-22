from .linkedlist import LinkedList

def bfc_sort(array, pending_item_percentage=0.55):
    input_arr_len = len(array)
    if input_arr_len <= 1:
        return

    pending_item_size = max(int(input_arr_len * pending_item_percentage), 6)
    
    min_value = max_value = array[0]
    min_value_ind = max_value_ind = 0

    for i, x in enumerate(array[1:], start=1):
        if x < min_value:
            min_value = x
            min_value_ind = i
        elif x > max_value:
            max_value = x
            max_value_ind = i

    if min_value == max_value:
        return

    asc_array = LinkedList(min_value)
    dsc_array = LinkedList(max_value, 'DESC')
    pending_items = []

    for curr_ind in range(input_arr_len):
        if curr_ind == min_value_ind or curr_ind == max_value_ind:
            continue

        curr_item = array[curr_ind]

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

    asc_iter = iter(asc_array)
    dsc_iter = iter(dsc_array)
    
    asc_val = next(asc_iter, None)
    dsc_val = next(dsc_iter, None)
    
    idx = 0

    while asc_val is not None and dsc_val is not None:
        if asc_val < dsc_val:
            array[idx] = asc_val
            asc_val = next(asc_iter, None)
        else:
            array[idx] = dsc_val
            dsc_val = next(dsc_iter, None)
        idx += 1

    while asc_val is not None:
        array[idx] = asc_val
        asc_val = next(asc_iter, None)
        idx += 1

    while dsc_val is not None:
        array[idx] = dsc_val
        dsc_val = next(dsc_iter, None)
        idx += 1
