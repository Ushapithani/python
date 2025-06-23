def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_of_squares(n):
    return fibonacci(n) * fibonacci(n + 1)


print(sum_of_squares(6))  # Output: 104