class Solution:
    def checkSubarraySum(self, nums, k):
        total = 0
        remainder_map = {0: -1}

        for i, num in enumerate(nums):
            total += num
            remainder = total % k if k != 0 else total

            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i

        return False


sol = Solution()
nums = [23, 2, 3, 6, 7]
k = 13
print(sol.checkSubarraySum(nums, k)) 