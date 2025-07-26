"""Write a program to concatenate the following dictionaries to create a new one."""

#Code

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print("Concatenated dictionary:", result)
