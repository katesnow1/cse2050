import unittest

def factorial(k):
    """Returns the kth factorial"""
    #if k < 0: raise ValueError("Factorial isn't defined for negative numbers.")
    product = 1
    for num in range(1, k+1):
        product *= num
    return product
