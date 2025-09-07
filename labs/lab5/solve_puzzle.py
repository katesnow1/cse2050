def solve_puzzle(L): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    return _solve_puzzle(L, idx=0, visited=set())

def _solve_puzzle(L, idx, visited):
    """Helper function for solve_puzzle, does all the recursion and keeps track of which indices we've already visited"""
    #base cases
    if idx == len(L) - 1: return True
    if idx in visited: return False
    visited.add(idx)
    move = L[idx]
    size = len(L)
    #new moves (potential new idx) is cw, ccw
    cw = (idx + move) % size
    ccw = (idx - move) % size
    return _solve_puzzle(L, cw, visited) or _solve_puzzle(L, ccw, visited)