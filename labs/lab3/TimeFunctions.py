import time
def time_function(func, args, n_trials = 10):
    """Returns minimum time (out of n_trials) it takes to complete func with arg"""
    min_time = float('inf')
    for _ in range(n_trials):
        start = time.time()
        func(args)
        end = time.time()
        elasped = end - start
        if elasped < min_time: min_time = elasped
    return min_time

def time_function_flexible(func, args, n_trials = 10):
    """Returns minimum time (out of n_trials) it takes to complete func with multiple args"""
    min_time = float('inf')
    for _ in range(n_trials):
        start = time.time()
        func(*args)
        end = time.time()
        elasped = end - start
        if elasped < min_time: min_time = elasped
    return min_time



if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))