from collections import Counter
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing, repeating =None, None
        seen = Counter(nums)
        
        for i in range(1, n+1):
            if i not in seen: missing = i
            if seen[i] > 1: repeating =i
       
            
        return [repeating, missing]

def main():
    nums = [1,2,2,4]
    print(Solution().findErrorNums(nums))

main()