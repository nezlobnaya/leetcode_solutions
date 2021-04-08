class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup={2:"abc", 3:"def", 4:"ghi", 5:"jkl",6:"mno",
                7:"pqrs",8:"tuv",9:"wxyz"}
        N = len(digits)
        if not digits: return []
        
        ans=[""]
       
        for char in digits:
            aux=[]
            for v in lookup[int(char)]:
                for a in ans:
                    aux.append(a+v)
            ans=aux

        return ans
     
        

                
        
        