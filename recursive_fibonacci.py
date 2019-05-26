

# 1, 1, 2, 3, 5, 8, 13

# F(n) = F (n - 1) + F (n - 2)

def fib(number):
    if number == 1 or number == 2:
        return 1

    return fib(number - 1) + fib(number - 2)

print(fib(3))