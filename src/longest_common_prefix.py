# https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs.pop()
        for s in strs:
            if len(s) < len(prefix):
                continue
            
            i = 0
            while i < min(len(s), len(prefix)):
                if s[i] != prefix[i]:
                    prefix = s[:i]
                    break
                i += 1
        return prefix

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))