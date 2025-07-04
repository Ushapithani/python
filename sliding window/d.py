def maxTrublent(arr):
    n = len(arr)
    if n < 2:
        return n

    max_len = 1
    curr_len = 1

    for i in range(1, n):
        if i >= 2 and ((arr[i - 2] < arr[i - 1] > arr[i]) or (arr[i - 2] > arr[i - 1] < arr[i])):
            curr_len += 1
        else:
            if arr[i] != arr[i - 1]:
                curr_len = 2
            else:
                curr_len = 1
        max_len = max(max_len, curr_len)

    return max_len

arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print(maxTrublent(arr))