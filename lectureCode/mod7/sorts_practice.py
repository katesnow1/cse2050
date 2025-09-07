def fib(k):
    return _fib(k, solved=dict())

def _fib(k, solved):
    if k == 0:
        return 0
    if k == 1:
        return 1
    
    if k in solved:
        return solved[k]
    
    solved[k] = _fib(k-1, solved) + _fib(k-2, solved)

    return solved[k]


def fewest_coins(amt, coins):
    solved = {coin:1 for coin in coins}
    return _fc(amt, coins, solved)

def _fc(amt, coins, solved):
    if amt in solved:
        return solved[amt]
    
    valid_coins = [coin for coin in coins if coin <= amt]
    min_coins = float('inf')
    for coin in valid_coins:
        n_coins = 1 + _fc(amt-coin, coins, solved)
        
        if n_coins < min_coins:
            min_coins = n_coins

    solved[amt] = min_coins

    return solved[amt]
    
def binary(L, target):
    left = 0
    right = len(L)

    while left < right:
        mid_idx = (left+right) // 2
        mid_item = L[mid_idx]
        if mid_item == target:
            return True
        elif mid_item < target:
            left = mid_item + 1
        else:
            right = mid_item
    return False


def bs(L):
    n = len(L)
    swap = True
    j = 0
    while swap:
        swap = False
        for i in range(n-1-j):
            if L[i] > L[i+1]:
                swap = True
                L[i], L[i+1] = L[i+1], L[i]
        j+=1
        print(L)

def ss(L):
    n = len(L)
    for i in range(n-1):
        max_idx = 0
        for j in range(1, n-i):
            if L[j] > L[max_idx]:
                max_idx = j
        L[j], L[max_idx] = L[max_idx], L[j]
        print(L)

def ins(L):
    n = len(L)
    for i in range(n-1):
        j = n - 2 - i
        item = L[j]
        while j < n-1 and item > L[j+1]:
            L[j] = L[j+1]
            j+=1
        L[j] = item
        print(L)

def ms(L):
    n = len(L)
    if n <= 1:
        return L

    L_left = ms(L[:n//2])
    L_right = ms(L[n//2:])

    merge(L, L_left, L_right)

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


def qs(L):
    _qs(L, left=0, right=len(L))

def _qs(L, left, right):

    if right-left < 2: return None

    pivot = partition(L, left, right)

    _qs(L, left, pivot)

    _qs(L, pivot+1, right)

def partition(L, left, right):
    pivot = right-1
    i = left
    j = pivot - 1
    while i < j:
        while L[i] < L[pivot]:
            i+=1
        
        while j > i and L[j] >= L[pivot]:
            j-=1
        
        if i < j:
            L[i], L[j] = L[j], L[i]
    
    if L[i] >= L[pivot]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i
    return pivot
        
###############################################################################
# init, and repr  are implemented for you. You should implement the other     #
# methods recursively.                                                        #
###############################################################################
class Node:
    """Recursively implementes Linked List functionality"""
    def __init__(self, data, link=None):
        """Instantiates a new Node with given data"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"
    
    def __len__(self):
        """Recursively calculates length of sublist starting at this node"""
        return 1 if self.link is None else 1 + len(self.link)

    def get_tail(self):
        """Recursively finds the data stored in the tail of this sublist"""
        return self.data if self.link is None else self.link.get_tail()
    
    def add_last(self, data):
        """Recursively adds to end of this sublist"""
        if self.link is None:
            self.link = Node(data, None)
        else:
            self.link.add_last(data)

    def total(self):
        """Recursively adds all items"""
        return self.data if not self.link else self.data + self.link.total()
    
    def remove_last(self):
        """Recursively removes last item in sublist
            Returns a tuple of (new_head, data). The new_head is the
            new head of this sublist after removing the tail.

            OUTPUT
            ------
            new_head, tail_data
                * new_head: Node or None
                    The new link for whatever node called this function
                
                * tail_data: Any
                    The data that was found in the tail node
        """
        #finds the penultimate node
        if self.link is None:
            data = self.data
            return None, data
        new_head, tail_data = self.link.remove_last()
        self.link = new_head
        return self, tail_data


    def reverse(self, prev):
        """Recursively reverse list"""
        #check if self.link exists
        #before this, you must store self.link otherwise you'll lose access
        #want to make self.link = prev
        #when last step is recursion, tail recursion
        head = self if not self.link else self.link.reverse(self)
        self.link = prev
        return head
            




if __name__ == "__main__":
    L = [3,6,3,9,1,0,5,2]
    L2 = [3,6,3,9,1,0,5,2]
    print(L)
    ms(L)
    L2.sort()
    assert L == L2
    #assert fib(6) == 8
    #assert fewest_coins(50, [1, 5, 10, 25]) == 2
    #assert binary(L, 7) == False
    print ("all good")
