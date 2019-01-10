def twosum(nums, target):
    for i in range(len(nums)-1, 0, -1):
        if target-nums[i] in nums:
            if i != nums.index(target-nums[i]):
                return [nums.index(target-nums[i]), i]
    return None


print(twosum([2,7,5,11], 9))
print(twosum([1,2,5,7,4], 6))
print(twosum([3,3], 6))