"""Declare a list with 10 integers and ask the user to enter an index.
Check whether the number in that index is positive or negative number. 
If any invalid index is entered, handle the exception and print an error message"""

#Code

numbers = [10, -5, 23, -8, 0, 45, -11, 18, -30, 7]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]

    if value > 0:
        print(f"The number at index {index} is positive.")
    elif value < 0:
        print(f"The number at index {index} is negative.")
    else:
        print(f"The number at index {index} is zero.")

except IndexError:
    print("Error: Invalid index. Please enter a number between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer index.")
