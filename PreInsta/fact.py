# facroriAL USING RECURSION
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
number=int(input("enter a number :"))
print("factorial of  a number", factorial(number))