class Solution:
    def minPartitions(self, n: str) -> int:
        # m = float('-inf')
        # for char in n:
        #     m=max(int(char), m)
        # return m
        return max(num for num in n)
            
       