class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)):
            if abs(i - A[i]) > 1: return False
        return True