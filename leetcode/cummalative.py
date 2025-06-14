def cumulative_sum(lst):
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result


numbers = [1, 2, 3, 4, 5]
print(f"Cumulative sum: {cumulative_sum(numbers)}")