"""Write a program to count the frequency of a user entered word in a text file."""

#Code

filename = input("Enter the filename (with .txt extension): ")
search_word = input("Enter the word to count: ")

try:
    with open(filename, 'r') as file:
        content = file.read()

    # Normalize case and split into words
    words = content.lower().split()
    word_count = words.count(search_word.lower())

    print(f"\n🔍 The word '{search_word}' appears {word_count} time(s) in the file.")

except FileNotFoundError:
    print("File not found. Please check the file name.")
except Exception as e:
    print(" An error occurred:", e)
