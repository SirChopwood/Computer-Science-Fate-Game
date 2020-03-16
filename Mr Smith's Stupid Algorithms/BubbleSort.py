import random
import datetime


def bubblesort():
    start_time = datetime.datetime.now()
    unsorted_list = []
    randomise = int(input("1. List 1-n\n2. List 1-(n*10)\n"))
    if randomise == 1:
        for i in range(int(input("How many numbers to sort? "))):
            unsorted_list.append(i)
    elif randomise == 2:
        for i in range(int(input("How many numbers to sort? "))):
            unsorted_list.append(i*random.randint(1, 10))

    for i in range(5):
        random.shuffle(unsorted_list)
    print(unsorted_list)

    new_list = unsorted_list
    sorting = True
    while sorting:
        changes_made = False
        for i in range(len(new_list)):

            try:
                if new_list[i] > new_list[i + 1]:
                    temp = new_list[i + 1]
                    new_list[i + 1] = new_list[i]
                    new_list[i] = temp
                    changes_made = True
                    print(new_list)

            except IndexError:
                break

        if not changes_made:
            sorting = False

    print("Sorting Complete!")
    end_time = datetime.datetime.now() - start_time
    print(end_time)
    return new_list

def auto_bubblesort(dataset_size):
    unsorted_list = []

    for i in range(dataset_size):
        unsorted_list.append(i*random.randint(1, 10))

    for i in range(5):
        random.shuffle(unsorted_list)

    new_list = unsorted_list
    sorting = True
    while sorting:
        changes_made = False
        for i in range(len(new_list)):

            try:
                if new_list[i] > new_list[i + 1]:
                    temp = new_list[i + 1]
                    new_list[i + 1] = new_list[i]
                    new_list[i] = temp
                    changes_made = True

            except IndexError:
                break

        if not changes_made:
            sorting = False

    return

def module_bubblesort(dataset_size):
    unsorted_list = []

    for i in range(dataset_size):
        unsorted_list.append(i*random.randint(1, 10))

    for i in range(5):
        random.shuffle(unsorted_list)

    new_list = unsorted_list
    sorting = True
    while sorting:
        changes_made = False
        for i in range(len(new_list)):

            try:
                if new_list[i] > new_list[i + 1]:
                    temp = new_list[i + 1]
                    new_list[i + 1] = new_list[i]
                    new_list[i] = temp
                    changes_made = True

            except IndexError:
                break

        if not changes_made:
            sorting = False

    return new_list