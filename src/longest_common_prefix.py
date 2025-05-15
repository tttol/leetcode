# https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        first = strs[0]
        last = strs[-1]

        ans = ""
        for i in range(len(first)):
            if first[i] != last[i]:
                break
            ans += first[i]
        return ans

s = Solution()
print(s.longestCommonPrefix(["reflower","flow","flight"]))
print(s.longestCommonPrefix(["a"]))
print(s.longestCommonPrefix([""]))
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["minimum","min"]))
print(s.longestCommonPrefix(["","b"]))