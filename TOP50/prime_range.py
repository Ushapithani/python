def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for d in range(start, end + 1):
    if prime(d):
        print(d)