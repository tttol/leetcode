class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sub_ptr = 0
        sub_len = len(s)
        if sub_len < 1:
            return True
        for _t in t:
            if s[sub_ptr] == _t:
                sub_ptr += 1
            
            if sub_ptr == sub_len:
                return True
        return False

s = Solution()
print(s.isSubsequence(s = "abc", t = "ahbgdc"))
print(s.isSubsequence(s = "axc", t = "ahbgdc"))
print(s.isSubsequence(s = "aaa", t = "ahbgdasfseafaac"))
print(s.isSubsequence(s = "", t = "ahbgdc"))