class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lookup = defaultdict(set)
        
        for w in words:
            lookup[w] =set(w)
            
        def do_not_share(w1, w2):
            if lookup[w1] & lookup[w2]: return False
            return True
            
        
        mx = 0
        for i in words:
            for j in words:
                if do_not_share(i,j):
                    mx = max(len(i) *len(j), mx)
        return mx