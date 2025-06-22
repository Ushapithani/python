def swap(arr):
    for i in range(0 , len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
print(swap([1,2,3,4,5]))






def swap_adjacent_chars(s):
    chars = list(s)  
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i+1] = chars[i+1], chars[i]  
    return ''.join(chars)  


print(swap_adjacent_chars("hello"))  # Output: "ehllo"