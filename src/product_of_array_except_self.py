class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [] * n # ans[i]: i-1までの累積の積
        dp = [1] * n
        dp[0] = nums[0]

        for i in range(1, n):
            ans[i] *= nums[i - 1] * ans[i - 1]

        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i + 1]
            ans[i] *= suffix

        return ans
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))