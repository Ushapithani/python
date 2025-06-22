my_list = [1, 2, 2, 3, 4, 4, 4, 5]
frequency = {}

for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)


#{1: 1, 2: 2, 3: 1, 4: 3, 5: 1}