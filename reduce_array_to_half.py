class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N =len(arr)
        aux =Counter(arr)
        ans = set()
        numbers_removed_from_arr = 0
        
        for k, v in sorted(aux.items(), key = lambda x: -x[1]):
            ans.add(k)
            numbers_removed_from_arr += v
            if (numbers_removed_from_arr >= N // 2):
                break
        return len(ans)