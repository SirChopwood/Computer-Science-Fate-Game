import BinarySearch
import BubbleSort
import datetime

size_datasets1 = [10, 30, 50, 100, 300, 500, 1000, 3000, 5000]
size_datasets2 = [10, 30, 50, 100, 300, 500]
speed_datasets1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
speed_datasets2 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]

option = input("1. Test Speed of different size datasets.\n2. Test speed of many same size datasets.\n")
if option == 1:
    datasets1 = size_datasets1
    datasets2 = size_datasets2
elif option == 2:
    datasets1 = speed_datasets1
    datasets2 = speed_datasets2
else:
    quit(69)


dataset_times = []
dataset2_times = []
for dataset in datasets1:
    start_time = datetime.datetime.now()
    BubbleSort.auto_bubblesort(dataset)
    end_time = datetime.datetime.now() - start_time
    print("Sorting Complete! (" + str(dataset) + ")")
    print("Completed in: " + str(end_time))
    dataset_times.append(end_time)

for dataset in datasets2:
    start_time = datetime.datetime.now()
    BinarySearch.auto_binarysearch(dataset)
    end_time = datetime.datetime.now() - start_time
    print("Searching Complete! (" + str(dataset) + ")")
    print("Completed in: " + str(end_time))
    dataset2_times.append(end_time)

