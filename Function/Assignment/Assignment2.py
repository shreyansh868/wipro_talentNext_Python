"""Write a function to return the reverse of a string."""

#Code

def reverse_string(text):
    return text[::-1]

s = input("Enter a string: ")
print("Reversed string:", reverse_string(s))
