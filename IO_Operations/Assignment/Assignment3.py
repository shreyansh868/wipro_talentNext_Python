"""Write a program to accept input from user and append it to a txt file."""

#Code

filename = input("Enter the filename (with .txt extension): ")
user_input = input("Enter the text to append to the file: ")

try:
    with open(filename, 'a') as file:
        file.write(user_input + '\n')
    print("Text appended successfully.")
except Exception as e:
    print("An error occurred:", e)
