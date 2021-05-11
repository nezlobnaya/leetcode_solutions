class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N=len(cardPoints)
        total = sum(cardPoints)
        L_sub_arr = N-k
        mn = current_sum = sum(cardPoints[:L_sub_arr])
        print("Initial",current_sum)
        
        for i in range(k):
            current_sum-= cardPoints[i]
            print("Point",cardPoints[i])
            print("Sum current",current_sum)
            current_sum+=cardPoints[i+L_sub_arr]
            print("Point aux",cardPoints[i+L_sub_arr])
            print("Sum current aux",current_sum )
            
            mn = min(mn, current_sum)
        return total-mn
            
    