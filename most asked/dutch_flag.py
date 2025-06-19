 ''''Given an array nums with n objects colored red, white, or blue, sort 
them in-place so that objects of the same color are adjacent, with 
the colors in the order red, white, and blue.'''




def sortColors(nums):

    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


nums = list(map(int, input("Enter 0s, 1s, and 2s separated by spaces: ").split()))
sortColors(nums)
print("Sorted colors:", nums)