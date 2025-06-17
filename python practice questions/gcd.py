def find_gcd(a, b):
    while b:
        a, b = b, a % b  
    return a

a = 48
b = 18
gcd = find_gcd(a, b)
print(f"GCD of {a} and {b} is {gcd}")














def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

nums = [48, 18, 30, 42]
gcd_result = gcd_multiple(nums)

print(f"GCD of {nums} is {gcd_result}")
