# **Find the closest Fibonacci number less than or equal to n.
def closest_fibonacci(n):
    if n < 0:
        return None 
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b
    return a
print(closest_fibonacci(30))  # Output: 21
print(closest_fibonacci(55))  # Output: 55
print(closest_fibonacci(4))   # Output: 3