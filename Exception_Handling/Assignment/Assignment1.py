"""Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result."""

#Code

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print(f" Result: {num1} ÷ {num2} = {result}")

except ZeroDivisionError:
    print(" Error: Division by zero is not allowed.")
except ValueError:
    print(" Error: Please enter valid numeric input.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
