"""Write a program to read the entire content from a txt file and display it to the user."""

#Code

filename = input("Enter the filename (with .txt extension): ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\n📄 File Content:\n")
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name and path.")
except Exception as e:
    print( An error occurred:", e)
