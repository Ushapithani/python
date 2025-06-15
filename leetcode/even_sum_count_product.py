def analyze_even_digits(n):
    even_digits = []
    total = 0
    product = 1
    n = abs(n)
    if n == 0:
        even_digits.append(0)
        total = 0
        product = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_digits.append(digit)
            total += digit
            product *= digit
        n //= 10
    return even_digits[::-1], len(even_digits), total, product


number = int(input("Enter a number: "))
digits, count, sum_even, prod_even = analyze_even_digits(number)

print("Even digits:", digits)
print("Count of even digits:", count)
print("Sum of even digits:", sum_even)
print("Product of even digits:", prod_even)