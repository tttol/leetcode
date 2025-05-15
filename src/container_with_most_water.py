# https://leetcode.com/problems/container-with-most-water/description/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        water_amount = 0
        for i in range(n):
            for j in range(i + 1 ,n):
                water_amount = max(water_amount, min(height[i], height[j]) * (j - i))
        return water_amount
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))