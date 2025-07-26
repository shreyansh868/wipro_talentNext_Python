"""Write a program to remove a given item from the set."""

#code

my_set = {10, 20, 30, 40, 50}
item = int(input("Enter the item to remove: "))

if item in my_set:
    my_set.remove(item)
    print("Updated set:", my_set)
else:
    print("Item not found in the set.")
