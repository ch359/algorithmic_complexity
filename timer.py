import time
import random
import statistics
import csv

results = {}


def timer(setup, tested_function, iterations):
    buffer = 10
    for i in range(5000, 105000, 5000):
        results[i] = []
        print(results)
        for j in range(0, iterations + buffer, 1):
            test_data = setup(i)

            start = time.time()
            tested_function(test_data)
            end = time.time()

            if j >= buffer:
                results[i].append(end - start)


def test_function(data):
    data.reverse()


def setup_function(num):
    test_data = []
    for i in range(0, num, 1):
        test_data.append(random.randint(0, 100000))
    return test_data

def collate_results():
    for key in results.keys():
        results[key] = average_results(key)


def average_results(key):
    return statistics.mean(results[key])


def write_results():
    with open('colin_selection_sort.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in results.items():
            writer.writerow([key, value])

def slow_flip_results_sort(data):
    for i in range(1, len(data) -1, 1):
        later = data[i]
        earlier = data[i - 1]
        if later < earlier:
            data[i] = earlier
            data[i - 1] = later


def anchor_sort(data):
    anchor_position = 0
    anchor = data[anchor_position]
    while True:
        if anchor_position == len(data):
            break

        for i in range(anchor_position, len(data) - 1, 1):
            if data[i] < anchor:
                smaller = data.pop(i)
                data.insert(0, smaller)


def new_array_sort(data):
    sorted_data = [data[0]]

def colin_reverse(data):
    reversed = []
    for i in range(1, len(data) - 1, 1):
        reversed.append(data[i])
    return reversed

def kai_reverse(data):
    reversed = []
    for i in range(1, len(data) - 1, 1):
        reversed.append(data.pop())
    return reversed



#
# timer(setup_function, slow_flip_results_sort, 20)
# print(results)
# collate_results()
# print(results)
# write_results()
#




def merge_sort(data):

    # break problem down
    length = len(data)
    if len(data) < 2:
        return data
    left = data[:int(length/2)]
    right = data[int(length/2):]

    # recursive call
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # merge results
    index_left, index_right = 0, 0
    result = []
    # merge - loop
    while index_left < len(sorted_left) and index_right < len(sorted_right):
        # merge - compare numbers
        if sorted_left[index_left] <= sorted_right[index_right]:
            result.append(sorted_left[index_left])
            index_left += 1
        else:
            result.append(sorted_right[index_right])
            index_right += 1

    # merge - catch end of left and right arrays
    if index_left > len(sorted_left) - 1:
        result += sorted_right[index_right:]

    elif index_right > len(sorted_right) - 1:
        result += sorted_left[index_left:]

    # print(result)
    return result

def python_timsort(data):
    return data.sort()

def find_minimum_index(data):
    minimum = data[0]
    min_index = 0
    length = len(data)
    i = 0
    while i < length:
        if data[i] < minimum:
            minimum = data[i]
            min_index = i
        i += 1
    return min_index


def selection_sort(data):
    result = []
    while data:
        # minimum_position = find_minimum_index(data)
        minimum_position = data.index(min(data))
        result.append(data[minimum_position])
        data[minimum_position] = data[-1]
        data.pop()
    return result

#
timer(setup_function, selection_sort, 20)
collate_results()
print(results)
write_results()
#
#
# data = [3, 5, 2, 7, 4, 5, 10, 1]
# print(selection_sort(data))

