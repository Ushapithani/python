def round_robin_split(lst, k):
    return [lst[i::k] for i in range(k)]


lst = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(round_robin_split(lst, k))  # Output: [[1, 4, 7], [2, 5], [3, 6]]