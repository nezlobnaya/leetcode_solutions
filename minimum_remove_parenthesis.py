
"""
1249. Minimum Remove to Make Valid Parentheses

"""



class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        l = list(s)
        stack = []
        for i in range(n):
            if l[i] == '(':
                stack.append(i)
            elif l[i] == ')':
                if stack:
                    stack.pop()
                else:
                    l[i]=""
        for j in stack:
            l[j]=""

            
        return ''.join(l)
            
def main():
    s="(a(b(c)d)"
    print("Output:",Solution().minRemoveToMakeValid(s))    
main()   