"""Write a program to remove the item from a specified index in a list."""

#code

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

index = int(input("Enter the index to remove item from: "))

if 0 <= index < len(numbers):
    numbers.pop(index)
    print("Updated list:", numbers)
else:
    print("Invalid index.")
