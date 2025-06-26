def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print("Merged array:", merge_sorted_arrays(a, b)) #Merged array: [1, 2, 3, 4, 5, 6, 7, 8]


