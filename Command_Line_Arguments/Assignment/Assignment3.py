"""Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them."""

#code

import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Please enter exactly 10 numbers as command line arguments.")
else:
    numbers = list(map(int, sys.argv[1:]))
    prime_sum = sum(num for num in numbers if is_prime(num))
    print("Sum of prime numbers:", prime_sum)
