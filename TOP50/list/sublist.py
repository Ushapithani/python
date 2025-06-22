# flatten a sublist


nested_list = [[1, 2], (3, 4), [5]]
flattened = []

for sublist in nested_list:
    for item in sublist:
        flattened.append(item)

print(flattened)  # Output: [1, 2, 3, 4, 5]