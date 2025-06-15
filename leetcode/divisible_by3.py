def is_sum_divisible_by_3(n):
    total = 0
    original = n
    while n > 0:
        total += n % 10
        n //= 10
    return total % 3 == 0


number = int(input("Enter a number: "))
if is_sum_divisible_by_3(number):
    print(f"The sum of digits of {number} is divisible by 3.")
    
else:
    print(f"The sum of digits of {number} is NOT divisible by 3.")