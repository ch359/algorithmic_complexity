import time

results = []


def timer(setup, tested_function, iterations):
    setup()
    buffer = 10
    for i in range(0, iterations + buffer, 1):
        start = time.time()
        tested_function()
        end = time.time()
        print(end - start)
        if i >= buffer:
            results.append(end - start)


def test_function():
    time.sleep(0.5)


def setup_function():
    return


timer(setup_function, test_function, 20)
print(results)
