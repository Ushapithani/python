def move_zeroes(nums):
    zero_index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_index] = nums[i]
            zero_index += 1

    for i in range(zero_index, len(nums)):
        nums[i] = 0

    return nums
nums = [0, 1, 0, 3, 12]
result = move_zeroes(nums)
print(result)  # Output: [1, 3, 12, 0, 0]