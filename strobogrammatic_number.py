"""
246. Strobogrammatic Number

"""

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotate = []
        for char in num[::-1]:
            if char == '0' or char=='1' or char == '8':
                rotate.append(char)
            elif char == '9':
                rotate.append('6')
            elif char == '6':
                rotate.append('9')
            else: 
                return False
        rotate = ''.join(rotate)
        return rotate == num