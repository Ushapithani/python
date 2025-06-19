def solve():
    arr = list(map(int,input().split()))
    freq={}
    for num in arr:
        freq[num] = freq.get(num, 0)+1
    max_freq=0
    dominant=None
    for num, count in freq.items():
        if count > max_freq:
            max_freq = count
            dominant = num
    
    count = 0
    for num, freq_count in freq.items():
        if freq_count == max_freq:
            count += 1
    
    if count > 1:
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    n = int(input())
    solve()