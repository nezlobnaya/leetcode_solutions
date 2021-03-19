"""


"""

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [nums[i]- nums[i-1] for i in range(1,N) if nums[i]- nums[i-1]!=0]
        print(dp)
        if not dp: return 1
        counter=2
        for i in range(1,len(dp)):
            if dp[i-1] < 0 and dp[i] > 0 or dp[i-1] > 0 and dp[i] < 0: counter+=1

        return counter