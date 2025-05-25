# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_set = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            # 重複が発生したらcurrent_sをリセットしその時点のサイズをmax_lengthと比較
            while s[right] in str_set:
                str_set.remove(s[left])
                left += 1
            str_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            
        return max_length
            

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("a"))
print(s.lengthOfLongestSubstring(" "))
print(s.lengthOfLongestSubstring("au"))