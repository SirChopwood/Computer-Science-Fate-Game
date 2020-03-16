import BubbleSort
import datetime
import random

def binarysearch():
    sorted_list = BubbleSort.bubblesort()

    search_item = int(input("Choose a number to search for. "))

    start_time = datetime.datetime.now()
    searching = True
    binary_list = [sorted_list]
    while searching:
        new_list = []
        for binary_item in binary_list:
            half_len = int(len(binary_item) / 2)
            half_point = binary_item[half_len]
            if half_point == search_item:
                print("Item found!")
                searching = False
                break
            elif len(binary_item) == 1:
                print("Item NOT found!")
                new_list.append(binary_item)
            else:
                print("Item NOT found! - Splitting!")
                new_list.append(binary_item[:half_len])
                new_list.append(binary_item[half_len:])
        binary_list = new_list
        print(binary_list)

    print("Searching Complete!")
    end_time = datetime.datetime.now() - start_time
    print(end_time)
    return binary_list


def auto_binarysearch(dataset_size):
    sorted_list = BubbleSort.module_bubblesort(dataset_size)

    search_rand = random.randint(0,len(sorted_list))
    search_item = sorted_list[search_rand]

    searching = True
    binary_list = [sorted_list]
    while searching:
        new_list = []
        for binary_item in binary_list:
            half_len = int(len(binary_item) / 2)
            half_point = binary_item[half_len]
            if half_point == search_item:
                searching = False
                break
            elif len(binary_item) == 1:
                new_list.append(binary_item)
            else:
                new_list.append(binary_item[:half_len])
                new_list.append(binary_item[half_len:])
        binary_list = new_list

    return
