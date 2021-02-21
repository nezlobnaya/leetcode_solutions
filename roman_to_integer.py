class Solution:
#     def romanToInt(self, s: str) -> int:
#         res = 0
#         romans={"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000, }
#         i=0
#         while i < len(s):
#             if i +1 < len(s) and romans[s[i]] < romans[s[i+1]]:
#                 res += romans[s[i+1]] - romans[s[i]]
#                 i+=2
#             else: 
#                 res +=romans[s[i]]
#                 i +=1
                    
                   
            
#         return res
# improved solution
        def romanToInt(self, s: str) -> int:
            
            romans= {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,                    'IV': 4,'I': 1}
            res = 0
            i=0
            while i < len(s):
                if i < len(s) - 1 and s[i:i+2] in romans:
                    res += romans[s[i:i+2]] 
                    i+=2
                else: 
                    res +=romans[s[i]]
                    i +=1
                    # increase index
                        
                    
                
            return res



def main():
    s = "MCMXCIV"
    print(Solution().romanToInt(s))


main()