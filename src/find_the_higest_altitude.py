from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cumsum = [0] * (len(gain) + 1)
        cumsum[0] = 0
        for i in range(1, len(gain) + 1):
            cumsum[i] = cumsum[i - 1] + gain[i - 1]
        return max(cumsum)
    
s = Solution()
print(s.largestAltitude(gain = [-5,1,5,0,-7]))
print(s.largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))