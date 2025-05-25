class Solution:
    def longestPalindrome(self, s):
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        n = len(s)
        for length in range(n, 0, -1):
            current_len = n - length + 1
            for start in range(current_len):
                if check(start, start + length):
                    return s[start : start + length]

        return ""
    
s = Solution()
print(s.longestPalindrome("babad"))
# print(s.longestPalindrome("cbbd"))
# print(s.longestPalindrome("bb"))
# print(s.longestPalindrome("a"))