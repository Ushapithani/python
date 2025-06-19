t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    min_value=min(arr)
    total_cost=min_value*(n-1)
    print(total_cost)
    