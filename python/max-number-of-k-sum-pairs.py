class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0

        while left < right:
            if nums[left] + nums[right] == k:
                ans += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return ans
    
s = Solution()
print(s.maxOperations(nums = [1,2,3,4], k = 5))
print(s.maxOperations(nums = [3,1,3,4,3], k = 6))