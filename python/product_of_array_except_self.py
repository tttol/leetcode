class Solution(object):
    def dp(self, target_arr, initial_value):
        n = len(target_arr)
        dp = [1] * n
        dp[0] = initial_value
        for i in range(1, n):
            dp[i] = dp[i - 1] * target_arr[i]
        return dp
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        dp_prefix = [1] * n
        dp_prefix[0] = nums[0]
        for i in range(1, n):
            dp_prefix[i] = dp_prefix[i - 1] * nums[i]
    
        dp_suffix = [1] * n
        dp_suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            dp_suffix[i] = dp_suffix[i + 1] * nums[i]

        ans = [0] * n
        ans[0] = dp_suffix[1]
        ans[-1] = dp_prefix[-2]
        for i in range(1, n - 1):
            ans[i] = dp_prefix[i - 1] * dp_suffix[i + 1]

        return ans
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))
print(s.productExceptSelf([2,4]))