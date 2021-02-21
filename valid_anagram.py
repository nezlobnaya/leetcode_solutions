from collections import defaultdict
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
#         aux = defaultdict(int)
#         dic = defaultdict(int)
        
#         for i in range(len(s)):
#             aux[s[i]] +=1
#         print(aux)
#         for j in range(len(t)):
#             dic[t[j]] +=1
#         return aux == dic
        # return sorted(s) == sorted(t)   
        return Counter(s) == Counter(t)
