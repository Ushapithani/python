mat1 = [[1, 2, 3], [2, 3, 4], [4, 5, 5]]
mat2 = [[1, 2, 3], [2, 0, 0], [0, 1, 1]]

row = 3
col = 3
result = []

for i in range(row):
    rowlist = []
    for j in range(col):
        rowlist.append(mat1[i][j] + mat2[i][j])
    result.append(rowlist)

print("Sum of matrices:")
for row in result:
    print(row)