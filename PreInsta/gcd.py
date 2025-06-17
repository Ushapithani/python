def gcd(a , b):
    while b:
        a , b = b , a%b
    return a
num1=int(input("enter a number:"))
num2=int(input("enter a number 2"))
print("gcd od two numbers:", gcd(num1 , num2))
