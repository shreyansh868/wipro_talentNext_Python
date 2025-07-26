"""Write a program to check if a given key already exists in a dictionary."""

#Code

data = {'name': 'Alex', 'age': 25, 'city': 'New York'}
key = input("Enter key to check: ")

if key in data:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")
