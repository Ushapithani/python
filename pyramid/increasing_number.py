rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

    '''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
    '''

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1'''