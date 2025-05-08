class Solution(object):
    def get_digits(self, num):
        digits = 0
        while num > 0:
            digits += 1
            num //= 10
        return digits
    
    def reverse_num(self, x, digits):
        ret = 0
        while x > 0:
            target = x % 10

            if ret + target * 10**(digits-1) < -2**31 or 2**31 - 1 < ret + target * 10**(digits-1):
                return 0

            ret += target * 10**(digits-1)
            digits -= 1
            x //= 10
        return ret

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        ans = 0
        if x < 0:
            x *= -1
            digits = self.get_digits(x)
            ans = self.reverse_num(x, digits) * -1
        else:
            digits = self.get_digits(x)
            ans = self.reverse_num(x, digits)
        return int(ans)

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(900000))
print(s.reverse(90))