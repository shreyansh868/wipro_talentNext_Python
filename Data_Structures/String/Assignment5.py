"""Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. 
You may assume that n is between 0 and the length of the string inclusive. 
For example if the inputs are "Wipro" and 3, then the output should be "propropro"."""

#Code

text = input("Enter a string: ")
n = int(input("Enter an integer n: "))
result = text[-n:] * n
print("Resulting string:", result)
