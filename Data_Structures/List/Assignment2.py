"""Write a program to append a new item to the end of the list."""

#code

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

new_item = int(input("Enter a number to append: "))
numbers.append(new_item)

print("Updated list:", numbers)
