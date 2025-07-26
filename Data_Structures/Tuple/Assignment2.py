"""Write a program to check whether an element exists in a tuple or not."""

#code

numbers = (10, 20, 30, 40, 50)
element = int(input("Enter element to check: "))
if element in numbers:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")