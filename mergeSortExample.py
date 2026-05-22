# Example of Merge sort algorithm

def merge_sort(my_list):
    if len(my_list) > 1:
        # Divide the list into 2
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        # Carry out recursion
        merge_sort(left_half)
        merge_sort(right_half)

        # We proceed to merge the sorted parts
        i = j = k = 0

        # Step 1: Compare elements from both halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        # Step 2: Pick up any remaining elements from left_half
        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        # Step 3: Pick up any remaining elements from right_half
        while j < len(right_half):ch
            my_list[k] = right_half[j]
            j += 1
            k += 1

my_list = [35, 22, 90, 4, 50, 20, 30, 40, 1]
merge_sort(my_list)
print(f"Sorted list: {my_list}")