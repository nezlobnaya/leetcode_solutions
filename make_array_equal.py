class Solution:
    def minOperations(self, n: int) -> int:
        arr=[]
        for i in range(n):
            arr.append((2 * i) + 1)
            
        target = sum(arr)//n
        count=0
        for i in range(n):
            count+=abs(arr[i]-target)

        return count//2