def merge_sort(list_to_sort):
    """ (list) -> list
    Recursive sort of the list, not in place. Firstly we split list into two half, and each of them
    also split in half, and so on before lists length reach 1 or 0. Then we start merge them together:
    Compare i-elements from one list with j-element from another list, add smaller of them to merging list, 
    and increment index of element, that we will compare next time in corresponding list """
    
    len_list = len(list_to_sort)
    if len_list == 1 or len_list == 0:           # recursive base
        return list_to_sort
    half = len_list // 2
    list_joined = []
    list_1 = merge_sort(list_to_sort[:half])     # recursive call
    list_2 = merge_sort(list_to_sort[half:])     # recursive call
    i, j = 0, 0                                  # elements with this index will be compared
    for k in range(0, len_list):
        if j == len(list_2) or (i < len(list_1) and list_1[i] < list_2[j]):
            list_joined.append(list_1[i])
            i += 1
        else:
            list_joined.append(list_2[j])
            j += 1
    return list_joined
