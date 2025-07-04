def findMaxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    #return max_sum / k
    return max_sum
nums = [4, 2, 1, 3, 5, 6, 7]
k = 3
print(findMaxAverage(nums, k))