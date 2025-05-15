# https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def lcp(s1, s2):
            longest_common_prefix = ""
            for i in range(min(len(s1), len(s2))):
                if s1[i] != s2[i]:
                    break
                longest_common_prefix += s1[i]
            return longest_common_prefix

        n = len(strs)
        if n == 1:
            return strs[0]
        elif n == 2:
            return lcp(strs[0], strs[1])
        else:
            prefix = lcp(strs[0], strs[1])
            for i in range(2, len(strs)):
                prefix = lcp(prefix, strs[i])
            return prefix



s = Solution()
print(s.longestCommonPrefix(["reflower","flow","flight"]))
print(s.longestCommonPrefix(["a"]))
print(s.longestCommonPrefix([""]))
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["minimum","min"]))
print(s.longestCommonPrefix(["","b"]))