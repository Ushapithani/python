
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))


a = a + b
b = a - b
a = a - b


print("After swapping:")
print("a =", a)
print("b =", b)












low = int(input("Enter the start of the range: "))
high = int(input("Enter the end of the range: "))

print(f"Enter two numbers between {low} and {high}:")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))


if a < low or a > high or b < low or b > high:
    print("One or both values are out of the specified range.")
else:
    
    a = a + b
    b = a - b
    a = a - b

    print("After swapping:")
    print("a =", a)
    print("b =", b)