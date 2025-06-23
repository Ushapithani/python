def fibonacci_sum(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    total = a + b
    for _ in range(2, n):
        a, b = b, a + b
        total += b
    return total


print(fibonacci_sum(5))  # Output: 7