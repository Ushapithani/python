import bisect

def length_of_LIS(nums):
    sub = []
    for num in nums:
        i = bisect.bisect_left(sub, num)
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num     
    return len(sub)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_LIS(nums))  # Output: 4