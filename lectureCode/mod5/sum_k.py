###################
# START RECORDING #
###################

def sum_k(k):
    """Returns the sum of the first k ints"""

    return (k/2) * (k+1) #O(1)

    # _sum = 0
    # for number in range(1, k+1):
    #     _sum += number

    # return _sum

def sum_k_rec(k):
    """Returns the sum of the first k ints"""
    #S_k = k + S_{k-1}
    # all recursive functions need a "base case" where they stop making recursive calls
    if k == 0: return 0
    return k + sum_k_rec(k-1)

    


if __name__ == '__main__':
    sols = {0:0, 
            1:1, 
            2:3, 
            3:6, 
            4:10, 
            5:15, 
            6:21, 
            7:28, 
            8:36, 
            9:45, 
            10:55}

    for key in sols:
        assert sum_k(key) == sols[key]
        assert sum_k_rec(key) == sols[key]

    print("all good!")