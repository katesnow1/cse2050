def idx_left(L, idx, right):
    """return the index of the left child of param idx"""
    i_left = 2*idx + 1
    if i_left < right:
        return i_left
    else:
        return None

def idx_right(L, idx, right):
    """return the index of the right child of idx"""
    i_right = 2*idx + 2
    if i_right < right:
        return i_right
    else:
        return None

def idx_max_child(L, idx, right):
    """return the index of the max child of idx"""
    i_left, i_right = idx_left(L, idx, right), idx_right(L, idx, right)
    if i_left is None: return None
    elif i_right is None and i_left < right: return i_left
    else: 
        if L[i_left] >= L[i_right] and i_left < right:
            return i_left
        elif i_right < right:
            return i_right
        else:
            return None
    
def swap(L, i, j):
    """swaps the items at indices i and j"""
    L[i], L[j] = L[j], L[i]
    
def downheap(L, idx, right):
    """repeatedly downheaps the item at index idx until the array is heap-ordered"""
    idx_max = idx_max_child(L, idx, right)
    while idx_max is not None and L[idx] < L[idx_max]:
        swap(L, idx, idx_max)
        idx = idx_max
        idx_max = idx_max_child(L, idx, right)

def sorted(L):
    """checks if a list is sorted or not"""
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

def heapsort(L):
    """implements the heapsort algorithm"""
    #creates the max heap
    last_parent_idx = len(L) // 2 - 1
    for i in range(last_parent_idx, -1, -1):
        downheap(L, i, len(L))
    #now swap maximum item with final item
    right = len(L)-1
    while not sorted(L):
        swap(L, 0, right)
        right -=1
        downheap(L, 0, right)


    




if __name__ == '__main__':
    L = [3,6,3,8,2,9] 
    heapsort(L)
    print(L)