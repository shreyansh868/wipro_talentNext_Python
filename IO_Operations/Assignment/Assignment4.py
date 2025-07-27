"""Write a program to read contents from a txt file line by line and store each line into a list"""

#Code

filename = input("Enter the filename (with .txt extension): ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]  # Remove newline characters

    print("\n📄 Lines stored in the list:")
    print(lines)

except FileNotFoundError:
    print("File not found. Please check the file name.")
except Exception as e:
    print("An error occurred:", e)
