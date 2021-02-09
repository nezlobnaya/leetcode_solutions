"""

Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.

"""

# O(n) time complexity and O(1) space complexity
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        
        num_start, middle_num = float('inf'), float('inf')
        
        for num in nums:
            if num < num_start:
                num_start = num
            if num > num_start:
                middle_num = min(num, middle_num)
            if num > middle_num:
                return True
        return False