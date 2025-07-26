"""Write a program to count the number of upper and lower case letters in a String."""

#Code

text = input("Enter a string: ")
upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
        
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
