def second_largest(nums):
    if len(nums) < 2:
        return None   

    largest = second = float('-inf') 

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif second < num < largest:
            second = num

    return second if second != float('-inf') else None
nums = [5, 1, 9, 3, 9, 2]
print(second_largest(nums))  # Output: 5