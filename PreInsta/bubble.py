def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
        if not swapped:
            break
    return arr
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted array using bubble sort:", bubble_sort(numbers))