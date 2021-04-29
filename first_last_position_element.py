class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        output= [-1,-1]
        if not nums: return output
        l,r = 0, N
        
        while l < r:
            mid = (l +r)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid +1
        if l < N and nums[l]==target: output[0] = l
        
        l, r = 0, N
        while l < r:
            mid = (l +r)//2
            if nums[mid] <= target:
                l = mid +1
            else:
                r = mid
        if nums[r-1] == target: output[1] = r-1
            
        return output
            