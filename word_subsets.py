class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        total = {}
        for b in B:
            temp=Counter(b)
            for k, v in temp.items():
                if k not in total:
                    total[k] = v
                    print('TOTAL', total)
                else: total[k] = max(v, total[k])
        print(total)
        res = []
        for a in A:
            tmp = Counter(a)
            if all([k in tmp and v <=tmp[k] for k, v in total.items()]):
                res.append(a)
        return res

