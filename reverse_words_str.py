"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
"""

#dumb solution
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = (" ".join(s.split()[::-1]))
        return ans
        
# using pointers
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split() 
        l_ptr = 0
        r_ptr = len(arr)-1
        while l_ptr < r_ptr: 
            
            arr[l_ptr],arr[r_ptr] = arr[r_ptr],arr[l_ptr] 
            l_ptr+=1
            r_ptr-=1
        return ' '.join(arr)