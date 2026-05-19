# Recursion Example

## Exanple of factorial function
def factorial(n):
    result = 1
    while n > 1:
        result = n * result
        n -=1
    return result

print(factorial(5))

## Example of factorial function with the inclusion of recursion
def factorial_recursion(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)

print(factorial_recursion(4))

## Fibonacci with recursion
def fibonacci(n):
    # Define the base case
    if n <= 1:
        return n
    else:
        # Call recursively to fibonacci
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))

cache = [None] * (100)

## Fibonacci with Cache
def fibonacci_cache(n):
    if n <= 1:
        return n

    # Check if the value exists
    if not cache[n]:
        # Save the result in cache
        cache[n] = fibonacci_cache(n - 1) + fibonacci_cache(n - 2)

    return cache[n]


print(fibonacci_cache(6))


## Tower of Hanoi Example
def hanoi(num_disks, from_rod, to_rod, aux_rod):
  # Correct the base case
  if num_disks >= 1:
    # Correct the calls to the hanoi function
    hanoi(num_disks - 1, from_rod, to_rod, aux_rod)
    print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
    hanoi(num_disks - 1, from_rod, to_rod, aux_rod)

num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)