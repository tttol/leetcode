# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def div(a, b):
            remainder = ""
            i = 0
            len_b = len(b)
            while i < len(a):
                if a[i:i + len_b] == b:
                    i += len_b
                else:
                    remainder = a[i:]
                    break
            return remainder
        return div(str1, str2)

        # gcd(a, b) = gcd(b, r)
        prev_remainder = ''
        while str2 != "":
            str1= str2
            str2 = div(str1, str2)
            # print(str1, str2)

            # prev_remainder = str2
            
        return str1
        

s = Solution()
print(s.gcdOfStrings("ABCABC", "ABC"))
print(s.gcdOfStrings("ABABAB", "ABAB"))
print(s.gcdOfStrings("LEET", "CODE"))