"""Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values."""

#code

data = {'name': 'Alex', 'age': 25, 'city': 'New York'}

print("Keys:")
for key in data:
    print(key)

print("Values:")
for value in data.values():
    print(value)

print("Keys and Values:")
for key, value in data.items():
    print(key, ":", value)
