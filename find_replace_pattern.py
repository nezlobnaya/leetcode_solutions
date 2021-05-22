class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def get_pattern(s):
            lookup ={}
            output = []
            i =0
            for char in s:
                if char in lookup:
                    output.append(lookup[char])
                else:
                    i+=1
                    lookup[char] =i
                    output.append(i)
           
            return output
        
        p= get_pattern(pattern)
        print(p)
        output = []
        for word in words:
            if get_pattern(word) == p:
                output.append(word)
        return output

