"""Write a program to read first n lines from a txt file. Get n as user input."""

#Code

filename = input("Enter the filename (with .txt extension): ")
try:
    n = int(input("Enter the number of lines to read: "))

    with open(filename, 'r') as file:
        print(f"\n📄 First {n} line(s) from the file:\n")
        for i in range(n):
            line = file.readline()
            if line == '':
                print("[End of file reached]")
                break
            print(line.strip())

except FileNotFoundError:
    print(" File not found. Please check the file name.")
except ValueError:
    print(" Invalid input. Please enter a number for lines.")
except Exception as e:
    print(" An error occurred:", e)
