import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        def determine_sign(s):
            if s == '':
                return 0
            elif s[0] == '+' or re.match('[0-9]', s[0]):
                return 1
            elif s[0] == '-':
                return -1
            else:
                return 0
        
        s = s.lstrip()
        sign = determine_sign(s)
        if sign == 0:
            return 0
        
        num = 0
        for i, char in enumerate(s):
            if i == 0 and (s[i] == '+' or s[i] == '-'):
                continue
            elif not re.match('[0-9]', char):
                break
            else:
                num *= 10
                num += int(char)
        if sign == 1:
            return min(num, 2**31 - 1)
        elif sign == -1:
            return max(-num, -2**31)

s = Solution()
# print(s.myAtoi("42"))
print(s.myAtoi(" -042"))
print(s.myAtoi("   -042"))
print(s.myAtoi("1337c0d3"))
print(s.myAtoi("0-1"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("+-12"))
print(s.myAtoi("-+12"))
print(s.myAtoi("   +0 123"))
