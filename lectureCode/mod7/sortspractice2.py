def qs(L):
    _qs(L, left=0, right=len(L))

def _qs(L, left, right):
    if right - left < 2: return None

    pivot = partition(L, left, right)

    _qs(L, left, pivot)
    _qs(L, pivot+1, right)

def partition(L, left, right):
    pivot = right - 1
    i = left
    j = right - 2 
    while i < j:
        while L[i] < L[pivot]:
            i+=1

        while i < j and L[j] >= L[pivot]:
            j-=1

        if i < j:
            L[i], L[j] = L[j], L[i]
    
    if L[i] >= L[pivot]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i
    
    return pivot
    
def ins(L):
    n = len(L)
    for i in range(n-1):
        j = n - i - 2
        item = L[j]
        while j < n-1 and item > L[j+1]:
            L[j] = L[j+1]
            j+=1
        
        L[j] = item

if __name__ == "__main__":
    L = [3,6,3,9,1,0,5,2]
    L2 = [3,6,3,9,1,0,5,2]
    ins(L)
    L2.sort()
    assert L == L2
    #assert fib(6) == 8
    #assert fewest_coins(50, [1, 5, 10, 25]) == 2
    #assert binary(L, 9) == False
    print ("all good")