class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [nums[0]]
        run_sum = nums[0]

        for i in range(1, N):
            temp = run_sum+nums[i]
            run_sum = temp 
            output.append(run_sum)
        return output

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)
    
        for i in range(1, N):
            nums[i]+=nums[i-1]
        return nums