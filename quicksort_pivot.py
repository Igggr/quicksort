def quick_sort(array, start = 0, end = None, as_pivot = "first"):
    """   (list, int, int, string) -> none 
    
    Recursive in-place sort of given list:
    choose one element as a pivot, than swap pivot with first element
    in list and start compare all other elements in this list with pivot.
    If element smaller than pivot swap it with first element, that greater than pivot.
    Compliting this make recursive call on two slices of list, that consist of elements smaller and
    greater than choosen pivot"""
    
    if end is None:
        end = len(array) 
        
    if end - start <= 1:         # recursive base
        return 0
    
    if as_pivot == "first":
        pivot = array[start]
    else:
        if as_pivot == "last":
            pivot_index = end - 1 
            
        elif as_pivot == "random":
            pivot_index = random.randint(start, end - 1)     
            
        elif as_pivot == "middle":
            middle = (end - start - 1) // 2
            search_median = sorted( [ [array[start], start], 
                                      [array[end - 1], (end - 1)],
                                      [array[start + middle], (start + middle)] ])
            pivot_index = search_median[1][1]
            
        pivot = array[pivot_index]                      
        array[pivot_index] = array[start]                      # swap pivot and zero element
        array[start] = pivot                                   # in sub-array
           
    i = start + 1                       # border between elements less then pivot and bigger then pivot     
    for j in range(start + 1, end):
        if array[j] < pivot:
            tmp = array[i]              # first element bigger, than pivot
            array[i] = array[j]         # will be swaped with element less, than pivot 
            array[j] = tmp              # border between elements less than pivot, and bigerr than pivot  
            i += 1                      # will be moved right
    
    tmp = array[i-1]            # swap pivot and last elements, 
    array[i-1] = pivot          # that less than pivot
    array[start] = tmp
    
    l_start = start             # left slice of the list, that
    l_end = i - 1               # consist of elements less than pivot    
    r_start = i                 # right slice of the list, that 
    r_end = j + 1               # consist of elements greater than pivot
    
    quick_sort(array, l_start, l_end, as_pivot)         # recursive call on elements less than pivot
    quick_sort(array, r_start, r_end, as_pivot)         # recursive call on elements greater than pivot
