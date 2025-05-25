# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Use sliding window technique
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If the character is already in the set, move the left pointer
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
            
        return max_length

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("a"))
print(s.lengthOfLongestSubstring(" "))
print(s.lengthOfLongestSubstring("au"))