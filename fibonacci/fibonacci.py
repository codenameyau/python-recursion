"""
fibonacci.py
"""

def fib(n):
    """
    Linear time iterative solution.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def fib_rec(n):
    """
    Recursive solution.

    Warning:
    The call stack grows exponentially as 'n' increase.
    Do not use the recursive solution beyond n = 20.
    """
    if n < 3:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def fib_binet(n):
    """
    Constant time solution using Binet's Fibonacci Number Formula.
    In real-use, GOLDEN_RATIO should be moved outside of this function
    to avoid unneccesary re-computation.
    """
    GOLDEN_RATIO = (1 + 5**0.5) / 2
    return int((GOLDEN_RATIO**n - (-GOLDEN_RATIO)**(-n)) / (5**0.5))
