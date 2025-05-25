# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         non_zero_ptr = 0
#         zero_ptr = 0

#         n = len(nums)
#         for i in range(n):
#             if nums[i] == 0: 
#                 zero_ptr += 1
#             else:
#                 nums[zero_ptr] = 
        
#         for _ in range(zero_ptr):
#             nums.append(0)
#         nums = nums[n:]
#         print(nums)

# s = Solution()
# s.moveZeroes([0,1,0,3,12])
# s.moveZeroes([0])