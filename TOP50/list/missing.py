def find_missing_number(nums):
    n = len(nums) + 1  #  one number is missing
    total = n * (n + 1) // 2  
    return total - sum(nums)
nums = [1, 2, 3, 5]
print(find_missing_number(nums))  # Output: 4