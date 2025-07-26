"""Write a program to insert a new item before the second element in an existing list."""

#code

items = [10, 20, 30, 40, 50]
print("Original list:", items)

new_item = int(input("Enter the new item to insert before the second element: "))
items.insert(1, new_item)
print("Updated list:", items)
