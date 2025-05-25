# https://leetcode.com/problems/integer-to-roman/
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        SYMBOL = [
            ["I", "V"],
            ["X", "L"],
            ["C", "D"],
            ["M"],
        ]
        
        digit = 0
        roman_arr = []
        while num > 0:
            target = num % 10
            if 1 <= target <= 3:
                roman_arr.append(SYMBOL[digit][0] * target)
            elif target == 4:
                roman_arr.append(SYMBOL[digit][0] + SYMBOL[digit][1])
            elif target == 5:
                roman_arr.append(SYMBOL[digit][1])
            elif 6 <= target <= 8:
                roman_arr.append(SYMBOL[digit][1] + SYMBOL[digit][0] * (target - 5))
            elif target == 9:
                roman_arr.append(SYMBOL[digit][0] + SYMBOL[digit+1][0])
            
            num = num//10
            digit += 1
        return "".join(roman_arr[::-1])

s = Solution()
print(s.intToRoman(3749))
print(s.intToRoman(58))
print(s.intToRoman(1994))
print(s.intToRoman(10)) # X
print(s.intToRoman(100)) # C