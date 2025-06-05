def add(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2
print("select operation\n"
"1.addition\n" 
"2.multiplication\n" 
"3.subtraction\n" 
"4.division\n")
cal=int(input(select operation(1-4)))
n1=int(input(enter first number))
n2=int(input(enter second operation))
if cal==1:
    print(n1,"+",n2,"=", add(n1,n2))
 elif cal==2:
    print(n1,"*",n2,"=", mul(n1,n2))
elif cal==3:
    print(n1,"-",n2,"=", sub(n1,n2))
elif cal==3:
    print(n1,"/",n2,"=", div(n1,n2))
else:
    print(invalid)


