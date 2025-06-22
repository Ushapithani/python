def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]