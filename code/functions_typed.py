from typing import List

def fib(n: int, a: int=0, b: int=0) -> List[int]:
    """Return the first n numbers of the Fibonacci sequence

    Keyword arguments:
    n -- length of sequence
    a -- first number
    b -- second number
    """
    fib = [] # type: List[int]
    for i in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

print(fib(5))
# >>> [0, 1, 1, 2, 3]
