class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result, currentSum = 0, 0
        N =len(nums)
        seen = set()
        
        start=0
        
        for end in range(N):
            while nums[end] in seen:
                seen.remove(nums[start])
                currentSum -=nums[start]
                start+=1
            seen.add(nums[end])
            currentSum += nums[end]
            result = max(result, currentSum)
        
        return result
        