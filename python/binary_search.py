class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        
        left = 0
        right = len(nums)
        while right - left + 1 > 0:
            median = left + int(len(nums[left:right]) / 2)
            if target == nums[median]:
                return median
            elif target < nums[median]:
                right = median
            else:
                left = median
            # print(median, left, right)

s = Solution()
print(s.search([-1,0,3,5,9,12], 9))
print(s.search([-1,0,3,5,9,12], 2))
                
