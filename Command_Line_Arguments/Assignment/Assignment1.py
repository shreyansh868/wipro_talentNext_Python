"""Write a program to accept two numbers as command line arguments and display their sum"""

#Code

import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers as command line arguments.")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    total = num1 + num2
    print("Sum:", total)

