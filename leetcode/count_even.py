def count_even_digits(n):
    count = 0
    n = abs(n)  
    if n == 0:
        return 1  
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n //= 10
    return count


number = int(input("Enter a number: "))
print("Number of even digits:", count_even_digits(number))








def get_even_digits(n):
    even_digits = []
    n = abs(n)  
    if n == 0:
        even_digits.append(0)
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_digits.append(digit)
        n //= 10
    return even_digits


number = int(input("Enter a number: "))
even_digits = get_even_digits(number)
print("Even digits:", even_digits[::-1])
print("Count of even digits:", len(even_digits))