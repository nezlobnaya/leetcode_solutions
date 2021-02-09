
class Solution:
    def intToRoman(self, num: int) -> str:
        ans=[]
        roman = {1000:'M',900:'CM',  500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        #  iterate through our dictionary and for each integer value, we divide the number by that integer value.
        # That tells us how many of those roman numerals we will need.
        for k, v in roman.items():
            ans.append(num//k*v)
            #  set number to the remainder that’s left.
            num%=k
        return "".join(ans)

num  = 1245         
print(Solution().intToRoman(num)) # MCCXLV

num  = 1248         
print(Solution().intToRoman(num)) # MCCXLVIII
# O(1) time
# O(1) space