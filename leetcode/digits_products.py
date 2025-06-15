def product_of_digits(n):
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n //= 10
    return product

#
number = int(input("Enter a number: "))
print("Product of digits:", product_of_digits(number))