class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        MOD = 10**9 + 7
        dp = [[0]*5 for _ in range(n+1)]
        
        # dp[i][0] = number of ways to have i characters and ending with 'a'
        # dp[i][1] = number of ways to have i characters and ending with 'e'
        # dp[i][2] = number of ways to have i characters and ending with 'i'
        # dp[i][3] = number of ways to have i characters and ending with 'o'
        # dp[i][4] = number of ways to have i characters and ending with 'u'
        
        for j in range(5):
            dp[1][j]=1
            
       
        
        
        for i in range(2, n+1):
             # Each vowel 'a' may only be followed by an 'e'.
             # Each vowel 'e' may only be followed by an 'a' or an 'i'.
             # Each vowel 'i' may not be followed by another 'i'.
             # Each vowel 'o' may only be followed by an 'i' or a 'u'.
             # Each vowel 'u' may only be followed by an 'a'.
                dp[i][0] = dp[i-1][1] + dp[i-1][2] + dp[i-1][4]
                dp[i][1] = dp[i-1][0] + dp[i-1][2]  
                dp[i][2] = dp[i-1][1] + dp[i-1][3] 
                dp[i][3] = dp[i-1][2]
                dp[i][4] = dp[i-1][2] + dp[i-1][3]

            
            
        return sum(dp[n]) % MOD