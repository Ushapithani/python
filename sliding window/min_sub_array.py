def minSubArrayLen(target, nums):
    n = len(nums)
    min_len = n + 1  
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_len == n + 1 else min_len


target = 7
nums = [2, 3, 1, 2, 4, 3]
print("Minimum subarray length:", minSubArrayLen(target, nums))