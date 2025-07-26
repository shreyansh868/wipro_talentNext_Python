"""Project: 2

Create a Python module with the following functions:
Function Name
ispalindrome(name)
Task
Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name)
Given the user name as input, this function should tell us how many vowels are present in it.
frequency_of_letters(name)
Given the user name as input, this function should tell us how many times each letter appears in the name.
Note: name will be completely in either lower case or upper case.
Import the module in another python script and test the functions by passing appropriate inputs."""

#Code

def ispalindrome(name):
    return name == name[::-1]

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

name = input("Enter a name: ")

if ispalindrome(name):
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

print("Number of vowels:", count_the_vowels(name))

print("Letter frequency:")
for letter, count in frequency_of_letters(name).items():
    print(f"{letter}: {count}")

