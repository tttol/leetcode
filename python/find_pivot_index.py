from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cumsum = [0] * (n + 1)
        cumsum[0] = 0
        for i in range(1, n + 1):
            cumsum[i] = cumsum[i - 1] + nums[i - 1]
        
        for i in range(n):
            left = cumsum[i] - cumsum[0]
            right = cumsum[n] - cumsum[i + 1]
            if left == right:
                return i
        return -1
    
s = Solution()
print(s.pivotIndex(nums = [1,7,3,6,5,6]))
print(s.pivotIndex(nums = [1,2,3]))
print(s.pivotIndex(nums = [2,1,-1]))