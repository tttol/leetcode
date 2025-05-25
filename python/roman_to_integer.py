# https://leetcode.com/problems/roman-to-integer/description/
# I II III IV V VI VII VIII IX X
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        SYMBOL = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        ans = 0
        for i in range(n):
            if i == n-1 or SYMBOL[s[i]] >= SYMBOL[s[i+1]]:
                ans += SYMBOL[s[i]]
            elif SYMBOL[s[i]] < SYMBOL[s[i+1]]:
                ans -= SYMBOL[s[i]]
        return ans

s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))