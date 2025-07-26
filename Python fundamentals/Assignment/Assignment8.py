"""Write a program to print the sum of all the digits of a given number."""

num = int(input("Enter a number: "))

sum_of_digits = 0

n = abs(num) 
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n = n // 10

print("Sum of digits:", sum_of_digits)
