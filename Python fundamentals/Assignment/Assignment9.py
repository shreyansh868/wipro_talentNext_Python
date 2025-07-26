"""Write a program to reverse a given number and print"""

num = int(input("Enter a number: "))

is_negative = num < 0

num = abs(num)
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if is_negative:
    reversed_num = -reversed_num

print("Reversed number:", reversed_num)
