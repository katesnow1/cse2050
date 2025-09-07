def bs(L, target):
    #BAD!

    if len(L) == 0:
        return False

    #find the middle index
    median_index = len(L) // 2

    #find the middle element
    middle_element = L[median_index]

    #case 1: match!
    if middle_element == target:
        return True
    
    #case 2: too small
    elif middle_element < target:
        return bs(L[median_index + 1:], target)

    #case 3: too big
    elif middle_element > target:
        return bs(L[:median_index], target)
    

def bs_good(L, target):

    return _bs_good(L, target, 0, len(L))
    
def _bs_good(L, target, start, end):

    if start >= end:
        return False

    #find the middle index
    median_index = (start + end) // 2

    #find the middle element
    middle_element = L[median_index]

    #case 1: match!
    if middle_element == target:
        return True
    
    #case 2: too small
    elif middle_element < target:
        return _bs_good(L, target, median_index + 1, end)

    #case 3: too big
    elif middle_element > target:
        return _bs_good(L, target, start, median_index)
    

 
def bs_iterative(L, target):

    start = 0
    end = len(L)

    while start < end:

        # find middle element
        median_index = (start + end) // 2
        middle_element = L[median_index]

        # case 1: match
        if middle_element == target:
            return True
        
        # case 2: too small
        elif middle_element < target:
            start = median_index + 1

        # case 3: too big
        elif middle_element > target:
            end = median_index

    return False


L = [1, 2, 3, 4, 5]
print(bs_iterative(L, 2))