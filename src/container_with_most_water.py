# https://leetcode.com/problems/container-with-most-water/description/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # 愚直解
        def on2(height):
            n = len(height)
            water_amount = 0
            for i in range(n):
                for j in range(i + 1 ,n):
                    water_amount = max(water_amount, min(height[i], height[j]) * (j - i))
            return water_amount
        
        def pointers(height):
            left = 0
            right = len(height) - 1
            water_amount = 0
            while left < right:
                water_amount = max(water_amount, (right - left) * min(height[left], height[right]))
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
            return water_amount

        return pointers(height)
            
        # dp[i][j] = i番目までの中で最大の高さとそのindexを保持
        # dp[i] * dp[i+1]で最大値を走査？
        # def dp(height):
        #     n = len(height)
        #     dp = [[0 for _ in range(2)] for _ in range(n)]
        #     dp[0][0], dp[0][1] = 0, height[0]
        #     for i in range(1, n):
        #         if dp[i-1][1] < height[i]:
        #             dp[i][0], dp[i][1] = i, height[i]
        #         else:
        #             dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]
        #     print(dp)

        #     return 0
        
        # return dp(height)
    
            
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))