"""Write a program to add a key and value to a dictionary."""

#code

data = {'name': 'Alex', 'age': 25}
print("Original dictionary:", data)

key = input("Enter key to add: ")
value = input("Enter value to add: ")

data[key] = value
print("Updated dictionary:", data)
