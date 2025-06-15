def count_digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n //= 10
    return count


number = int(input("Enter a number: "))
print("Number of digits:", count_digits(abs(number)))