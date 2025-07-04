def findMaxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    max_start_index = 0  

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_start_index = i - k + 1

    max_subarray = nums[max_start_index:max_start_index + k]
    print("Subarray with max average:", max_subarray)
    return max_sum  

nums = [4, 2, 1, 3, 5, 6, 7]
k = 3
print("Max average is:", findMaxAverage(nums, k))