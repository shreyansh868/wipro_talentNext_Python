"""Write a program to accept the file name to be opened from the user,
if file exist print the contents of the file in title case or else handle the exception and print an error message."""

filename = input("Enter the file name (with .txt extension): ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile Content in Title Case:\n")
        print(content.title())

except FileNotFoundError:
    print("Error: The specified file does not exist.")
except Exception as e:
    print("An unexpected error occurred:", e)
