def is_prime_n(n):
    if n < 2:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
print(f"{num} is prime: {is_prime_n(num)}")