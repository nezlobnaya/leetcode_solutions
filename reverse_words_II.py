from typing import List

class Solution:
    
    def reverse_each(self, l: List) -> None:
            N=len(l)
            i, start = 0,0
            while i < N:
                if l[i] == " ":
                    length = (i- start)

                    for j in range(0,(length//2)):
                        l[start + j], l[start+length -1 -j] =  l[start+ length -1 -j], l[start+j]
                    start = i+1
                i+=1
    
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """ 
        s.reverse()
        s.append(" ")
        self.reverse_each(s)
        s.pop()
     