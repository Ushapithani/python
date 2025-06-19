t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    min_value = min(arr)
    count = 0
    for num in arr:
        if num != min_value:
            count += 1
    print(count)