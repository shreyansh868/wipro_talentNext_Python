"""Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it."""

#Code

filename = input("Enter the filename (with .txt extension): ")

try:
    with open(filename, 'r') as file:
        content = file.read()

    words = content.split()
    longest_word = max(words, key=len)

    print("\n🔍 Longest word in the file:")
    print(longest_word)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception as e:
    print(" An error occurred:", e)
