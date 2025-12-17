# The above code checks if a number is prime or not.
"""
Rule 1: If n is less than or equal to 1 → ❌ Not prime.

Rule 2: Try dividing n by numbers from 2 up to √n (square root of n).

    1. If none of them divide it evenly (i.e., n % i ≠ 0 for all i), then n is ✅ Prime.

    2. If any of them divide it evenly (n % i == 0), then n is ❌ Not Prime.

"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # only up to √n
        if n % i == 0:
            return False
    return True

X = input("Enter any number: ")
n = int(X)
if is_prime(n):
    print(f"{n} is a prime number.")    
else:
    print(f"{n} is not a prime number.")


