numbers = [12, 45, 7, 89, 23, 5, 67]

maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)



numbers = [12, 45, 7, 89, 23, 5, 67]


maximum = minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Maximum value:", maximum)
print("Minimum value:", minimum)