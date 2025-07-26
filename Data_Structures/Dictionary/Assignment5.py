"""Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included and the values are square of the keys."""

#code

squares = {}
for i in range(1, 16):
    squares[i] = i ** 2
print("Dictionary of squares from 1 to 15:", squares)