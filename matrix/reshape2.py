def reshape(mat, r, c):
    row = len(mat)
    col = len(mat[0])

    # reshape is possible
    if row * col != r * c:
        return [num for sub in mat for num in sub] 

    
    flat = []
    for sub in mat:
        for num in sub:
            flat.append(num)

    
    return flat
mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(reshape(mat, r, c))  # Output: [1, 2, 3, 4]