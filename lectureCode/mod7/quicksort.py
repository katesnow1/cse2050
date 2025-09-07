def is_sorted(L): return all(L[i] <= L[i+1] for i in range(len(L)-1))

def quick_sort(L):
    """Uses quicksort to sort L in-place"""
    _quick_sort(L, left=0, right=len(L))

def _quick_sort(L, left, right):
    """Helper function does the actual work"""
    #base case
    if right-left < 2: return None #a list with 0 or 1 items is sorted

    #Recursive case = partition around a pivot, then recursively call on left and right "halves"
    pivot = partition(L, left, right) #store the index that I pivoted around
    _quick_sort(L, left, pivot)
    _quick_sort(L, pivot+1, right)




def partition(L, left, right):
    """Partitions L from [left:right] around a pivot"""
    i, j, pivot = left, right-2, right-1
    # pivot = right - 1
    # i = left
    # j = pivot - 1

    #Until i and j overlap
    while i < j:
        # Until I find a big item from the left
        while L[i] < L[pivot]: 
            i+=1

        #until I find a small item from the right
        while j>i and L[j] >= L[pivot]:
            j-=1

        #quick check in case i swept right past j
        # [1, 2, 3, 4]
        #i-^     ^-j 
        if i < j: 
            L[i], L[j] = L[j], L[i]

    #if I have a sublist of 2 items, then I start with i==j
    if L[i] >= L[pivot]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    return pivot



if __name__ == '__main__':
    ##################
    # Parition Tests #
    ##################
    L = ['e', 'd', 'c', 'b', 'a']
    # idx:0    1    2    3    4
    partition(L, 1, 3)
    assert L == ['e', 'c', 'd', 'b', 'a']    

    ###################
    # Quicksort Tests #
    ###################
    import random
    n = 100 
    L = [random.randint(0, 100) for i in range(n)]
    quick_sort(L)
    assert is_sorted(L)
    print("sorted!")