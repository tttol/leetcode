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

        if len(str1) < len(str2):
            str1, str2 = str2, str1
        while str2 != "":
            r = div(str1, str2)
            if str1 == r:
                return ""
            str1, str2 = str2, r
            
        return str1
        

s = Solution()
print(s.gcdOfStrings("ABCABC", "ABC"))
print(s.gcdOfStrings("ABABAB", "ABAB"))
print(s.gcdOfStrings("LEET", "CODE"))
print(s.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))