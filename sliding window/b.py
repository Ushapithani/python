def maxSubarraySum(nums, k):
    if len(nums) < k:
        return None

    # window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum
    start_index = 0

    
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            start_index = i - k + 1

    print("Maximum subarray:", nums[start_index:start_index + k])
    return max_sum


nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print("Maximum sum of fixed-length subarray:", maxSubarraySum(nums, k))