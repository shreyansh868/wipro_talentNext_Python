"""Write a program to find the index of an item in a tuple."""

#code

my_tuple = (10, 20, 30, 40, 50)
item = int(input("Enter the item to find index: "))

if item in my_tuple:
    index = my_tuple.index(item)
    print("Index of the item:", index)
else:
    print("Item not found in the tuple.")
