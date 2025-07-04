class Solution:
    def alternatingSubarray(self, nums):
        n = len(nums)
        max_len = -1

        for i in range(n - 1):
            if nums[i + 1] - nums[i] == 1:
                length = 2
                for j in range(i + 2, n):
                    if nums[j] == nums[j - 2]:
                        length += 1
                    else:
                        break
                max_len = max(max_len, length)

        return max_len