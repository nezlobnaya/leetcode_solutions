"""
1461. Check If a String Contains All Binary Codes of Size K
"""
import math
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        N =len(s)
        if N < k: return False
        
        hash = set()

        for i in range(N):
            if len(s[i:i+k]) == k:
                hash.add(s[i:i+k])

        return len(hash) == math.pow(2, k)