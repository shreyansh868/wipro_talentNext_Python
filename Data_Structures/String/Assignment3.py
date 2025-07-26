"""Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2."""

#code

text = input("Enter a string (length >= 2): ")
n = len(text)
result = text[:2] * n
print("Resulting string:", result)
