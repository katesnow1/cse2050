def mergesort(L):
    """sorts with merge sort"""
    n = len(L)

    if n < 2: return L

    L_left = mergesort(L[:n//2])
    L_right = mergesort(L[n//2:])
    merge(L, L_left, L_right)

    return L


def merge(L, L_left, L_right):
    """merges sorted lists L_left and L_right into L"""
    i, j = 0, 0
    while i < len(L_left) and j < len(L_right):
        if L_left[i] <= L_right[j]:
            L[i+j] = L_left[i]
            i+=1
        else:
            L[i+j] = L_right[j]
            j+=1
    
    L[i+j:] = L_left[i:] + L_right[j:]

if __name__ == '__main__':
    L = [0,48,1248,14,3,5,285]
    L2 = [0,48,1248,14,3,5,285]
    mergesort(L)
    L2.sort()
    assert L == L2

