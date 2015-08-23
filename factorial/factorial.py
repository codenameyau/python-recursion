"""
factorial.py
"""

def factorial(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result


def factorial_rec(n):
    if n < 2:
        return 1
    return n * factorial_rec(n-1)


def factorial_tail_rec(n):
    """
    Python does not support tail-call optimization so writing factorial in
    tail call style will not offer additional benefits in terms of efficient
    context passing during recursion. Recursion is considered "non-pythonic"
    and should be avoided.
    """
    def auxiliary(c, accumalation):
        if c < 2:
            return accumalation
        return auxiliary(c-1, c * accumalation)
    return auxiliary(n, 1)


def factorial_reduce(n):
    if n < 2:
        return 1
    return reduce(lambda x, y: x*y, range(1, n+1))
