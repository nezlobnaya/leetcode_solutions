class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        
        n =len(A)
        aux = [None] *  (n-1)
        for i in range(1, len(A)):
            aux[i-1]= A[i]-A[i-1]
        count = 0
        result = 0
        for i in range(1, len(aux)):
            if aux[i] == aux[i-1]:
                count+=1
                result+=count
            else:
                count=0
        return result

# T: O(n)
# S: O(n)

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        
        count=0
        result=0
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
              
                count+=1
                result+=count
            else:
                 count=0
        return result

# T: O(n)
# S: O(1)
        
