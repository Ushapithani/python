import opera as op
num1 = int(input())

while True:
    ope=input()
    if ope=="=":
        print("total=",num1)
        break
    num2 = int(input())

    if ope == "+":
        num1=op.add(num1,num2)
    elif ope== "-":
        num1=op.sub(num1,num2)
    elif ope == "*":
       num1=op.mul(num1,num2)

    elif ope == "/":
        num=op.div(num1,num2)
        print(num1)