. #*Find the last digit of the `n`th Fibonacci number


def last_digit_fibonacci(n):
    n = n % 60 # Pisano period
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 10  
    return a

# Example
print(last_digit_fibonacci(7))    # Output: 13 
print(last_digit_fibonacci(120))  # Output: 1