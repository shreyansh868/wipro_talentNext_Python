"""Write a program to find if the given number is palindrome or not"""

num = int(input("Enter a number: "))

original_num = num
num = abs(num)
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if abs(original_num) == reversed_num:
    print("The number is a Palindrome.")
else:
    print("The number is Not a Palindrome.")
