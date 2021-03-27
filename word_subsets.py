class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans = defaultdict(int)
        count = 0
        j = 0
        while j < len(A):
            for i in range(len(B)):
                if B[i] in A[j]:
                    ans[A[j]]+=1
            j+=1
        res = []
        for k, v in ans.items():
            if v == len(B):
                res.append(k)
                

        return res

