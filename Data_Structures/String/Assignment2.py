"""Write a program that will check whether a given String is Palindrome or not.."""

#code

text = input("Enter a string: ")

if text == text[::-1]:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")
