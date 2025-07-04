def minSubArrayLen(target, nums):
    n = len(nums)
    min_len = n 
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len 
nums = [2, 3, 1, 2, 4, 3]
target = 7

print("Minimum subarray length:", minSubArrayLen(target, nums))