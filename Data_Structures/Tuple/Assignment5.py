"""Write a program to replace last value of tuples in a list to 100."""

#Code

my_list = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in my_list]
print("Updated list of tuples:", updated_list)
