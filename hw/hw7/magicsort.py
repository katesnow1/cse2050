import math
from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes

class MagicCase(Enum):
    """Enumeration for tracking which case we want to use in magicsort"""
    GENERAL = 0
    SORTED = 1
    CONSTANT_INVERSIONS = 2
    REVERSE_SORTED = 3

def linear_scan(L):
    """Counts how many times an element is larger than the next and returns a value to determine what type of sorting should be performed"""

    n = len(L)
    counter = 0 
    for i in range(n - 1):
        if L[i] > L[i+1]:
            counter+=1
    if counter == 0:
        return MagicCase.SORTED
    elif counter == n-1:
        return MagicCase.REVERSE_SORTED
    elif counter <= INVERSION_BOUND:
        return MagicCase.CONSTANT_INVERSIONS
    else:
        return MagicCase.GENERAL


def reverse_list(L, alg_set=None):
    """Reverses a list in place in O(n) running time"""
    if alg_set is not None: alg_set.add(reverse_list.__name__)
    else: alg_set = {reverse_list.__name__}
    n = len(L)
    for i in range(n//2):
        L[i], L[n-1-i] = L[n-1-i], L[i]
    return alg_set

def magic_insertionsort(L, left, right, alg_set=None):
    """Sorts the sublist L[left:right] using insertion sort"""
    if alg_set is not None: alg_set.add(magic_insertionsort.__name__)
    else: alg_set = {magic_insertionsort.__name__}
    for i in range(left + 1, right):
        item = L[i]
        j = i - 1

        while j >= left and item < L[j]:
            L[j+1] = L[j]
            j-=1

        L[j+1] = item
    return alg_set

def magic_mergesort(L, left, right, alg_set=None):
    """Sorts the sublist L[left:right] using merge sort"""
    if alg_set is not None: alg_set.add(magic_mergesort.__name__)
    else: alg_set = {magic_mergesort.__name__}
    L_slice = L[left:right]
    _mergesort(L_slice, alg_set)
    L[left:right] = L_slice
    return alg_set

def _mergesort(L, alg_set):
    """Sorts w/ merge sort"""
    n = len(L)
    if len(L) <= 20:
        magic_insertionsort(L, 0, len(L), alg_set)
    else:
        #base case
        if n < 2: return L # a list with 0 or 1 items is sorted

        #Recursive Case
        L_left = _mergesort(L[:n//2], alg_set)
        L_right = _mergesort(L[n//2:], alg_set)

        #combine
        merge(L, L_left, L_right)

    return L

def merge(L, L_left, L_right):
    """Merges sorted lists L_left and L_right into L"""
    i , j = 0, 0
    
    while i < len(L_left) and j < len(L_right):
        if L_left[i] < L_right[j]:
            L[i+j] = L_left[i]
            i+=1
        else:
            L[i+j] = L_right[j]
            j+=1

    L[i+j:] = L_left[i:] + L_right[j:]

def magic_quicksort(L, left, right, depth=0, alg_set=None):
    """Quick sorts the items in L from index left up to but not including index right"""
    if alg_set is not None: alg_set.add(magic_quicksort.__name__)
    else: alg_set = {magic_quicksort.__name__}
    if right-left < 2: return None
    bestCase = math.log2(len(L[left:right])) + 1
    depth+=1
    _quicksort(L,left,right,depth,bestCase, alg_set)
    return alg_set

def _quicksort(L, left, right,depth,bestCase, alg_set):
    """Helper function does the actual work"""
    if depth > 3 * bestCase:
       magic_mergesort(L, left, right, alg_set)
    else:
        if right-left < 2: return None

        pivot = partition(L, left, right)
        depth+=1
        _quicksort(L, left, pivot,depth,bestCase, alg_set)
        depth+=1
        _quicksort(L, pivot+1, right,depth,bestCase, alg_set)


def partition(L, left, right):
    """Partitions L from [left:right] around a pivot"""
    i, j, pivot = left, right-2, right-1

    while i < j:
        while L[i] < L[pivot]: 
            i+=1

        while j>i and L[j] >= L[pivot]:
            j-=1

        if i < j: 
            L[i], L[j] = L[j], L[i]

    if L[i] >= L[pivot]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    return pivot

def magicsort(L):
    """Calls linear scan and L and determines how the list should be sorted, while also keeping track of how many sorting algorithms are used in the process"""
    inversion_case = linear_scan(L)
    n = len(L)

    algs_used = set()

    if inversion_case == MagicCase.SORTED:
        return algs_used
    elif inversion_case == MagicCase.REVERSE_SORTED:
        algs_used = reverse_list(L)
    elif inversion_case == MagicCase.CONSTANT_INVERSIONS:
        algs_used = magic_insertionsort(L, 0, n)
    elif inversion_case == MagicCase.GENERAL:
        algs_used = magic_quicksort(L, 0, n)
    
    return algs_used



if __name__ == "__main__":
    L = [3,0,1,4,2,7,3]
#index= [0,1,2,3,4,5,6] 
   #L = [3,0,1,2,4,7,3]
   # i = 1
   # j = 3
   # item = 2
    print(magic_quicksort(L, 1, 5))