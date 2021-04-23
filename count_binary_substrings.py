class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))
        
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        output = 0
        current =1
        aux =[]
        for i in range(1,len(s)):
            if int(s[i]) != int(s[i-1]):
                aux.append(current)
                current = 1
            else:
                current+=1
        aux.append(current)
        for x, y in zip(aux, aux[1:]):
            output += min(x,y)
        return output
