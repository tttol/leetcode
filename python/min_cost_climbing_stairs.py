from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        elif n== 1:
            return cost[0]
        
        dp = [0] * (n + 1)
        dp[n - 1] = cost[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        print(dp)
        return min(dp[0], dp[1])
    
if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs(cost = [10,15,20]))
    print(s.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))