"""Write a function that accepts a string and prints the number of upper case letters and lower case letters in it."""

#Code

def count_case_letters(text):
    upper = 0
    lower = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

s = input("Enter a string: ")
count_case_letters(s)
