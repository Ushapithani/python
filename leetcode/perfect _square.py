import math

def perfect_squares_in_range(start, end):
    squares = []
    for num in range(start, end + 1):
        root = math.isqrt(num)
        if root * root == num:
            squares.append(num)
    return squares



start = 1
end = 100

result = perfect_squares_in_range(1, 100)
print(f"Perfect squares between {start} and {end} are: {result}")