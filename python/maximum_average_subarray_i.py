class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        average = -float('inf')
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == k:
            sum = 0
            for _nums in nums:
                sum += _nums
            return sum / k
        
        # s0 = 0
        # s1 = a0
        # s2 = a0 + a1
        # sn = a0 + a1 + ... + an-1
        cumsum = [0] * (n + 1)
        cumsum[0] = 0
        for i in range(1, n + 1):
            cumsum[i] = nums[i - 1] + cumsum[i - 1]
        
        for i in range(n):
            if i + k >= n + 1:
                break
            
            sum = cumsum[i + k] - cumsum[i]
            average = max(average, sum / k)
        return average
  
s = Solution()
print(s.findMaxAverage(nums = [0,1,1,3,3], k = 4))
print(s.findMaxAverage(nums = [9,7,3,5,6,2,0,8,1,9], k = 6))
print(s.findMaxAverage(nums = [5], k = 1))
print(s.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
print(s.findMaxAverage(nums = [4,0,4,3,3], k = 5))