from collections import defaultdict 

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        #make a lookup using order
        
        #reorder order chars in str
        
        lookup = defaultdict(int)
        i = 0
        for char in order:
            lookup[char]=i
            i+=1
     
        
        return ''.join(sorted(str, key=lambda x:lookup[x]))
        