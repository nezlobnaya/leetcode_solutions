class Solution:
    def minOperations(self, n: int) -> int:
        arr=[]
        for i in range(n):
            arr.append((2 * i) + 1)
            
        target = sum(arr)//n
        count=0
        for i in range(n):
            diff = abs(arr[i]-target)
            count+=diff
        return count//2