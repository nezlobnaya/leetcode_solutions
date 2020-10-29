"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result, start = [], 0
        if len(nums) == 0: return result
        if len(nums) == 1: return [str(nums[0])]
        
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                continue
            if start == i:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start]) + '->' + str(nums[i]))
            start = i+1
        return result
        
        