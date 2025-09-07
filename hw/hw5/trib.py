def trib(k):
    """returns the kth number of the tribonacci sequence"""
    return _trib(k, dict())

def _trib(k, solved):
    """helper function for the trib function, does the recursion and keeps track of previously solved problems"""
    #base cases
    if k == 1: return 0
    elif k == 2: return 0
    elif k == 3: return 1
    elif k in solved.keys(): return solved[k]
    else:
        sum = _trib(k-1, solved) + _trib(k-2, solved) + _trib(k-3, solved)
        solved[k] = sum
        return sum