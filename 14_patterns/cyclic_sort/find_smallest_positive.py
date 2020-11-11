"""
Given an unsorted integer array nums, find the smallest missing positive integer.
"""

def firstMissingPositive(nums):
    nums.sort()
    if not nums or (nums[-1] < 1) :
        return 1

    for i in range(1, nums[-1]+1):
        if i not in nums:
            return i

    return nums[-1]+1

"""
Time/Space: O(n)/O(1)
"""