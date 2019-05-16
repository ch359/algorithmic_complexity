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
    with open('reverse_sort.csv', 'w') as csv_file:
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


#
# timer(setup_function, slow_flip_results_sort, 20)
# print(results)
# collate_results()
# print(results)
# write_results()

timer(setup_function, colin_reverse, 20)
collate_results()
print(results)
write_results()

