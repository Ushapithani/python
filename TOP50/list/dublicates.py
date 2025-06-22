my_list = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(my_list))
print(unique)



my_list = [1, 2, 2, 3, 4, 4, 5]
unique = []
for item in my_list:
    if item not in unique:
        unique.append(item)
print(unique)