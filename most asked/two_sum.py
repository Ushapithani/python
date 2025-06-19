'''Given an array of integers and an integer target, return indices of the 
two numbers such that they add up to target'''




def two_sum(nums,target):
    num_dict={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in num_dict:
            return (num_dict[complement], i) #covert tuple output into list return [num_dict[complement], i]

        num_dict[num]=i
    return []
nums=[3,1,5,7]
target=8
print(two_sum(nums, target))