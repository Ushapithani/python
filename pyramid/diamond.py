rows = int(input("for diamond: "))


for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  
    print("* " * i)                  

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")  
    print("* " * i)                   