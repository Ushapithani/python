rows = int(input("numbers increases throughout the pyrami :\n"))
num=1
for i in range(1, rows+1):
    for space in range(rows - i):
        print(" " , end=" ")
    for numbers in range(2*i-1):
        print(num, end=" ")
        num +=1
    print()
    '''
    '''