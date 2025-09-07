def is_sorted(L):
    """Return false if any L[i] > L[i+1]"""
    return not any(L[i] > L[i+1] for i in range(len(L)- 1))

assert is_sorted([-3,-3,-3])
assert is_sorted([1,2,3])
assert not is_sorted([1,2,0])
print("all good")

def bubblesort(L):
    pass

n=5
L = [n-i for i in range(n)]  #reverse sorted list
bubblesort(L)
assert is_sorted(L) #is this a sufficient test case?

# 1) doesn't tell me if L contains the right items
# 2) need more unittests
#       * reverse sorted
#       * randomly sorted
#       * empty
#       * almost sorted
#       * sorted
#       * all the same number
#       * 0 < len(L) < 100

def bubble(L):
    n = len(L)

    #while not is_sorted(L):
    for j in range(n-1):
        for i in range(n-1-j):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]


def bubble_adaptive(L):
    n = len(L)

    ISSORTED = False
    j = 0
    while not ISSORTED:

        ISSORTED = True
        for i in range(n-1-j):
            if L[i] > L[i+1]:
                ISSORTED = False
                L[i], L[i+1] = L[i+1], L[i]
        j+=1

# [100, 0, 1, 3, 4]
# [0, 1, 3, 4, 100] #After first outloop