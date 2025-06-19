def search(arr, key):
    for element in arr:
        if element == key:
            return True
    return False

key = int(input())                      
arr = list(map(int, input().split()))  

print("YES" if search(arr, key) else "NO")