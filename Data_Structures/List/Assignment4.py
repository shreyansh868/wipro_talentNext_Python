"""Write a program to print the number of occurrences of a specified element in a list."""

#code

numbers = [10, 20, 10, 30, 40, 10, 50, 20]
print("List:", numbers)

element = int(input("Enter the element to count: "))

count = numbers.count(element)
print(f"The element {element} appears {count} time in the list.")
