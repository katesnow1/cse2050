def quicksort(L):
    _quicksort(L, left=0, right=len(L))

def _quicksort(L, left, right):
    if right-left < 2: return

    pivot = partition(L, left, right)

    _quicksort(L, left, pivot)
    _quicksort(L, pivot+1, right)


def partition(L, left, right):
    i = left
    pivot = right-1
    j = pivot - 1

    while i < j:
        while L[i] < L[pivot]: i+=1

        while i < j and L[j] >= L[pivot]: j-=1

        if i < j: L[i], L[j] = L[j], L[i]
    
    if L[i] >= L[pivot]:
    
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    
    
    return pivot

if __name__ == '__main__':
    L = [2,4,7,3,7,3,7,3,7,32,3,8765,3]
    L2 = [2,4,7,3,7,3,7,3,7,32,3,8765,3]
    quicksort(L)
    L2.sort()
    assert L == L2
    print("all good")
