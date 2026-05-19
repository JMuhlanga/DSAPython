# Explaining the Big-O-Notation

colors = ['green','yellow','blue','pink']

# O(1)
def constant(colors):
    print(colors[2])

constant(colors)
## The above only has one operation printing colors even if we add more colors

# O(n)
def linear(colors):
    for color in colors:
        print(color)

linear(colors)
## The loop above iterates over the list and prints each one , so the print operation runs on each item within the list
## Thus if we increase the number of items within the list then the time taken to carry out everything increases
## If we have four elements, that is when n=4,  we perform 4 print operations , if we have 7 elements then 7 operations

# O(n*n) O of n squared
def quadratic(colors):
    for first in colors:
        for second in colors:
            print(first,second)

quadratic(colors)
## The above contains a nested loop, we start a new loop for each element of the list, printing the color from the first loop and the current color from the second loop
## So if n is 3 we perform 9 operations, if n is 100 we complete 10000 operations
## This algorithm follows a quadratic pattern

# O(n*n*n*...) O of n powered by a specific number
## For example 0(n*n*n)
def cubic(colors):
    for color1 in colors:
        for color2 in colors:
            for color3 in colors:
                print(color1,color2,color3)

cubic(colors)
## For the example above it is a cubic complexity such that three nested loops iterate over each element of the list, following a cubic pattern

# Example of mixing
colors2 = ['green','yellow','blue','pink','black','white','purple'] # O(1)
other_colors = ['orange','brown'] # O(1)

def complex_algorithm(colors2):
    color_count = 0 # O(1)

    for color in colors2:
        print(color) # O(n)
        color_count += 1 # O(n)

    for other_color in other_colors:
        print(other_color) # O(m)
        color_count += 1 # O(m)

    print(color_count) # O(1)

complex_algorithm(colors2) # O(4 + 2n + 2m)

## Simplify Big-O-Notation by:
### We simplify by removing constants - O(4 + 2n + 2m) -> O(n + m)
### Different variables for different inputs - O(n+m)
### Remove Smaller terms by keeping the one that keeps increasing faster


