"""Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message"""

#code

import sys

if len(sys.argv) < 2:
    print("Please provide a welcome message as a command line argument.")
else:
    print("File Name:", sys.argv[0])
    print("Welcome Message:", ' '.join(sys.argv[1:]))
