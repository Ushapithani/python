row = int(input("pyramid using numbers that are repeated")) 
for i in range(1, row+1):
    for space in range(row-i):
        print(" ", end= " ")
    
    for number in range(2*i-1):
            print(i, end=" ")
    print()

'''     1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5'''