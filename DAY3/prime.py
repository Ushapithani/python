n=int(input())
flag = True
for i in range(2,n):
    if n%i==0:
        flag=False
    
        break
if flag:
    print("prime")
else:
    print(" not a prime number")
    