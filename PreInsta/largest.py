#  find the largest element in a list
def find_largest(arr):
    largest = arr[0]
    for num in arr:  
        if num > largest:  
            largest = num  
    return largest  

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


print(f"Largest element in the array: {find_largest(numbers)}")