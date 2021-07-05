from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        aux= sorted(arr, key = lambda num: abs(x - num))
        
        output = []
        
        for i in range(k):
            output.append(aux[i])
        
        return sorted(output)
            