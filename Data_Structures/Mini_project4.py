"""Given a string of n words, help Alex to find out how many times his name appears in the string.
Constraint: 1 <= n <= 200"""

#code
text = input("Enter the sentence: ")

count = text.count("Alex")

print("Number of times 'Alex' appears:", count)
