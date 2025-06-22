def rotate_list( nums, k, direction = 'right'):
    n = len(nums)
    k = k % n
    if direction =='right':
        return nums[-k: ] + nums[ : -k]
    elif direction=='left':
        return nums[k: ] + nums[ :k]
    else:
        return error ("direction must be left or right")


my_list = [1, 2, 3, 4, 5]
rotated = rotate_list(my_list, 2, direction='right')
print(rotated)  # Output: [3, 4, 5, 1, 2]=left
                           #[4, 5, 1, 2, 3] =right


    
        
