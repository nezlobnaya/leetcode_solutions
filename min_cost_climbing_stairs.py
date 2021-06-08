class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N =len(cost)  
        f= [0]*N
        f[0]= cost[0]
        f[1]= cost[1]
        for i in range(2,N):
            f[i] = cost[i] + min(f[i-1], f[i-2])
        return min(f[-2:])