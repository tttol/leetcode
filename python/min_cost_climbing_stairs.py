from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        i = 0
        total_cost = 0
        while i < n:
            if i+1 < n:
                if cost[i] < cost[i+1]:
                    total_cost += cost[i]
                    i += 1
                else:
                    total_cost += cost[i+1]
                    i += 2
            else:
                total_cost += cost[i]
                i += 1

        return total_cost
    
if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs(cost = [10,15,20]))
    print(s.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))