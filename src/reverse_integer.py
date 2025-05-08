class Solution(object):
    def reverse_num(self, x):
        ret = 0
        while x > 0:
            target = x % 10
            if ret*10 + target < -2**31 or 2**31 - 1 < ret*10 + target:
                return 0
            
            ret = ret*10 + target
            x //= 10
        return ret

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = self.reverse_num(abs(x))
        if x < 0:
            ans *= -1
        return int(ans)

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(900000))
print(s.reverse(90))