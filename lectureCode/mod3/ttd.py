def sum_k(k):
    """Returns the sum of the first k integers"""
    return k/2 * (k+1)
    # _sum = 0

    # for _int in range(1, k+1):
    #     _sum += _int

    # return _sum

if __name__ == '__main__':
    assert sum_k(0) == 0
    assert sum_k(1) == 1
    assert sum_k(2) == 3
    assert sum_k(3) == 6
    assert sum_k(4) == 10
    assert sum_k(5) == 15