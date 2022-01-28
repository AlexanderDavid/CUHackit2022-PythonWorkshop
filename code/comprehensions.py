[expression for item in list]

squares = []
for x in range(10):
    squares.append(x**2)

squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = []
for x in range(100):
    if is_prime(x):
        primes.append(x)

primes = [x for x in range(100) if is_prime(x)]
# [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

mat = [[1, 2, 3], [4, 5, 6]]
flat = [x for row in mat for x in row]
# [1, 2, 3, 4, 5, 6]

sent = "The quick brown fox jumps over the lazy dog"
num_vowels = len([letter for letter in sent if letter in "aeiou"])
# 11
