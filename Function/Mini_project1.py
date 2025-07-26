"""Project: 1

Write a Python function that accepts a hyphen-separated 
sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically."""

#Code

def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)

input_colors = input()
print(sort_colors(input_colors))
