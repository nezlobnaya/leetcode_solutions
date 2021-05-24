class Solution:
    def toLowerCase(self, s: str) -> str:
        output = []
        for char in s:
            if char.isupper(): 
                output.append(chr(ord(char)+32))
            else:
                output.append(char)
        return "".join(output)