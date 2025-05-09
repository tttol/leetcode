import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        is_positive = True
        is_encountered = False
        s = s.strip()
        for char in s:
            if char == '+' and not is_encountered:
                is_encountered = True
            elif char == '-' and not is_encountered:
                is_encountered = True
                is_positive = False
            elif not re.match('[0-9]', char):
                break
            else:
                is_encountered = True
                num *= 10
                num += int(char)
        if is_positive:
            return min(num, 2**31 - 1)
        else:
            return max(-num, -2**31)


s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi(" -042"))
print(s.myAtoi("   -042"))
print(s.myAtoi("1337c0d3"))
print(s.myAtoi("0-1"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("+-12"))
print(s.myAtoi("-+12"))
print(s.myAtoi("   +0 123"))
