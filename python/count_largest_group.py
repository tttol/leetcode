# https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23
class Solution(object):

    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_map = [0 for _ in range(100)]
        largest = 0
        for i in range(1, n + 1):
            sum = self.sum_digits(i)
            sum_map[sum] += 1
            largest = max(largest, sum_map[sum])

        ans = 0
        for sm in sum_map:
            if sm == largest:
                ans += 1

        return ans
    
    def sum_digits(self, n):
        sum = 0
        while n >= 1:
            sum += n % 10
            n = int(n/10)
        return sum
    
            
            
        
# Example of how to call the countLargestGroup method
# solution = Solution()
# result = solution.countLargestGroup(13)
# print("Result:", result)
