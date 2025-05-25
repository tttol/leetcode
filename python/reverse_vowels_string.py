class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v = []
        for _s in s:
            if _s in VOWELS:
                v.append(_s)
        
        ans = []
        for _s in s:
            if _s in VOWELS:
                ans.append(v.pop())
            else:
                ans.append(_s)
        return "".join(ans)

s = Solution()
print(s.reverseVowels("IceCreAm"))
print(s.reverseVowels("leetcode"))