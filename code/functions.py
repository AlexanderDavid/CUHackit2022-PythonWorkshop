def fib(n, a=0, b=1):
    """Return the first n numbers of the Fibonacci sequence

    Keyword arguments:
    n -- length of sequence
    a -- first number
    b -- second number
    """
    fib = []
    for i in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

print(fib(5))
# >>> [0, 1, 1, 2, 3]
