def find_min_max(arr):
    if not arr:
        return "Array is empty!"
    
    smallest = largest = arr[0]  
    
    for num in arr:  
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    
    return smallest, largest
numbers = [10, 23, 45, 5, 78, 2, 99]
result = find_min_max(numbers)
print(f"Smallest number: {result[0]}")
print(f"Largest number: {result[1]}")


print(result)  