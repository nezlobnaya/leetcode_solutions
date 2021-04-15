class Solution:
    def fib(self, n: int) -> int:
        if n <2: return n
        prev_prev = 0
        prev = 1
        current = 0
        
        for i in range(2, n+1):
            current = prev_prev + prev
            
            prev_prev = prev
            prev = current
            
        return current