# Linear Search and Binary Search

## Linear Search
def linear_search(unordered_list,search_value):
    for index in range(len(unordered_list)):
        if unordered_list[index] == search_value:
            return True
    return False

### Returns True
print(linear_search([15,2,21,3,12,7,8],8))

### Returns False
print(linear_search([15,2,21,3,12,7,8],800))

## Binary Search
def binary_search(ordered_list,search_value):
    first = 0
    last = len(ordered_list) - 1

    while first <= last:
        middle = (first + last)//2
        if search_value == ordered_list[middle]:
            return True
        elif search_value < ordered_list[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False


### Binary search recursively
def binary_search_recursive(ordered_list, search_value):
    # Define the base case - Checking length of ordered list
    if len(ordered_list) == 0:
        return False
    else:
        middle = len(ordered_list) // 2
        # Check whether the search value equals the value in the middle
        if search_value == ordered_list[middle]:
            return True
        elif search_value < ordered_list[middle]:
            # Call recursively with the left half of the list
            return binary_search_recursive(ordered_list[:middle], search_value)
        else:
            # Call recursively with the right half of the list
            return binary_search_recursive(ordered_list[middle + 1:], search_value)


print(binary_search_recursive([1, 5, 8, 9, 15, 20, 70, 72], 5))
