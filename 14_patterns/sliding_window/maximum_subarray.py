#Sliding window

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_total = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_total = max(max_total, max_current)
            # if max_current > max_total:
            #     max_total = max_current
        return max_total

# Time Complexity: O(n)
# Space complexity O(1)
        