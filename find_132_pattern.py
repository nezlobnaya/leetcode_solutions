class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
       # 1 #left smallest
       # 3 # mid is the largest value
       # 2 #right is 2nd largest
       # l_132 pattern
        
        rightNumber = float('-inf')
        stack = []
        for i in range( len(nums) - 1, -1, -1):
            if nums[i] < rightNumber:
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    rightNumber = stack.pop()
                    
            stack.append(nums[i]) 
        return False

#Time complexity O(n)       