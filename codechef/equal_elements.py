t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    print(n - max_freq)