"""Given two non-negative values, print true if they have the same last digit, such as with 27 and 57. 
lastDigit(7, 17) true 
lastDigit(6, 17) false
lastDigit(3, 113) true"""

dig1=int(input("enter first number"))
dig2=int(input("enter first number"))
if dig1%10==dig2%10:
    print(True)
else:
    print(False)


