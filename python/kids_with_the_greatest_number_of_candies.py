class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candiy = max(candies)
        return [c + extraCandies >= max_candiy for c in candies]

s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))
print(s.kidsWithCandies([4,2,1,1,2], 1))
print(s.kidsWithCandies([12,1,12], 1))