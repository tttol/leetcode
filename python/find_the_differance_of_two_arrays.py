from typing import List


class Solution:
    def distinct(self, target_set: set, others_set: set):
        ret = []
        for ts in target_set:
            if ts not in others_set:
                ret.append(ts)
        return ret
            
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [self.distinct(set1, set2), self.distinct(set2, set1)]


s = Solution()
print(s.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))
print(s.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))