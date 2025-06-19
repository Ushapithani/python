''''Given an array nums of n integers, return an array of all the unique 
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
 0 <= a, b, c, d < n
 a, b, c, and d are distinct.
 nums[a] + nums[b] + nums[c] + nums[d] == target'''

def four_sum(nums, target):
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        quad = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                        result.add(quad)

    return [list(quad) for quad in result]


nums = list(map(int, input("Enter the numbers in the array: ").split()))
target = int(input("Enter the target sum: "))
u = four_sum(nums, target)
print(u)