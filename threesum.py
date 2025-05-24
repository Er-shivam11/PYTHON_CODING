def threeSum(nums):
    n = len(nums)
    res = []

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in res:
                        res.append(triplet)
    return res

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
