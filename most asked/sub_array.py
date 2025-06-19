 '''Given an array of integers (positive, negative, or zero), find the contiguous subarray (containing at least one number)
  that has the largest possible sum, and return that sum.'''


#largest sum of sub array



def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1 :]:
        current_sum=max(num, current_sum+num)
        max_sum = max(max_sum, current_sum)
    return max_sum
nums=[1, 2 , 3, 56, -12]
print(max_sub_array(nums))