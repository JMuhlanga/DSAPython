# Example of Bubble sort algorithm
def bubble_sort(my_list)
    list_length = len(my_list)
    for i in range (list_length - 1):
        for j in range(list_length - 1 -i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

# Example of the same with isSorted variable
def bs_isSorted(my_list):
    list_length = len(my_list)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range (list_length - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i],my_list[i + 1] = my_list[i +1],my_list[i]
                is_sorted = False
        list_length -=1
    return my_list