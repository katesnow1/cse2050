def merge_sort(L):
    n = len(L)
    if n < 2: return L
    L_left = merge_sort(L[:n//2])
    L_right = merge_sort(L[n//2:])
    merge(L_left, L_right)

    return L

def merge(L, L_left, L_right):
    i, j = 0, 0
    while i < len(L_left) and j < len(L_right):
        if L_left[i] <= L_right[j]:
            L[i+j] = L_left[i]
            i+=1

        else:
            L[i+j] = L_right[j]
            j+=1
    
    L[i+j:] = L_left[i:] + L_right[j:]
