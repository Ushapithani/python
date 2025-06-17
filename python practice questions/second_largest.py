# Get numbers from user
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

# Check if there are at least two distinct numbers
if len(set(numbers)) < 2:
    print("No second largest number found.")
else:
    largest = max(numbers)  # Find the largest number
    numbers = [num for num in numbers if num != largest]
    second_largest = max(numbers)  
    print("Second largest number is:", second_largest)
