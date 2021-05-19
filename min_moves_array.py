class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        mid = nums[N//2]
        
        return sum(abs(mid -n) for n in nums)