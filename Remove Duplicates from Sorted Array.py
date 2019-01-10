def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    r = 1
    i = 0
    while i < len(nums)-1:
        if nums[i] != nums[i+1]:
            r = r + 1
            i = i + 1
        else:
            nums.remove(nums[i])


    return r

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
