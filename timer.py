import time
import random
import statistics
import csv

results = {}


def timer(setup, tested_function, iterations):
    buffer = 10
    for i in range(5000, 105000, 5000):
        results[i] = []
        for j in range(0, iterations + buffer, 1):
            test_data = setup(i)

            start = time.time()
            tested_function(test_data)
            end = time.time()

            if j >= buffer:
                results[i].append(end - start)


def test_function(data):
    data.sort()


def setup_function(num):
    test_data = []
    for i in range(0, num, 1):
        test_data.append(random.randint(0, 10))
    return test_data

def collate_results():
    for key in results.keys():
        results[key] = average_results(key)


def average_results(key):
    return statistics.mean(results[key])


def write_results():
    with open('builtin_sort.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in results.items():
            writer.writerow([key, value])


timer(setup_function, test_function, 20)
print(results)
collate_results()
print(results)
write_results()
