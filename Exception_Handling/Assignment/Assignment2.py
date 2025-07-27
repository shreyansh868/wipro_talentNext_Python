"""Write a program to accept a number from the user and check whether it's prime or not. 
If user enters anything other than number, handle the exception and print an error message."""

#Code

try:
    num = int(input("Enter a number: "))

    if num <= 1:
        print(f"{num} is not a prime number.")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")

except ValueError:
    print("Error: Please enter a valid integer.")
