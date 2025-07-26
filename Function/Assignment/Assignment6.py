"""Write a function that takes a number as a parameter and checks whether the number is prime or not."""

#Code

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("The number is prime.")
else:
    print("The number is not prime.")
