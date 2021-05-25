class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        def is_Num(n):
            try:     
                int(n)
                return True
            except:
                return False
        
        for token in tokens:
            if is_Num(token):
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "+": c = a+b
                elif token == "-": c = b-a
                elif token =="*": c = a*b
                elif token == "/": c= int(b/a)
                stack.append(str(c))
        return stack[-1]
      