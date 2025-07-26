"""Write a program to remove the first occurrence of a specified element from a list"""

#Code
numbers = [10, 20, 30, 40, 50, 30]
print("Original list:", numbers)

element = int(input("Enter the element to remove: "))

if element in numbers:
    numbers.remove(element)
    print("Updated list:", numbers)
else:
    print("Element not found in the list.")

