def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

d = int(input("Enter a number: "))
a = prime(d)
print(a)