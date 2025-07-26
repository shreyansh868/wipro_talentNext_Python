"""Write a function to print the even numbers from a given list. List is passed to the function as an argument."""

#Code

def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)

nums = [10, 15, 22, 33, 40, 55, 60]
print_even_numbers(nums)
