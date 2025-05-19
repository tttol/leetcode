class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = 2**31 - 1
        second = 2**31 - 1

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

s = Solution()
# print(s.increasingTriplet([1,2,1,3])) # True
# print(s.increasingTriplet([1,2,3,4,5])) # True
# print(s.increasingTriplet([5,4,3,2,1])) # False
# print(s.increasingTriplet([2,1,5,0,4,6])) # True
print(s.increasingTriplet([20,100,10,12,5,13])) # True