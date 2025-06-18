# sum of natural numbers using  USING RECURSION
def sum_natural(n):
    if n==1:
        return 1
    return n+sum_natural(n-1)
number=int(input("enter a number :"))
print("sum  of  a number", sum_natural(number))