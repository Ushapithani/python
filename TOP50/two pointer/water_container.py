def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Calculate the area
        width = right - left
        water = min(height[left], height[right]) * width
        max_water = max(max_water, water)

        sw
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


heights = [1,8,6,2,5,4,8,3,7]
print("Maximum water that can be contained:", max_area(heights)) #Maximum water that can be contained: 49