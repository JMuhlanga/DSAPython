# Selection & Insertion Sort Algorithm

def selection_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length - 1):
        lowest = my_list[i]
        index = i
        for j in range(i + 1, list_length):
            if my_list[j] < lowest:
                index = j
                lowest =my_list[j]
        my_list[i], my_list[index] = my_list[index],my_list[i]
    return my_list

def insertion_sort(my_list):
    for i in range(1,len(my_list)):
        number_to_order = my_list[i]
        j = i-1
        while j >= 0 and number_to_order < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = number_to_order
    return my_list

my_list = [6, 2, 9, 7, 4, 8]
selection_sort(my_list)
print(my_list)