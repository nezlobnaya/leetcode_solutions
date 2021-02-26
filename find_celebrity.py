# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        for i in range(n):
            if self.isCelebrity(i):
                return i
        return -1
        
    def isCelebrity(self,i):
        for j in range(self.n):
            if i == j: continue
            if knows(i,j) or not knows(j,i):
                return False
        return True
