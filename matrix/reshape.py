def reshape(mat, r, c):
    row = len(mat)
    col = len(mat[0])
    if row * col != r * c:
        return mat
    flat = []
    for row in mat:
        for num in row:
            flat.append(num)
    index = 0
    result =[]
    for i in range(r):
        new_row = []
        for j in range(c):
            new_row.append(flat[index])
            index +=1
        result.append(new_row)
    return result
mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(reshape(mat, r , c))


    
    


